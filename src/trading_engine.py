import asyncio
import random
import time
import uuid
from typing import Set, Dict, Optional, Tuple, List
import lighter
from dataclasses import dataclass

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


@dataclass
class TPSLOrders:
    """Track TP/SL orders for a position"""
    tp_order_index: Optional[int] = None
    sl_order_index: Optional[int] = None
    tp_price: Optional[int] = None
    sl_price: Optional[int] = None
    tp_set: bool = False
    sl_set: bool = False


class Position:
    """Represents a single position with TP/SL support"""

    def __init__(self, position_id: str, token: str, position_type: str,
                 is_long: bool, base_amount: int, amount_usdc: float,
                 open_order_index: int, open_tx_id: int, entry_price: int):
        self.position_id = position_id
        self.token = token
        self.position_type = position_type
        self.is_long = is_long
        self.base_amount = base_amount
        self.amount_usdc = amount_usdc
        self.open_order_index = open_order_index
        self.open_tx_id = open_tx_id
        self.entry_price = entry_price  # Store entry price for TP/SL calculation
        self.open_time = time.time()
        self.is_closing = False
        self.tp_sl_orders = TPSLOrders()  # Track TP/SL orders


class TradingEngine:
    """
    Futures trading engine with TP/SL support for Lighter Protocol.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None

        # Trading state
        self.active_positions: Dict[str, Position] = {}
        self.positions_by_token: Dict[str, List[str]] = {}
        self.running = False
        self.stats = Stats()

        # Track order indices
        self.next_order_index = 1000
        self._order_index_lock = asyncio.Lock()

        # Track nonces
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

        # Per-token cooldown tracking
        self.token_last_close_time: Dict[str, float] = {}

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

            logger.info(f"Trading engine initialized with TP/SL support")
            logger.info(f"TP: {Config.TP_PERCENT * 100:.3f}%, SL: {Config.SL_PERCENT * 100:.3f}%")
            logger.info(f"Per-token cooldown: {Config.DELAY_BETWEEN_TRADES}s")

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
                imf = int(10000 / Config.DEFAULT_LEVERAGE)

                tx_info, error = self.client.sign_update_leverage(
                    market_index=market_index,
                    fraction=imf,
                    margin_mode=self.client.CROSS_MARGIN_MODE,
                    nonce=await self.get_next_nonce()
                )

                if error:
                    logger.error(f"Failed to sign leverage update for {token}: {error}")
                    continue

                result = await self.transaction_api.send_tx(
                    tx_type=self.client.TX_TYPE_UPDATE_LEVERAGE,
                    tx_info=tx_info
                )

                logger.info(f"Set leverage {Config.DEFAULT_LEVERAGE}x for {token}")
                await asyncio.sleep(1)

            except Exception as e:
                logger.error(f"Failed to set leverage for {token}: {e}")

    async def cleanup(self):
        """Cleanup resources"""
        if self.client:
            await self.client.close()
        if self.api_client:
            await self.api_client.close()

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

    async def _set_tp_sl_orders(self, position: Position, market_index: int):
        """Set TP and SL orders for a position"""
        try:
            # Calculate TP/SL prices based on entry price and configured percentages
            if position.is_long:
                tp_price = int(position.entry_price * (1 + Config.TP_PERCENT))
                sl_price = int(position.entry_price * (1 - Config.SL_PERCENT))
            else:
                tp_price = int(position.entry_price * (1 - Config.TP_PERCENT))
                sl_price = int(position.entry_price * (1 + Config.SL_PERCENT))

            position.tp_sl_orders.tp_price = tp_price
            position.tp_sl_orders.sl_price = sl_price

            # Create TP order
            tp_order_index = await self.get_next_order_index()
            tp_tx_info, tp_error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=tp_order_index,
                base_amount=position.base_amount,
                price=tp_price,
                is_ask=position.is_long,  # Sell for long TP, buy for short TP
                order_type=self.client.ORDER_TYPE_TAKE_PROFIT_LIMIT,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
                reduce_only=True,
                trigger_price=tp_price,
                order_expiry=int(time.time() + 86400),  # 24 hour expiry
                nonce=await self.get_next_nonce()
            )

            if not tp_error:
                tp_result = await self.transaction_api.send_tx(
                    tx_type=self.client.TX_TYPE_CREATE_ORDER,
                    tx_info=tp_tx_info
                )
                position.tp_sl_orders.tp_order_index = tp_order_index
                position.tp_sl_orders.tp_set = True
                logger.info(f"✅ Set TP for {position.token} at {tp_price} (entry: {position.entry_price})")

            # Small delay between orders to avoid rate limits
            await asyncio.sleep(1)

            # Create SL order
            sl_order_index = await self.get_next_order_index()
            sl_tx_info, sl_error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=sl_order_index,
                base_amount=position.base_amount,
                price=sl_price,
                is_ask=position.is_long,  # Sell for long SL, buy for short SL
                order_type=self.client.ORDER_TYPE_STOP_LOSS_LIMIT,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
                reduce_only=True,
                trigger_price=sl_price,
                order_expiry=int(time.time() + 86400),
                nonce=await self.get_next_nonce()
            )

            if not sl_error:
                sl_result = await self.transaction_api.send_tx(
                    tx_type=self.client.TX_TYPE_CREATE_ORDER,
                    tx_info=sl_tx_info
                )
                position.tp_sl_orders.sl_order_index = sl_order_index
                position.tp_sl_orders.sl_set = True
                logger.info(f"✅ Set SL for {position.token} at {sl_price} (entry: {position.entry_price})")

        except Exception as e:
            logger.error(f"Failed to set TP/SL for position {position.position_id}: {e}")

    async def _cancel_tp_sl_orders(self, position: Position, market_index: int):
        """Cancel TP/SL orders before closing position"""
        try:
            # Cancel TP order if exists
            if position.tp_sl_orders.tp_set and position.tp_sl_orders.tp_order_index:
                tp_cancel_info, tp_error = self.client.sign_cancel_order(
                    market_index=market_index,
                    order_index=position.tp_sl_orders.tp_order_index,
                    nonce=await self.get_next_nonce()
                )
                if not tp_error:
                    await self.transaction_api.send_tx(
                        tx_type=self.client.TX_TYPE_CANCEL_ORDER,
                        tx_info=tp_cancel_info
                    )
                    logger.info(f"Cancelled TP order for {position.token}")

            # Small delay
            await asyncio.sleep(0.5)

            # Cancel SL order if exists
            if position.tp_sl_orders.sl_set and position.tp_sl_orders.sl_order_index:
                sl_cancel_info, sl_error = self.client.sign_cancel_order(
                    market_index=market_index,
                    order_index=position.tp_sl_orders.sl_order_index,
                    nonce=await self.get_next_nonce()
                )
                if not sl_error:
                    await self.transaction_api.send_tx(
                        tx_type=self.client.TX_TYPE_CANCEL_ORDER,
                        tx_info=sl_cancel_info
                    )
                    logger.info(f"Cancelled SL order for {position.token}")

        except Exception as e:
            logger.error(f"Failed to cancel TP/SL orders: {e}")

    async def _can_open_position_for_token(self, token: str) -> bool:
        """Check if cooldown period has passed for token"""
        last_close = self.token_last_close_time.get(token, 0)
        time_since_close = time.time() - last_close
        return time_since_close >= Config.DELAY_BETWEEN_TRADES

    async def start(self):
        """Start trading bot"""
        self.running = True
        logger.info("🚀 Futures trading bot started with TP/SL")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Position size: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")

        # Start position monitor for time-based closing
        monitor_task = asyncio.create_task(self._position_monitor())

        try:
            await self._trading_loop()
        finally:
            monitor_task.cancel()

    async def _position_monitor(self):
        """Monitor positions for time-based closing"""
        while self.running:
            try:
                current_time = time.time()

                for position_id, position in list(self.active_positions.items()):
                    if position.is_closing:
                        continue

                    # Check if exceeded max hold time
                    if current_time - position.open_time >= Config.MAX_HOLD_SECONDS:
                        logger.info(f"⏰ Max hold time reached for {position.token} position {position_id}")
                        asyncio.create_task(self._close_position(position_id))

                await asyncio.sleep(5)  # Check every 5 seconds

            except Exception as e:
                logger.error(f"Position monitor error: {e}")

    async def stop(self):
        """Stop trading bot"""
        self.running = False

        # Close all open positions
        if self.active_positions:
            logger.info(f"Closing {len(self.active_positions)} open positions...")
            for position_id in list(self.active_positions.keys()):
                await self._close_position(position_id)
                await asyncio.sleep(2)  # Delay between closes

        logger.info("Trading bot stopped")
        logger.info(self.stats.get_stats_string())

    async def _trading_loop(self):
        """Main trading loop with per-token cooldowns"""
        while self.running:
            try:
                # Find tokens available for trading (not in cooldown)
                available_tokens = []
                for token in Config.TRADING_TOKENS:
                    if await self._can_open_position_for_token(token):
                        # Check position limit
                        token_positions = len(self.positions_by_token.get(token, []))
                        if token_positions < Config.MAX_POSITIONS_PER_TOKEN:
                            available_tokens.append(token)

                if available_tokens:
                    token = random.choice(available_tokens)
                    await self._open_position(token)

                    # Wait minimum time between any trades
                    await asyncio.sleep(Config.SAFE_DELAY_BETWEEN_TRADES)
                else:
                    # No tokens available, wait
                    await asyncio.sleep(1)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(5)

    async def _open_position(self, token: str):
        """Open a position and set TP/SL"""
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            return

        position_id = str(uuid.uuid4())[:8]
        is_long = random.choice([True, False])
        position_type = "long" if is_long else "short"
        amount_usdc = round(random.uniform(Config.MIN_TRADE_AMOUNT, Config.MAX_TRADE_AMOUNT), 2)
        base_amount = int(amount_usdc)

        # Use a reasonable entry price for calculation (you might want to fetch current price)
        # For now, using a placeholder
        entry_price = 100000  # This should be fetched from market data

        if is_long:
            price = 999999999  # Max slippage for market order
            is_ask = False
        else:
            price = 1
            is_ask = True

        try:
            logger.info(f"📈 Opening {position_type.upper()} {token}: ${amount_usdc} (ID: {position_id})")

            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,
                trigger_price=0,
                order_expiry=0,
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign open order: {error}")
                return

            result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            # Log to database
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

            # Create position
            position = Position(
                position_id=position_id,
                token=token,
                position_type=position_type,
                is_long=is_long,
                base_amount=base_amount,
                amount_usdc=amount_usdc,
                open_order_index=order_index,
                open_tx_id=open_tx_id,
                entry_price=entry_price
            )

            # Store position
            self.active_positions[position_id] = position
            if token not in self.positions_by_token:
                self.positions_by_token[token] = []
            self.positions_by_token[token].append(position_id)

            logger.info(f"✅ Opened {position_type} {token} (ID: {position_id})")
            self.stats.add_position(True, amount_usdc, is_long)

            # Set TP/SL orders after a short delay
            await asyncio.sleep(2)
            await self._set_tp_sl_orders(position, market_index)

            # Schedule random hold time close (backup if TP/SL not hit)
            hold_time = random.uniform(Config.POSITION_HOLD_TIME_MIN, Config.POSITION_HOLD_TIME_MAX)
            asyncio.create_task(self._schedule_close_position(position_id, hold_time))

        except Exception as e:
            logger.error(f"Failed to open position: {e}")

    async def _schedule_close_position(self, position_id: str, hold_time: float):
        """Schedule position close after hold time"""
        await asyncio.sleep(hold_time)
        position = self.active_positions.get(position_id)
        if position and not position.is_closing:
            await self._close_position(position_id)

    async def _close_position(self, position_id: str):
        """Close position (cancel TP/SL first)"""
        position = self.active_positions.get(position_id)
        if not position or position.is_closing:
            return

        position.is_closing = True
        market_index = Config.MARKET_INDICES.get(position.token)
        if market_index is None:
            return

        # Cancel TP/SL orders first
        await self._cancel_tp_sl_orders(position, market_index)
        await asyncio.sleep(1)

        # Close position
        if position.is_long:
            price = 1
            is_ask = True
        else:
            price = 999999999
            is_ask = False

        retry_count = 0
        max_retries = 3

        while retry_count < max_retries:
            try:
                logger.info(f"📉 Closing {position.position_type.upper()} {position.token} (ID: {position_id})")

                order_index = await self.get_next_order_index()
                nonce = await self.get_next_nonce()

                tx_info, error = self.client.sign_create_order(
                    market_index=market_index,
                    client_order_index=order_index,
                    base_amount=position.base_amount,
                    price=price,
                    is_ask=is_ask,
                    order_type=self.client.ORDER_TYPE_MARKET,
                    time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                    reduce_only=True,
                    trigger_price=0,
                    order_expiry=0,
                    nonce=nonce
                )

                if error:
                    logger.error(f"Failed to sign close order: {error}")
                    position.is_closing = False
                    return

                result = await self.transaction_api.send_tx(
                    tx_type=self.client.TX_TYPE_CREATE_ORDER,
                    tx_info=tx_info
                )

                # Success - update tracking
                self.token_last_close_time[position.token] = time.time()

                # Remove from tracking
                del self.active_positions[position_id]
                if position.token in self.positions_by_token:
                    self.positions_by_token[position.token].remove(position_id)
                    if not self.positions_by_token[position.token]:
                        del self.positions_by_token[position.token]

                logger.info(f"✅ Closed {position.token} position (ID: {position_id})")
                logger.info(self.stats.get_stats_string())
                break  # Success, exit retry loop

            except Exception as e:
                error_msg = str(e)
                if "invalid nonce" in error_msg:
                    logger.warning(f"Invalid nonce detected, resyncing... (attempt {retry_count + 1}/{max_retries})")
                    await self.resync_nonce()
                    retry_count += 1
                    await asyncio.sleep(1)
                else:
                    logger.error(f"Failed to close position: {e}")
                    position.is_closing = False
                    break

        if retry_count >= max_retries:
            logger.error(f"Failed to close position after {max_retries} retries")
            position.is_closing = False