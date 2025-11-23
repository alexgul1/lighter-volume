import asyncio
import random
import time
import uuid
from typing import Dict, Optional, List, Tuple
from dataclasses import dataclass
import lighter

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats
from src.telegram_notifier import TelegramNotifier
from src.position_monitor import PositionMonitor
from src.account_manager import AccountManager

logger = setup_logger(__name__, Config.LOG_LEVEL)


@dataclass
class MarketData:
    """Market data from order book details"""
    symbol: str
    market_id: int
    last_trade_price: float
    open_interest: float
    size_decimals: int
    price_decimals: int


class Position:
    """Represents a single position in the hedged trading strategy"""

    def __init__(self, position_id: str, token: str, position_type: str,
                 is_long: bool, base_amount: int, amount_usdc: float,
                 open_order_index: int, open_tx_id: int, account_num: int,
                 entry_price: float):
        self.position_id = position_id
        self.token = token
        self.position_type = position_type
        self.is_long = is_long
        self.base_amount = base_amount
        self.amount_usdc = amount_usdc
        self.open_order_index = open_order_index
        self.open_tx_id = open_tx_id
        self.account_num = account_num  # 1 or 2
        self.entry_price = entry_price
        self.open_time = time.time()
        self.is_closing = False  # Flag to prevent double closing
        self.paired_position_id: Optional[str] = None  # ID of the hedged pair


