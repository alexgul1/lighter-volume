import asyncio
import random
import time
import uuid
from typing import Set, Dict, Optional, Tuple, List
import lighter

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


class Position:
    """Represents a single position"""

    def __init__(self, position_id: str, token: str, position_type: str,
                 is_long: bool, base_amount: int, amount_usdc: float,
                 open_order_index: int, open_tx_id: int):
        self.position_id = position_id
        self.token = token
        self.position_type = position_type
        self.is_long = is_long
        self.base_amount = base_amount
        self.amount_usdc = amount_usdc
        self.open_order_index = open_order_index
        self.open_tx_id = open_tx_id
        self.open_time = time.time()
        self.is_closing = False  # Flag to prevent double closing


class TradingEngine:
    """
    Futures trading engine for Lighter Protocol.
    Supports multiple concurrent positions per token.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None

        # Trading state - now supports multiple positions per token
        self.active_positions: Dict[str, Position] = {}  # position_id -> Position
        self.positions_by_token: Dict[str, List[str]] = {}  # token -> list of position_ids
        self.running = False
        self.stats = Stats()

        # Track order indices
        self.next_order_index = 1000
        self._order_index_lock = asyncio.Lock()

        # Track nonces
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

        # Error tracking for automatic recovery
        self.consecutive_failures = 0

    async def initialize(self):
        """Initialize Lighter client"""
        try:
            # Initialize API client
            configuration = lighter.Configuration(Config.BASE_URL)
            self.api_client = lighter.ApiClient(configuration)
            self.transaction_api = lighter.TransactionApi(self.api_client)

            # Initialize signer client
            self.client = lighter.SignerClient(
                url=Config.BASE_URL,
                private_key=Config.API_KEY_PRIVATE_KEY,
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )

            # Check client
            err = self.client.check_client()
            if err is not None:
                raise Exception(f"Client check failed: {err}")

            # Get initial nonce
            next_nonce = await self.transaction_api.next_nonce(
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )
            self.current_nonce = next_nonce.nonce

            # Set leverage for all markets
            await self._set_leverage_for_markets()

            logger.info(f"Trading engine initialized (Account type: {Config.ACCOUNT_TYPE})")
            logger.info(f"Default leverage: {Config.DEFAULT_LEVERAGE}x")
            logger.info(f"Multiple positions per token: ENABLED")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def _set_leverage_for_markets(self):
        """Set leverage for all trading markets"""
        for token in Config.TRADING_TOKENS:
            market_index = Config.MARKET_INDICES.get(token)
            if market_index is None:
                continue

            try:
                # Calculate Initial Margin Fraction (IMF) from leverage
                # IMF = 10000 / leverage (as per signer_client.py)
                imf = int(10000 / Config.DEFAULT_LEVERAGE)

                # Sign leverage update
                tx_info, error = self.client.sign_update_leverage(
                    market_index=market_index,
                    fraction=imf,
                    margin_mode=self.client.CROSS_MARGIN_MODE,  # Use cross margin
                    nonce=await self.get_next_nonce()
                )

                if error:
                    logger.error(f"Failed to sign leverage update for {token}: {error}")
                    continue

                # Send transaction
                result = await self.transaction_api.send_tx(
                    tx_type=self.client.TX_TYPE_UPDATE_LEVERAGE,
                    tx_info=tx_info
                )

                logger.info(f"Set leverage {Config.DEFAULT_LEVERAGE}x for {token}")
                await asyncio.sleep(1)  # Small delay between leverage updates

            except Exception as e:
                logger.error(f"Failed to set leverage for {token}: {e}")

    async def cleanup(self):
        """Cleanup resources"""
        if self.client:
            await self.client.close()
        if self.api_client:
            await self.api_client.close()

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
        self.consecutive_failures = 0
        self.client = None
        self.api_client = None
        self.transaction_api = None

        # Reinitialize everything
        logger.info("Reinitializing Lighter client...")
        await self.initialize()

        logger.info("✅ Full restart completed successfully")

    async def get_next_order_index(self) -> int:
        """Get unique order index"""
        async with self._order_index_lock:
            index = self.next_order_index
            self.next_order_index += 1
            return index

    async def get_next_nonce(self) -> int:
        """Get next nonce"""
        async with self._nonce_lock:
            nonce = self.current_nonce
            self.current_nonce += 1
            return nonce

    async def start(self):
        """Start trading bot"""
        self.running = True
        logger.info("🚀 Futures trading bot started")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Position size: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")
        logger.info(f"Hold time: {Config.POSITION_HOLD_TIME_MIN}-{Config.POSITION_HOLD_TIME_MAX}s")

        await self._trading_loop()

    async def stop(self):
        """Stop trading bot"""
        self.running = False

        # Close all open positions
        if self.active_positions:
            logger.info(f"Closing {len(self.active_positions)} open positions...")
            close_tasks = []
            for position_id, position in self.active_positions.items():
                if not position.is_closing:
                    close_tasks.append(self._close_position(position_id))
            if close_tasks:
                await asyncio.gather(*close_tasks, return_exceptions=True)

        logger.info("Trading bot stopped")
        logger.info(self.stats.get_stats_string())

    async def _trading_loop(self):
        """Main trading loop with automatic recovery on consecutive failures"""
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

                # We can now open positions for any token, even if it has existing positions
                token = random.choice(Config.TRADING_TOKENS)

                # Open a new position
                await self._open_position(token)

                # Wait before next trade
                await asyncio.sleep(Config.DELAY_BETWEEN_TRADES)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(5)

    async def _open_position(self, token: str):
        """Open a long or short position"""

        # Get market index
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            logger.error(f"Unknown market for token {token}")
            return

        # Generate unique position ID
        position_id = str(uuid.uuid4())[:8]

        # Random position type
        is_long = random.choice([True, False])
        position_type = "long" if is_long else "short"

        # Random amount in USDC
        amount_usdc = round(random.uniform(
            Config.MIN_TRADE_AMOUNT,
            Config.MAX_TRADE_AMOUNT
        ), 2)

        # Calculate base amount
        base_amount = int(amount_usdc)

        # Calculate price with max slippage
        if is_long:
            price = 999999999  # Buy at any price
            is_ask = False  # Buy to open long
        else:
            price = 1  # Sell at any price
            is_ask = True  # Sell to open short

        try:
            # Count active positions for this token
            token_positions = self.positions_by_token.get(token, [])
            logger.info(f"📈 Opening {position_type.upper()} {token}: ${amount_usdc} "
                        f"(ID: {position_id}, Active: {len(token_positions)})")

            # Get order index and nonce
            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            # Sign order
            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,  # False for opening position
                trigger_price=0,
                order_expiry=0,  # 0 for IOC
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign open order: {error}")

                # Increment consecutive failures counter
                self.consecutive_failures += 1
                logger.warning(f"Consecutive failures: {self.consecutive_failures}/{Config.MAX_CONSECUTIVE_FAILURES}")

                # Log failed transaction
                tx = Transaction(
                    tx_type="open",
                    position_type=position_type,
                    token=token,
                    amount_usdc=amount_usdc,
                    base_amount=base_amount,
                    price=price,
                    is_success=False,
                    error=f"Sign error: {error}"
                )
                await self.db.log_transaction(tx)
                return

            # Send transaction
            result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            # Log transaction
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=price,
                is_success=True,
                order_id=str(order_index),
                tx_hash=str(result) if result else None
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
                open_tx_id=open_tx_id
            )

            # Store position
            self.active_positions[position_id] = position

            # Update positions by token
            if token not in self.positions_by_token:
                self.positions_by_token[token] = []
            self.positions_by_token[token].append(position_id)

            logger.info(f"✅ Opened {position_type} {token} (ID: {position_id})")
            self.stats.add_position(True, amount_usdc, is_long)

            # Reset consecutive failures on success
            self.consecutive_failures = 0

            # Schedule position close
            hold_time = random.uniform(
                Config.POSITION_HOLD_TIME_MIN,
                Config.POSITION_HOLD_TIME_MAX
            )
            asyncio.create_task(self._schedule_close_position(position_id, hold_time))

        except Exception as e:
            logger.error(f"Failed to open position for {token}: {e}")

            # Increment consecutive failures counter
            self.consecutive_failures += 1
            logger.warning(f"Consecutive failures: {self.consecutive_failures}/{Config.MAX_CONSECUTIVE_FAILURES}")

            # Log failed transaction
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=price,
                is_success=False,
                error=str(e)
            )
            await self.db.log_transaction(tx)

    async def _schedule_close_position(self, position_id: str, hold_time: float):
        """Schedule closing a specific position after hold time"""
        await asyncio.sleep(hold_time)
        await self._close_position(position_id)

    async def _close_position(self, position_id: str):
        """Close a specific position by ID"""

        position = self.active_positions.get(position_id)
        if not position or position.is_closing:
            return

        # Mark as closing to prevent double closing
        position.is_closing = True

        # Get market index
        market_index = Config.MARKET_INDICES.get(position.token)
        if market_index is None:
            return

        # For closing: reverse the side
        if position.is_long:
            price = 1  # Sell at any price
            is_ask = True
        else:
            price = 999999999  # Buy at any price
            is_ask = False

        try:
            logger.info(f"📉 Closing {position.position_type.upper()} {position.token} "
                        f"(ID: {position_id})")

            # Get order index and nonce
            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            # Sign order
            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=position.base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=True,  # True for closing position
                trigger_price=0,
                order_expiry=0,  # 0 for IOC
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign close order: {error}")
                position.is_closing = False  # Reset flag on error
                return

            # Send transaction
            result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            # Log transaction
            tx = Transaction(
                tx_type="close",
                position_type=position.position_type,
                token=position.token,
                amount_usdc=position.amount_usdc,
                base_amount=position.base_amount,
                price=price,
                is_success=True,
                dependency=position.open_tx_id,
                order_id=str(order_index),
                tx_hash=str(result) if result else None
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

            logger.info(f"✅ Closed {position.position_type} {position.token} "
                        f"(ID: {position_id}, Remaining: {remaining})")
            logger.info(self.stats.get_stats_string())

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
                price=price,
                is_success=False,
                dependency=position.open_tx_id,
                error=str(e)
            )
            await self.db.log_transaction(tx)