class TradingEngine:
    """
    Hedged futures trading engine for Lighter Protocol.
    Opens opposing positions (long/short) across two accounts to hedge risk
    while maximizing farming rewards on low OI tokens.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

        # Account manager for isolated worker processes
        self.account_manager: Optional[AccountManager] = None

        # Shared API clients for read operations
        self.api_client = None
        self.order_api = None
        self.account_api = None

        # Telegram notifications
        self.telegram: Optional[TelegramNotifier] = None

        # Position monitoring
        self.position_monitor: Optional[PositionMonitor] = None

        # Trading state
        self.active_positions: Dict[str, Position] = {}  # position_id -> Position
        self.positions_by_token: Dict[str, List[str]] = {}  # token -> list of position_ids
        self.running = False
        self.stats = Stats()
        self.start_time = time.time()

        # Market data cache
        self.market_data_cache: Dict[str, MarketData] = {}  # token -> MarketData
        self.cache_timestamp = 0
        self.cache_ttl = Config.MARKET_DATA_CACHE_TTL  # Adaptive caching based on account type

        # Track order indices per account (for worker processes)
        self.next_order_index_1 = 1000
        self.next_order_index_2 = 2000
        self._order_index_lock = asyncio.Lock()

        # Error tracking for automatic recovery
        self.consecutive_failures = 0

    async def initialize(self):
        """Initialize Lighter clients for dual account hedging with process isolation"""
        try:
            logger.info("🔧 Initializing Account Manager with isolated worker processes...")

            # Verify account configuration (security check)
            pk1_hash = Config.ACCOUNT_1_PRIVATE_KEY[:8] + "..." + Config.ACCOUNT_1_PRIVATE_KEY[-8:]
            pk2_hash = Config.ACCOUNT_2_PRIVATE_KEY[:8] + "..." + Config.ACCOUNT_2_PRIVATE_KEY[-8:]
            logger.info(f"🔑 Account 1: index={Config.ACCOUNT_1_INDEX}, api_key_index={Config.ACCOUNT_1_API_KEY_INDEX}, pk={pk1_hash}")
            logger.info(f"🔑 Account 2: index={Config.ACCOUNT_2_INDEX}, api_key_index={Config.ACCOUNT_2_API_KEY_INDEX}, pk={pk2_hash}")

            if Config.ACCOUNT_1_PRIVATE_KEY == Config.ACCOUNT_2_PRIVATE_KEY:
                logger.error("❌ CRITICAL: Both accounts use the SAME private key! This will cause nonce conflicts!")
                raise Exception("Both accounts cannot use the same private key")

            if Config.ACCOUNT_1_INDEX == Config.ACCOUNT_2_INDEX and Config.ACCOUNT_1_API_KEY_INDEX == Config.ACCOUNT_2_API_KEY_INDEX:
                logger.error("❌ CRITICAL: Both accounts have SAME index configuration! This will cause nonce conflicts!")
                raise Exception("Accounts must have different index configurations")

            logger.info("✅ Account configurations are valid (different keys/indices)")

            # Initialize Account Manager (handles process isolation)
            self.account_manager = AccountManager()
            logger.info("✅ Account Manager initialized with multiprocessing isolation")

            # Shared API clients for read operations (order, account)
            configuration = lighter.Configuration(Config.BASE_URL)
            self.api_client = lighter.ApiClient(configuration)
            self.order_api = lighter.OrderApi(self.api_client)
            self.account_api = lighter.AccountApi(self.api_client)

            # Set leverage for all markets on both accounts
            await self._set_leverage_for_markets()

            # Initialize Telegram notifications
            if Config.TELEGRAM_ENABLE_NOTIFICATIONS and Config.TELEGRAM_BOT_TOKEN:
                self.telegram = TelegramNotifier(
                    bot_token=Config.TELEGRAM_BOT_TOKEN,
                    chat_id=Config.TELEGRAM_CHAT_ID,
                    message_thread_id=int(Config.TELEGRAM_TOPIC_ID) if Config.TELEGRAM_TOPIC_ID else None
                )
                await self.telegram.initialize()

                # Register Telegram commands
                self.telegram.register_command("balance", self._handle_balance_command)
                self.telegram.register_command("pnl", self._handle_pnl_command)
                self.telegram.register_command("status", self._handle_status_command)
                self.telegram.register_command("help", self._handle_help_command)

                # Start command polling
                await self.telegram.start_command_polling()

                logger.info("Telegram notifications and commands enabled")
            else:
                logger.warning("Telegram notifications disabled")

            # Initialize Position Monitor
            if Config.ENABLE_POSITION_MONITORING:
                self.position_monitor = PositionMonitor(
                    account_api=self.account_api,
                    order_api=self.order_api,
                    account_1_index=Config.ACCOUNT_1_INDEX,
                    account_2_index=Config.ACCOUNT_2_INDEX
                )
                await self.position_monitor.start()
                logger.info(f"Position monitoring enabled (interval: {Config.POSITION_MONITOR_INTERVAL}s)")
            else:
                logger.warning("Position monitoring disabled")

            logger.info(f"🎯 Hedged trading engine initialized")
            logger.info(f"Account 1: Index {Config.ACCOUNT_1_INDEX}")
            logger.info(f"Account 2: Index {Config.ACCOUNT_2_INDEX}")
            logger.info(f"Leverage: {Config.DEFAULT_LEVERAGE}x")
            logger.info(f"Strategy: Dual account hedging (long/short pairs)")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def _set_leverage_for_markets(self):
        """Set leverage for all trading markets on both accounts via worker processes"""
        logger.info("Setting leverage for all trading markets on both accounts...")

        for token in Config.TRADING_TOKENS:
            market_index = Config.MARKET_INDICES.get(token)
            if market_index is None:
                continue

            # Set leverage on Account 1 via worker process
            success_1 = await self.account_manager.set_leverage(
                account_num=1,
                token=token,
                market_index=market_index,
                leverage=Config.DEFAULT_LEVERAGE
            )

            if success_1:
                logger.info(f"✅ Set leverage {Config.DEFAULT_LEVERAGE}x for {token} on Account 1")
            else:
                logger.error(f"❌ Failed to set leverage for {token} on Account 1")

            # Respect rate limits between API calls
            await asyncio.sleep(Config.SAFE_DELAY_BETWEEN_TRADES)

            # Set leverage on Account 2 via worker process
            success_2 = await self.account_manager.set_leverage(
                account_num=2,
                token=token,
                market_index=market_index,
                leverage=Config.DEFAULT_LEVERAGE
            )

            if success_2:
                logger.info(f"✅ Set leverage {Config.DEFAULT_LEVERAGE}x for {token} on Account 2")
            else:
                logger.error(f"❌ Failed to set leverage for {token} on Account 2")

            # Respect rate limits between markets
            await asyncio.sleep(Config.SAFE_DELAY_BETWEEN_TRADES)

        logger.info("✅ Leverage updates completed for all markets")

    async def cleanup(self):
        """Cleanup resources"""
        if self.position_monitor:
            await self.position_monitor.stop()
        if self.telegram:
            await self.telegram.cleanup()
        if self.api_client:
            await self.api_client.close()

    async def get_account_balance(self, account_num: int) -> Tuple[float, float]:
        """
        Get account balance and PnL.

        Args:
            account_num: Account number (1 or 2)

        Returns:
            Tuple of (available_balance, total_pnl)
        """
        try:
            account_index = Config.ACCOUNT_1_INDEX if account_num == 1 else Config.ACCOUNT_2_INDEX
            logger.debug(f"Fetching balance for Account {account_num} (index={account_index})")

            response = await self.account_api.account(by="index", value=str(account_index))

            # 🔍 FULL DEBUG LOGGING
            logger.info(f"🔍 === FULL API Response for Account {account_num} (index={account_index}) ===")
            logger.info(f"Response type: {type(response)}")
            logger.info(f"Response dir: {dir(response)}")
            logger.info(f"Response repr: {repr(response)}")

            # Try to log response as dict if possible
            if hasattr(response, '__dict__'):
                logger.info(f"Response __dict__: {response.__dict__}")

            # Try to convert to dict/json
            try:
                import json
                if hasattr(response, 'to_dict'):
                    logger.info(f"Response to_dict():\n{json.dumps(response.to_dict(), indent=2, default=str)}")
                elif hasattr(response, 'dict'):
                    logger.info(f"Response dict():\n{json.dumps(response.dict(), indent=2, default=str)}")
            except Exception as e:
                logger.debug(f"Could not serialize response to JSON: {e}")

            logger.info(f"🔍 === END Response Debug ===\n")

            # Handle different response formats from lighter SDK
            account_data = None
            if hasattr(response, 'data') and response.data:
                logger.debug(f"Using response.data[0], data length: {len(response.data)}")
                account_data = response.data[0]
            elif hasattr(response, 'sub_accounts') and response.sub_accounts:
                logger.debug(f"Using response.sub_accounts[0], sub_accounts length: {len(response.sub_accounts)}")
                account_data = response.sub_accounts[0]
            elif hasattr(response, '__getitem__'):
                logger.debug("Using response[0] (directly indexable)")
                account_data = response[0]
            else:
                logger.debug("Using response itself as account_data")
                account_data = response

            if not account_data:
                logger.warning(f"Account {account_num}: No account data found")
                return (0.0, 0.0)

            # Debug: Log account_data details
            logger.debug(f"Account data type: {type(account_data)}")
            logger.debug(f"Account data attributes: {dir(account_data)}")

            # Get available balance (USDC)
            if hasattr(account_data, 'available_balance'):
                logger.debug(f"Account {account_num} available_balance raw: {account_data.available_balance} (type: {type(account_data.available_balance)})")
            else:
                logger.warning(f"Account {account_num}: No 'available_balance' attribute")

            available_balance = float(account_data.available_balance) if hasattr(account_data, 'available_balance') and account_data.available_balance else 0.0
            logger.info(f"Account {account_num} parsed available_balance: ${available_balance}")

            # Calculate total PnL (unrealized + realized)
            total_pnl = 0.0
            if hasattr(account_data, 'positions'):
                logger.debug(f"Account {account_num} has {len(account_data.positions)} positions")
                for position in account_data.positions:
                    unrealized_pnl = float(position.unrealized_pnl) if position.unrealized_pnl else 0.0
                    realized_pnl = float(position.realized_pnl) if position.realized_pnl else 0.0
                    total_pnl += unrealized_pnl + realized_pnl
                    logger.debug(f"Position: unrealized={unrealized_pnl}, realized={realized_pnl}")
            else:
                logger.debug(f"Account {account_num}: No 'positions' attribute")

            logger.info(f"Account {account_num} total PnL: ${total_pnl}")
            return (available_balance, total_pnl)

        except Exception as e:
            logger.error(f"Failed to get account {account_num} balance: {e}", exc_info=True)
            return (0.0, 0.0)

    async def get_account_position_count(self, account_num: int) -> int:
        """Get number of open positions for an account"""
        try:
            account_index = Config.ACCOUNT_1_INDEX if account_num == 1 else Config.ACCOUNT_2_INDEX
            response = await self.account_api.account(by="index", value=str(account_index))

            # Handle different response formats from lighter SDK
            account_data = None
            if hasattr(response, 'data') and response.data:
                account_data = response.data[0]
            elif hasattr(response, 'sub_accounts') and response.sub_accounts:
                account_data = response.sub_accounts[0]
            elif hasattr(response, '__getitem__'):
                account_data = response[0]
            else:
                account_data = response

            if not account_data or not hasattr(account_data, 'positions'):
                return 0

            count = sum(1 for pos in account_data.positions if float(pos.position) != 0)
            return count

        except Exception as e:
            logger.error(f"Failed to get account {account_num} position count: {e}")
            return 0

    async def check_and_alert_low_balance(self):
        """Check both accounts for low balance and send alerts if needed"""
        min_balance = Config.MAX_TRADE_AMOUNT * 3

        # Check Account 1
        balance_1, _ = await self.get_account_balance(1)
        if balance_1 < min_balance and self.telegram:
            await self.telegram.notify_low_balance_alert(
                account_num=1,
                current_balance=balance_1,
                min_balance=min_balance,
                max_trade_amount=Config.MAX_TRADE_AMOUNT
            )

        # Check Account 2
        balance_2, _ = await self.get_account_balance(2)
        if balance_2 < min_balance and self.telegram:
            await self.telegram.notify_low_balance_alert(
                account_num=2,
                current_balance=balance_2,
                min_balance=min_balance,
                max_trade_amount=Config.MAX_TRADE_AMOUNT
            )

    async def send_balance_notification(self):
        """Send balance and PnL notification after position close"""
        if not self.telegram:
            return

        try:
            # Get balances and PnL for both accounts
            balance_1, pnl_1 = await self.get_account_balance(1)
            balance_2, pnl_2 = await self.get_account_balance(2)

            total_balance = balance_1 + balance_2
            total_pnl = pnl_1 + pnl_2
            min_balance = Config.MAX_TRADE_AMOUNT * 3

            await self.telegram.notify_balance_after_close(
                account_1_balance=balance_1,
                account_1_pnl=pnl_1,
                account_2_balance=balance_2,
                account_2_pnl=pnl_2,
                total_balance=total_balance,
                total_pnl=total_pnl,
                min_balance_threshold=min_balance
            )

            # Check and send low balance alerts
            await self.check_and_alert_low_balance()

        except Exception as e:
            logger.error(f"Failed to send balance notification: {e}")

    # Telegram command handlers
    async def _handle_balance_command(self) -> str:
        """Handle /balance command"""
        try:
            balance_1, _ = await self.get_account_balance(1)
            balance_2, _ = await self.get_account_balance(2)
            total_balance = balance_1 + balance_2

            return (
                f"💰 <b>Account Balances</b>\n\n"
                f"<b>Account 1:</b> ${balance_1:,.2f}\n"
                f"<b>Account 2:</b> ${balance_2:,.2f}\n"
                f"<b>Total:</b> ${total_balance:,.2f}\n"
                f"\n⏰ {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}"
            )
        except Exception as e:
            return f"❌ Error fetching balances: {e}"

    async def _handle_pnl_command(self) -> str:
        """Handle /pnl command"""
        try:
            _, pnl_1 = await self.get_account_balance(1)
            _, pnl_2 = await self.get_account_balance(2)
            total_pnl = pnl_1 + pnl_2

            pnl1_emoji = "💚" if pnl_1 >= 0 else "❤️"
            pnl2_emoji = "💚" if pnl_2 >= 0 else "❤️"
            total_pnl_emoji = "💚" if total_pnl >= 0 else "❤️"

            return (
                f"📊 <b>Profit & Loss</b>\n\n"
                f"<b>Account 1:</b> {pnl1_emoji} ${pnl_1:+.2f}\n"
                f"<b>Account 2:</b> {pnl2_emoji} ${pnl_2:+.2f}\n"
                f"<b>Total:</b> {total_pnl_emoji} <b>${total_pnl:+.2f}</b>\n"
                f"\n⏰ {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}"
            )
        except Exception as e:
            return f"❌ Error fetching P/L: {e}"

    async def _handle_status_command(self) -> str:
        """Handle /status command"""
        try:
            balance_1, pnl_1 = await self.get_account_balance(1)
            balance_2, pnl_2 = await self.get_account_balance(2)
            pos_count_1 = await self.get_account_position_count(1)
            pos_count_2 = await self.get_account_position_count(2)

            uptime = (time.time() - self.start_time) / 3600

            if self.telegram:
                await self.telegram.notify_account_status(
                    account_1_balance=balance_1,
                    account_1_pnl=pnl_1,
                    account_1_positions=pos_count_1,
                    account_2_balance=balance_2,
                    account_2_pnl=pnl_2,
                    account_2_positions=pos_count_2,
                    uptime_hours=uptime
                )

            return ""  # Already sent via notify_account_status
        except Exception as e:
            return f"❌ Error fetching status: {e}"

    async def _handle_help_command(self) -> str:
        """Handle /help command"""
        return (
            f"🤖 <b>Lighter Bot Commands</b>\n\n"
            f"/balance - Show account balances\n"
            f"/pnl - Show profit & loss\n"
            f"/status - Full account status\n"
            f"/help - Show this help message\n"
            f"\n<b>Bot Info:</b>\n"
            f"Strategy: Dual account hedging\n"
            f"Tokens: {', '.join(Config.TRADING_TOKENS)}\n"
            f"Leverage: {Config.DEFAULT_LEVERAGE}x\n"
        )

    async def get_market_data(self, token: str, force_refresh: bool = False) -> Optional[MarketData]:
        """
        Get market data including price and open interest for a token.
        Uses caching to reduce API calls.
        """
        # Check cache
        current_time = time.time()
        if not force_refresh and token in self.market_data_cache:
            if current_time - self.cache_timestamp < self.cache_ttl:
                return self.market_data_cache[token]

        # Fetch from API
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            logger.error(f"Unknown market for token {token}")
            return None

        try:
            # Get order book details
            details_response = await self.order_api.order_book_details(market_id=market_index)

            if not details_response.order_book_details:
                logger.error(f"No order book details for {token}")
                return None

            detail = details_response.order_book_details[0]

            # Debug OI calculation
            logger.info(f"🔍 OI Debug for {token}:")
            logger.info(f"  Raw OI from API: {detail.open_interest}")
            logger.info(f"  Price: ${detail.last_trade_price}")
            logger.info(f"  Size decimals: {detail.size_decimals}")
            logger.info(f"  Price decimals: {detail.price_decimals}")

            # OI is already in USDC - no conversion needed!
            # The API returns open_interest directly in USDC
            oi_in_usdc = float(detail.open_interest) if detail.open_interest else 0.0

            logger.info(f"  Final OI (USDC): ${oi_in_usdc:,.2f}")

            market_data = MarketData(
                symbol=detail.symbol,
                market_id=detail.market_id,
                last_trade_price=detail.last_trade_price,
                open_interest=oi_in_usdc,
                size_decimals=detail.size_decimals,
                price_decimals=detail.price_decimals
            )

            # Update cache
            self.market_data_cache[token] = market_data
            self.cache_timestamp = current_time

            return market_data

        except Exception as e:
            logger.error(f"Failed to get market data for {token}: {e}")
            return None

    async def get_all_market_data(self) -> Dict[str, MarketData]:
        """
        Get market data for all trading tokens.
        Uses rate-limit-friendly delays between requests.
        """
        market_data = {}
        for i, token in enumerate(Config.TRADING_TOKENS):
            data = await self.get_market_data(token, force_refresh=True)
            if data:
                market_data[token] = data

            # Add delay between requests (except after last one)
            # Standard: 7s delay, Premium: 0.5s delay
            if i < len(Config.TRADING_TOKENS) - 1:
                await asyncio.sleep(Config.SAFE_DELAY_BETWEEN_TRADES)

        return market_data


    def calculate_base_amount(self, usdc_amount: float, current_price: float, size_decimals: int) -> int:
        """
        Calculate base_amount for order from USDC amount and current price.
        Formula: base_amount = int((usdc_amount / price) * 10^size_decimals)
        """
        if current_price <= 0:
            raise ValueError(f"Invalid price: {current_price}")

        size_in_base_token = usdc_amount / current_price
        base_amount = int(size_in_base_token * (10 ** size_decimals))

        return base_amount

    async def get_next_order_index(self, account_num: int) -> int:
        """Get unique order index for specified account"""
        async with self._order_index_lock:
            if account_num == 1:
                index = self.next_order_index_1
                self.next_order_index_1 += 1
            else:
                index = self.next_order_index_2
                self.next_order_index_2 += 1
            return index

    async def full_restart(self):
        """Perform full restart: close everything and reinitialize"""
        logger.info("🔄 Starting full bot restart...")

        # Close all open positions first
        if self.active_positions:
            logger.info(f"Closing {len(self.active_positions)} open positions before restart...")
            close_tasks = []
            for position_id, position in list(self.active_positions.items()):
                if not position.is_closing:
                    close_tasks.append(self._close_position(position_id))
            if close_tasks:
                await asyncio.gather(*close_tasks, return_exceptions=True)

        # Cleanup old connections
        logger.info("Cleaning up old connections...")
        await self.cleanup()

        # Wait a bit for cleanup to complete
        await asyncio.sleep(2)

        # Clear state
        self.active_positions.clear()
        self.positions_by_token.clear()
        self.market_data_cache.clear()
        self.consecutive_failures = 0
        self.account_manager = None
        self.api_client = None
        self.order_api = None

        # Reinitialize everything
        logger.info("Reinitializing Lighter clients...")
        await self.initialize()

        logger.info("✅ Full restart completed successfully")

    async def start(self):
        """Start hedged trading bot"""
        self.running = True
        logger.info("🚀 Hedged futures trading bot started")
        logger.info(f"Strategy: Dual account long/short pairs")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Leverage: {Config.DEFAULT_LEVERAGE}x")
        logger.info(f"Margin per position: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")
        logger.info(f"Position size: ${Config.MIN_TRADE_AMOUNT * Config.DEFAULT_LEVERAGE} - ${Config.MAX_TRADE_AMOUNT * Config.DEFAULT_LEVERAGE}")
        logger.info(f"Hold time: {Config.POSITION_HOLD_TIME_MIN/3600:.1f}h - {Config.POSITION_HOLD_TIME_MAX/3600:.1f}h")
        logger.info(f"Low OI filter: {'Enabled' if Config.ENABLE_LOW_OI_FILTER else 'Disabled'}")

        await self._trading_loop()

    async def stop(self):
        """Stop trading bot and close all positions"""
        logger.info("🛑 === STARTING SHUTDOWN SEQUENCE ===")
        self.running = False

        # Close all open positions on shutdown
        if self.active_positions:
            logger.info(f"🛑 Shutdown: Found {len(self.active_positions)} open positions")
            logger.info(f"Positions: {list(self.active_positions.keys())}")

            close_tasks = []
            for position_id, position in list(self.active_positions.items()):
                logger.info(f"Checking position {position_id}: is_closing={position.is_closing}")
                if not position.is_closing:
                    logger.info(f"✓ Adding position {position_id} to close queue")
                    close_tasks.append(self._close_position(position_id))
                else:
                    logger.info(f"⚠️ Skipping position {position_id} - already closing")

            if close_tasks:
                logger.info(f"⏳ Created {len(close_tasks)} close tasks. Starting parallel close (timeout: 120s)...")
                import time
                start_time = time.time()

                try:
                    # Give enough time for worker processes to complete (60s each + buffer)
                    results = await asyncio.wait_for(
                        asyncio.gather(*close_tasks, return_exceptions=True),
                        timeout=120
                    )

                    elapsed = time.time() - start_time
                    logger.info(f"⏱️ Close tasks completed in {elapsed:.2f}s")

                    # Log any errors
                    success_count = 0
                    error_count = 0
                    for i, result in enumerate(results):
                        if isinstance(result, Exception):
                            logger.error(f"❌ Error closing position #{i}: {result}")
                            error_count += 1
                        else:
                            success_count += 1

                    logger.info(f"✅ Close results: {success_count} successful, {error_count} errors")
                    logger.info(f"Remaining active positions: {len(self.active_positions)}")

                except asyncio.TimeoutError:
                    elapsed = time.time() - start_time
                    logger.error(f"❌ Timeout waiting for positions to close after {elapsed:.2f}s")
                    logger.warning(f"⚠️ {len([p for p in self.active_positions.values() if not p.is_closing])} positions may still be open")
                    logger.warning(f"Still active: {list(self.active_positions.keys())}")
            else:
                logger.info("No positions need closing (all already marked as closing)")
        else:
            logger.info("No open positions to close")

        logger.info("🛑 === SHUTDOWN COMPLETE ===")
        logger.info(f"Final active positions count: {len(self.active_positions)}")
        logger.info(self.stats.get_stats_string())

    async def _trading_loop(self):
        """Main trading loop with low OI token selection and hedged pairs"""
        while self.running:
            try:
                # Check if we need to pause and perform full restart due to consecutive failures
                if self.consecutive_failures >= Config.MAX_CONSECUTIVE_FAILURES:
                    logger.error(f"🛑 Reached {self.consecutive_failures} consecutive failures!")
                    logger.info(f"⏸️  Pausing for {Config.PAUSE_DURATION_SECONDS} seconds before full restart...")

                    # Pause
                    await asyncio.sleep(Config.PAUSE_DURATION_SECONDS)

                    # Perform full restart (close positions, cleanup, reinitialize)
                    try:
                        await self.full_restart()
                    except Exception as restart_error:
                        logger.error(f"Failed to restart: {restart_error}")
                        # If restart fails, wait a bit and try to continue anyway
                        await asyncio.sleep(10)
                        self.consecutive_failures = 0

                    continue

                # Use tokens from config (no OI filtering)
                # ⚠️ CRITICAL: Filter out tokens that already have open positions
                # Allow multiple pairs on DIFFERENT tokens, but only ONE pair per token
                available_tokens = [t for t in Config.TRADING_TOKENS if t not in self.positions_by_token]

                if not available_tokens:
                    logger.info(f"⏸️  All tokens already have open positions ({len(self.active_positions)} positions). Waiting...")
                    await asyncio.sleep(30)  # Check again in 30 seconds
                    continue

                # Select random token from filtered list
                token = random.choice(available_tokens)

                # Open hedged position pair (long + short on different accounts)
                await self._open_hedged_pair(token)

                # Wait before next trade pair
                await asyncio.sleep(Config.DELAY_BETWEEN_TRADES)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(5)

    async def _open_hedged_pair(self, token: str):
        """
        Open a hedged pair of positions: long on one account, short on the other.
        Randomizes which account gets which side, timing, and amounts.
        """
        # Get market data with current price
        market_data = await self.get_market_data(token)
        if not market_data:
            logger.error(f"Cannot get market data for {token}")
            return

        # Generate base margin (not position size!)
        # MIN_TRADE_AMOUNT and MAX_TRADE_AMOUNT now represent MARGIN
        base_margin = round(random.uniform(
            Config.MIN_TRADE_AMOUNT,
            Config.MAX_TRADE_AMOUNT
        ), 2)

        # Apply variance to create slightly different margins for each position
        variance = random.uniform(
            -Config.TRADE_AMOUNT_VARIANCE_PERCENT / 100,
            Config.TRADE_AMOUNT_VARIANCE_PERCENT / 100
        )
        margin_1 = round(base_margin * (1 + variance), 2)
        margin_2 = round(base_margin * (1 - variance), 2)

        # Calculate position sizes: Position Size = Margin × Leverage
        position_size_1 = round(margin_1 * Config.DEFAULT_LEVERAGE, 2)
        position_size_2 = round(margin_2 * Config.DEFAULT_LEVERAGE, 2)

        # Randomize which account opens long vs short
        if random.choice([True, False]):
            # Account 1: Long, Account 2: Short
            position_1_is_long = True
            position_2_is_long = False
        else:
            # Account 1: Short, Account 2: Long
            position_1_is_long = False
            position_2_is_long = True

        logger.info(f"🎯 Opening hedged pair for {token} (OI: ${market_data.open_interest:,.0f}, Price: ${market_data.last_trade_price:.2f})")
        logger.info(f"   Account 1: {'LONG' if position_1_is_long else 'SHORT'} - Margin: ${margin_1}, Position: ${position_size_1}")
        logger.info(f"   Account 2: {'LONG' if position_2_is_long else 'SHORT'} - Margin: ${margin_2}, Position: ${position_size_2}")

        # Open first position (using position size, not margin)
        position_id_1 = await self._open_single_position(
            token=token,
            is_long=position_1_is_long,
            amount_usdc=position_size_1,
            account_num=1,
            market_data=market_data
        )

        if not position_id_1:
            return  # Failed to open first position

        # Random delay between the two positions
        delay = random.uniform(
            Config.TRADE_TIMING_DELAY_MIN,
            Config.TRADE_TIMING_DELAY_MAX
        )
        await asyncio.sleep(delay)

        # Open second position (using position size, not margin)
        position_id_2 = await self._open_single_position(
            token=token,
            is_long=position_2_is_long,
            amount_usdc=position_size_2,
            account_num=2,
            market_data=market_data
        )

        if not position_id_2:
            logger.warning(f"Failed to open second position of hedged pair")
            return

        # Schedule closing for both positions (same hold time for the pair)
        hold_time = random.uniform(
            Config.POSITION_HOLD_TIME_MIN,
            Config.POSITION_HOLD_TIME_MAX
        )

        # Link the paired positions
        if position_id_1 in self.active_positions and position_id_2 in self.active_positions:
            self.active_positions[position_id_1].paired_position_id = position_id_2
            self.active_positions[position_id_2].paired_position_id = position_id_1
            logger.info(f"✅ Hedged pair opened: {position_id_1} <-> {position_id_2}")

            # Send Telegram notification with hold time
            if self.telegram:
                await self.telegram.notify_hedged_pair_opened(
                    token=token,
                    position_1_id=position_id_1,
                    position_1_type="long" if position_1_is_long else "short",
                    position_1_margin=margin_1,
                    position_1_size=position_size_1,
                    position_1_account=1,
                    position_2_id=position_id_2,
                    position_2_type="long" if position_2_is_long else "short",
                    position_2_margin=margin_2,
                    position_2_size=position_size_2,
                    position_2_account=2,
                    entry_price=market_data.last_trade_price,
                    open_interest=market_data.open_interest,
                    hold_time_seconds=hold_time,
                    leverage=Config.DEFAULT_LEVERAGE
                )

        asyncio.create_task(self._schedule_close_position(position_id_1, hold_time))
        asyncio.create_task(self._schedule_close_position(position_id_2, hold_time))

    async def _open_single_position(
        self,
        token: str,
        is_long: bool,
        amount_usdc: float,
        account_num: int,
        market_data: MarketData
    ) -> Optional[str]:
        """
        Open a single position on specified account via isolated worker process.
        Returns position_id if successful, None otherwise.
        """
        market_index = market_data.market_id
        position_type = "long" if is_long else "short"
        position_id = str(uuid.uuid4())[:8]

        # Calculate base_amount using correct formula
        try:
            base_amount = self.calculate_base_amount(
                usdc_amount=amount_usdc,
                current_price=market_data.last_trade_price,
                size_decimals=market_data.size_decimals
            )
        except Exception as e:
            logger.error(f"Failed to calculate base_amount: {e}")
            return None

        # Market order prices
        if is_long:
            price = 999999999  # Buy at any price
        else:
            price = 1  # Sell at any price

        # Get order index for tracking
        order_index = await self.get_next_order_index(account_num)

        # Open position via isolated worker process
        try:
            result = await self.account_manager.open_position(
                account_num=account_num,
                token=token,
                market_index=market_index,
                base_amount=base_amount,
                is_long=is_long,
                price=price,
                order_index=order_index
            )

            if not result or not result.get('success'):
                logger.error(f"Failed to open position on Account {account_num}: {result}")
                self.consecutive_failures += 1
                return None

            # Success - log and create position
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=market_data.last_trade_price,
                is_success=True,
                order_id=f"Acc{account_num}_{order_index}",
                tx_hash=result.get('result')
            )
            open_tx_id = await self.db.log_transaction(tx)

            # Create position object
            position = Position(
                position_id=position_id,
                token=token,
                position_type=position_type,
                is_long=is_long,
                base_amount=base_amount,
                amount_usdc=amount_usdc,
                open_order_index=order_index,
                open_tx_id=open_tx_id,
                account_num=account_num,
                entry_price=market_data.last_trade_price
            )

            # Store position
            self.active_positions[position_id] = position

            # Update positions by token
            if token not in self.positions_by_token:
                self.positions_by_token[token] = []
            self.positions_by_token[token].append(position_id)

            logger.info(f"✅ Opened {position_type.upper()} {token} on Account {account_num} (ID: {position_id}, Price: ${market_data.last_trade_price:.2f})")
            self.stats.add_position(True, amount_usdc, is_long)

            # Reset consecutive failures on success
            self.consecutive_failures = 0

            return position_id

        except Exception as e:
            logger.error(f"Failed to open position on Account {account_num} for {token}: {e}")
            self.consecutive_failures += 1

            # Log failed transaction
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=market_data.last_trade_price,
                is_success=False,
                error=str(e)
            )
            await self.db.log_transaction(tx)

            return None

    async def _schedule_close_position(self, position_id: str, hold_time: float):
        """Schedule closing a specific position after hold time"""
        await asyncio.sleep(hold_time)
        await self._close_position(position_id)

    async def _close_position(self, position_id: str):
        """Close a specific position by ID via isolated worker process"""
        logger.info(f"🔄 _close_position() called for {position_id}")

        position = self.active_positions.get(position_id)
        if not position:
            logger.warning(f"⚠️ Position {position_id} not found in active_positions")
            return

        if position.is_closing:
            logger.warning(f"⚠️ Position {position_id} already marked as closing")
            return

        # Mark as closing to prevent double closing
        logger.info(f"✓ Marking position {position_id} as closing")
        position.is_closing = True

        # Get market index
        market_index = Config.MARKET_INDICES.get(position.token)
        if market_index is None:
            logger.error(f"❌ No market index for token {position.token}")
            return

        # For closing: reverse the side's price
        if position.is_long:
            price = 1  # Sell at any price
        else:
            price = 999999999  # Buy at any price

        logger.info(f"📉 Closing {position.position_type.upper()} {position.token} on Account {position.account_num} "
                    f"(ID: {position_id}, market_index={market_index}, price={price})")

        # Get current market data for exit price
        market_data = await self.get_market_data(position.token)
        exit_price = market_data.last_trade_price if market_data else None

        # Get PnL BEFORE closing position (while position still exists in API)
        pnl = None
        try:
            account_index = Config.ACCOUNT_1_INDEX if position.account_num == 1 else Config.ACCOUNT_2_INDEX
            response = await self.account_api.account(by="index", value=str(account_index))

            # Handle different response formats
            account_data = None
            if hasattr(response, 'data') and response.data:
                account_data = response.data[0]
            elif hasattr(response, 'sub_accounts') and response.sub_accounts:
                account_data = response.sub_accounts[0]
            elif hasattr(response, '__getitem__'):
                account_data = response[0]
            else:
                account_data = response

            # Find this specific position in the account data
            if account_data and hasattr(account_data, 'positions'):
                for pos_data in account_data.positions:
                    if hasattr(pos_data, 'market_id') and pos_data.market_id == market_index:
                        # Found the position - get its PnL
                        unrealized = float(pos_data.unrealized_pnl) if hasattr(pos_data, 'unrealized_pnl') and pos_data.unrealized_pnl else 0.0
                        realized = float(pos_data.realized_pnl) if hasattr(pos_data, 'realized_pnl') and pos_data.realized_pnl else 0.0
                        pnl = unrealized + realized
                        logger.info(f"Position PnL before close: unrealized=${unrealized:.2f}, realized=${realized:.2f}, total=${pnl:.2f}")
                        break
        except Exception as e:
            logger.warning(f"Could not fetch PnL before closing position: {e}")

        # Get order index for tracking
        order_index = await self.get_next_order_index(position.account_num)
        logger.info(f"✓ Got order index: {order_index}")

        # Close position via isolated worker process
        try:
            logger.info(f"⏳ Calling account_manager.close_position() for {position_id}...")
            logger.info(f"   Account: {position.account_num}, Token: {position.token}, Market: {market_index}")
            logger.info(f"   Base amount: {position.base_amount}, Is long: {position.is_long}, Order index: {order_index}")

            import time
            call_start = time.time()

            success = await self.account_manager.close_position(
                account_num=position.account_num,
                token=position.token,
                market_index=market_index,
                base_amount=position.base_amount,
                is_long=position.is_long,
                price=price,
                order_index=order_index
            )

            call_duration = time.time() - call_start
            logger.info(f"⏱️ account_manager.close_position() returned after {call_duration:.2f}s: success={success}")

            if not success:
                logger.error(f"❌ account_manager.close_position() returned False for {position_id}")
                position.is_closing = False
                return

            logger.info(f"✓ Position {position_id} closed successfully via worker")

            # Success - log and cleanup
            # Log transaction
            tx = Transaction(
                tx_type="close",
                position_type=position.position_type,
                token=position.token,
                amount_usdc=position.amount_usdc,
                base_amount=position.base_amount,
                price=position.entry_price,
                is_success=True,
                dependency=position.open_tx_id,
                order_id=f"Acc{position.account_num}_{order_index}",
                tx_hash=None
            )
            await self.db.log_transaction(tx)

            # Remove from active positions
            del self.active_positions[position_id]

            # Remove from positions by token
            if position.token in self.positions_by_token:
                self.positions_by_token[position.token].remove(position_id)
                if not self.positions_by_token[position.token]:
                    del self.positions_by_token[position.token]

            # Count remaining positions for this token
            remaining = len(self.positions_by_token.get(position.token, []))

            # Calculate hold time
            hold_time_hours = (time.time() - position.open_time) / 3600

            logger.info(f"✅ Closed {position.position_type} {position.token} on Account {position.account_num} "
                        f"(ID: {position_id}, Remaining: {remaining}, PnL: ${pnl:.2f if pnl else 'N/A'})")
            logger.info(self.stats.get_stats_string())

            # Send Telegram notification for single position close
            if self.telegram:
                await self.telegram.notify_position_closed(
                    position_id=position_id,
                    token=position.token,
                    position_type=position.position_type,
                    account_num=position.account_num,
                    amount_usdc=position.amount_usdc,
                    entry_price=position.entry_price,
                    exit_price=exit_price,
                    hold_time_hours=hold_time_hours,
                    pnl=pnl
                )

            # Check if this is part of a hedged pair and send pair notification
            if position.paired_position_id:
                paired_pos = self.active_positions.get(position.paired_position_id)
                # If paired position was already closed, send hedged pair summary
                if not paired_pos:
                    await self._send_hedged_pair_summary(position, position_id)

            # Send balance notification after closing position
            await self.send_balance_notification()

        except Exception as e:
            logger.error(f"Failed to close position {position_id}: {e}")
            position.is_closing = False  # Reset flag on error

            # Log failed transaction
            tx = Transaction(
                tx_type="close",
                position_type=position.position_type,
                token=position.token,
                amount_usdc=position.amount_usdc,
                base_amount=position.base_amount,
                price=position.entry_price,
                is_success=False,
                dependency=position.open_tx_id,
                error=str(e)
            )
            await self.db.log_transaction(tx)

    async def _send_hedged_pair_summary(self, position: Position, position_id: str):
        """
        Send hedged pair summary when both positions are closed.
        This is called when the second position of a pair closes.
        """
        if not self.telegram or not position.paired_position_id:
            return

        try:
            # Get market ID for this token
            market_id = Config.MARKET_INDICES.get(position.token)
            if not market_id:
                return

            # Try to get PnL from position monitor (historical data might be available)
            pair_pnl = None
            if self.position_monitor:
                pair_pnl = self.position_monitor.get_hedged_pair_pnl(market_id)

            # If we don't have monitor data, we can't calculate accurate pair PnL
            # Just notify that pair is fully closed
            if not pair_pnl:
                logger.info(f"Hedged pair for {position.token} fully closed (IDs: {position_id} <-> {position.paired_position_id})")
                return

            pos1_pnl, pos2_pnl, total_pnl = pair_pnl
            hold_time_hours = (time.time() - position.open_time) / 3600

            await self.telegram.notify_hedged_pair_closed(
                token=position.token,
                position_1_id=position_id,
                position_1_pnl=pos1_pnl,
                position_2_id=position.paired_position_id,
                position_2_pnl=pos2_pnl,
                total_pnl=total_pnl,
                entry_price=position.entry_price,
                hold_time_hours=hold_time_hours
            )

        except Exception as e:
            logger.error(f"Failed to send hedged pair summary: {e}")