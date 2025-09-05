import asyncio
import json
import random
import time
import uuid
from typing import Set, Dict, Optional, Tuple, List, Any
import lighter
import websockets
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import deque

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


@dataclass
class RateLimiter:
    """Rate limiter for API requests"""
    max_weight_per_minute: int = 60  # Standard account limit
    request_weight: int = 6  # Weight per sendTx

    def __init__(self):
        self.requests = deque()  # Store (timestamp, weight) tuples
        self.total_weight = 0

    def can_make_request(self, weight: int = 6) -> bool:
        """Check if we can make a request without exceeding limits"""
        self._cleanup_old_requests()
        return (self.total_weight + weight) <= self.max_weight_per_minute

    def add_request(self, weight: int = 6):
        """Record a request"""
        self.requests.append((time.time(), weight))
        self.total_weight += weight

    def _cleanup_old_requests(self):
        """Remove requests older than 60 seconds"""
        current_time = time.time()
        while self.requests and (current_time - self.requests[0][0]) > 60:
            _, weight = self.requests.popleft()
            self.total_weight -= weight

    def get_wait_time(self, weight: int = 6) -> float:
        """Get seconds to wait before we can make a request"""
        self._cleanup_old_requests()
        if self.can_make_request(weight):
            return 0

        # Find the oldest request that needs to expire
        if self.requests:
            oldest_time = self.requests[0][0]
            wait_time = 60 - (time.time() - oldest_time) + 1  # +1 second buffer
            return max(0, wait_time)
        return 0


@dataclass
class PositionTPSL:
    """Take Profit and Stop Loss settings for a position"""
    take_profit_price: int
    stop_loss_price: int
    tp_order_index: Optional[int] = None
    sl_order_index: Optional[int] = None
    tp_set: bool = False
    sl_set: bool = False


class Position:
    """Represents a single position with TP/SL support"""

    def __init__(self, position_id: str, token: str, position_type: str,
                 is_long: bool, base_amount: int, amount_usdc: float,
                 open_order_index: int, open_tx_id: int, market_id: int):
        self.position_id = position_id
        self.token = token
        self.market_id = market_id
        self.position_type = position_type
        self.is_long = is_long
        self.base_amount = base_amount
        self.amount_usdc = amount_usdc
        self.open_order_index = open_order_index
        self.open_tx_id = open_tx_id
        self.open_time = time.time()
        self.is_closing = False

        # WebSocket tracking
        self.avg_entry_price: Optional[int] = None
        self.position_value: Optional[int] = None
        self.unrealized_pnl: Optional[int] = None

        # TP/SL settings
        self.tp_sl: Optional[PositionTPSL] = None
        self.tp_sl_pending = False  # Flag to prevent multiple TP/SL attempts

        # Time-based close
        self.max_hold_time: float = 0


class TradingEngine:
    """
    Enhanced futures trading engine with proper rate limiting.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None
        self.ws_client = None
        self.ws_task = None

        # Trading state
        self.active_positions: Dict[str, Position] = {}
        self.positions_by_token: Dict[str, List[str]] = {}
        self.positions_by_market: Dict[int, List[str]] = {}
        self.running = False
        self.stats = Stats()

        # Rate limiting
        self.rate_limiter = RateLimiter()

        # Per-token cooldown tracking
        self.token_last_close_time: Dict[str, float] = {}

        # Global trade spacing for standard accounts
        if Config.IS_PREMIUM:
            self.min_seconds_between_trades = 0.5
        else:
            # Standard account: 10 trades/min max = 6 seconds minimum between trades
            self.min_seconds_between_trades = 6.5  # Add 0.5s buffer

        self.last_trade_time = 0

        # Track order indices
        self.next_order_index = 1000
        self._order_index_lock = asyncio.Lock()

        # Track nonces
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

        # WebSocket authentication
        self.auth_token = None

    async def initialize(self):
        """Initialize Lighter client and WebSocket"""
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

            # Create auth token for WebSocket
            self.auth_token, err = self.client.create_auth_token_with_expiry(
                Config.AUTH_TOKEN_EXPIRY
            )
            if err:
                raise Exception(f"Failed to create auth token: {err}")

            # Set leverage for all markets (with rate limiting)
            await self._set_leverage_for_markets()

            # Start WebSocket connection
            await self._start_websocket()

            logger.info(f"Trading engine initialized (Account type: {Config.ACCOUNT_TYPE})")
            logger.info(f"Rate limit: 60 weight/min, {10 if not Config.IS_PREMIUM else 600} trades/min max")
            logger.info(f"Min time between trades: {self.min_seconds_between_trades}s")
            logger.info(f"TP/SL: {Config.TP_PERCENT * 100}%/{Config.SL_PERCENT * 100}%")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def _wait_for_rate_limit(self, weight: int = 6) -> None:
        """Wait if necessary to respect rate limits"""
        wait_time = self.rate_limiter.get_wait_time(weight)
        if wait_time > 0:
            logger.warning(f"Rate limit reached, waiting {wait_time:.1f}s...")
            await asyncio.sleep(wait_time)

    async def _send_transaction_with_limit(self, tx_type: int, tx_info: str) -> Any:
        """Send transaction with rate limiting"""
        await self._wait_for_rate_limit(6)

        try:
            result = await self.transaction_api.send_tx(
                tx_type=tx_type,
                tx_info=tx_info
            )
            self.rate_limiter.add_request(6)
            return result
        except Exception as e:
            if "429" in str(e) or "Too Many Requests" in str(e):
                logger.error("Rate limit hit despite checking, backing off for 30s...")
                await asyncio.sleep(30)
                raise
            raise

    async def _start_websocket(self):
        """Start WebSocket connection and subscribe to account updates"""
        self.ws_task = asyncio.create_task(self._websocket_handler())

    async def _websocket_handler(self):
        """Handle WebSocket connection and messages"""
        ws_url = Config.WS_URL

        while self.running:
            try:
                async with websockets.connect(ws_url) as websocket:
                    self.ws_client = websocket
                    logger.info("WebSocket connected")

                    # Authenticate
                    auth_msg = {
                        "type": "authenticate",
                        "data": {"auth_token": self.auth_token}
                    }
                    await websocket.send(json.dumps(auth_msg))

                    # Subscribe to account updates
                    subscribe_msg = {
                        "type": "subscribe",
                        "channel": f"account_all/{Config.ACCOUNT_INDEX}"
                    }
                    await websocket.send(json.dumps(subscribe_msg))
                    logger.info(f"Subscribed to account updates")

                    # Handle messages
                    async for message in websocket:
                        try:
                            data = json.loads(message)
                            await self._process_websocket_message(data)
                        except json.JSONDecodeError:
                            logger.error(f"Invalid JSON: {message[:100]}")
                        except Exception as e:
                            logger.error(f"Error processing message: {e}")

            except websockets.exceptions.ConnectionClosed:
                logger.warning("WebSocket disconnected, reconnecting in 5s...")
                await asyncio.sleep(5)
            except Exception as e:
                logger.error(f"WebSocket error: {e}")
                await asyncio.sleep(5)

    async def _process_websocket_message(self, data: Dict[str, Any]):
        """Process WebSocket message for position updates"""
        try:
            if "account_all" in data.get("channel", ""):
                positions = data.get("data", {}).get("positions", [])

                for pos_data in positions:
                    market_id = pos_data.get("market_id")
                    avg_price = pos_data.get("avg_entry_price")

                    if market_id is None or not avg_price:
                        continue

                    # Find our positions for this market
                    position_ids = self.positions_by_market.get(market_id, [])

                    for position_id in position_ids:
                        position = self.active_positions.get(position_id)
                        if not position or position.tp_sl_pending:
                            continue

                        # Update position data
                        position.avg_entry_price = int(avg_price)
                        position.position_value = pos_data.get("position_value")
                        position.unrealized_pnl = pos_data.get("unrealized_pnl")

                        # Set TP/SL if not already set
                        if position.avg_entry_price and not position.tp_sl:
                            position.tp_sl_pending = True
                            asyncio.create_task(self._set_tp_sl_for_position(position))

        except Exception as e:
            logger.error(f"Error processing WebSocket data: {e}")

    async def _set_tp_sl_for_position(self, position: Position):
        """Set TP/SL with proper rate limiting"""
        if not position.avg_entry_price:
            return

        try:
            # Calculate TP/SL prices
            if position.is_long:
                tp_price = int(position.avg_entry_price * (1 + Config.TP_PERCENT))
                sl_price = int(position.avg_entry_price * (1 - Config.SL_PERCENT))
            else:
                tp_price = int(position.avg_entry_price * (1 - Config.TP_PERCENT))
                sl_price = int(position.avg_entry_price * (1 + Config.SL_PERCENT))

            position.tp_sl = PositionTPSL(
                take_profit_price=tp_price,
                stop_loss_price=sl_price
            )

            # Wait for rate limit before setting TP
            await self._wait_for_rate_limit(6)

            tp_order_index = await self.get_next_order_index()
            tp_tx_info, tp_error = self.client.sign_create_order(
                market_index=position.market_id,
                client_order_index=tp_order_index,
                base_amount=position.base_amount,
                price=tp_price,
                is_ask=position.is_long,  # Sell for long TP
                order_type=self.client.ORDER_TYPE_LIMIT,  # Use limit order
                time_in_force=self.client.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
                reduce_only=True,
                trigger_price=0,
                order_expiry=int(time.time() + 3600),  # 1 hour expiry
                nonce=await self.get_next_nonce()
            )

            if not tp_error:
                await self._send_transaction_with_limit(
                    self.client.TX_TYPE_CREATE_ORDER,
                    tp_tx_info
                )
                position.tp_sl.tp_order_index = tp_order_index
                position.tp_sl.tp_set = True
                logger.info(f"Set TP for {position.token} at {tp_price} (entry: {position.avg_entry_price})")

            # Wait a bit before SL to avoid rapid requests
            await asyncio.sleep(2)

            # Wait for rate limit before setting SL
            await self._wait_for_rate_limit(6)

            sl_order_index = await self.get_next_order_index()
            sl_tx_info, sl_error = self.client.sign_create_order(
                market_index=position.market_id,
                client_order_index=sl_order_index,
                base_amount=position.base_amount,
                price=sl_price,
                is_ask=position.is_long,  # Sell for long SL
                order_type=self.client.ORDER_TYPE_STOP_LOSS_LIMIT,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
                reduce_only=True,
                trigger_price=sl_price,
                order_expiry=int(time.time() + 3600),
                nonce=await self.get_next_nonce()
            )

            if not sl_error:
                await self._send_transaction_with_limit(
                    self.client.TX_TYPE_CREATE_ORDER,
                    sl_tx_info
                )
                position.tp_sl.sl_order_index = sl_order_index
                position.tp_sl.sl_set = True
                logger.info(f"Set SL for {position.token} at {sl_price}")

        except Exception as e:
            logger.error(f"Failed to set TP/SL for {position.position_id}: {e}")
            position.tp_sl_pending = False

    async def _set_leverage_for_markets(self):
        """Set leverage with rate limiting"""
        for token in Config.TRADING_TOKENS:
            market_index = Config.MARKET_INDICES.get(token)
            if market_index is None:
                continue

            try:
                await self._wait_for_rate_limit(6)

                imf = int(10000 / Config.DEFAULT_LEVERAGE)
                tx_info, error = self.client.sign_update_leverage(
                    market_index=market_index,
                    fraction=imf,
                    margin_mode=self.client.CROSS_MARGIN_MODE,
                    nonce=await self.get_next_nonce()
                )

                if not error:
                    await self._send_transaction_with_limit(
                        self.client.TX_TYPE_UPDATE_LEVERAGE,
                        tx_info
                    )
                    logger.info(f"Set leverage {Config.DEFAULT_LEVERAGE}x for {token}")
                    await asyncio.sleep(2)  # Space out leverage updates

            except Exception as e:
                logger.error(f"Failed to set leverage for {token}: {e}")

    async def cleanup(self):
        """Cleanup resources"""
        if self.ws_task:
            self.ws_task.cancel()
            try:
                await self.ws_task
            except asyncio.CancelledError:
                pass

        if self.ws_client:
            await self.ws_client.close()

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

    async def start(self):
        """Start trading bot"""
        self.running = True
        logger.info("🚀 Trading bot started with rate limiting")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Min delay between trades: {self.min_seconds_between_trades}s")

        # Start position monitor
        monitor_task = asyncio.create_task(self._position_monitor())

        try:
            await self._trading_loop()
        finally:
            monitor_task.cancel()
            try:
                await monitor_task
            except asyncio.CancelledError:
                pass

    async def _position_monitor(self):
        """Monitor positions for time-based closing"""
        while self.running:
            try:
                current_time = time.time()
                positions_to_close = []

                for position_id, position in self.active_positions.items():
                    if position.is_closing:
                        continue

                    # Check if exceeded max hold time
                    hold_duration = current_time - position.open_time
                    if hold_duration >= Config.MAX_HOLD_SECONDS:
                        positions_to_close.append(position_id)

                # Close positions one by one with delay
                for position_id in positions_to_close:
                    logger.info(f"⏰ Max hold time reached for {position_id}")
                    await self._close_position(position_id)
                    await asyncio.sleep(self.min_seconds_between_trades)

                await asyncio.sleep(5)  # Check every 5 seconds

            except Exception as e:
                logger.error(f"Position monitor error: {e}")
                await asyncio.sleep(5)

    async def stop(self):
        """Stop trading bot"""
        self.running = False

        # Close positions with proper spacing
        if self.active_positions:
            logger.info(f"Closing {len(self.active_positions)} positions...")
            for position_id in list(self.active_positions.keys()):
                position = self.active_positions.get(position_id)
                if position and not position.is_closing:
                    await self._close_position(position_id)
                    await asyncio.sleep(self.min_seconds_between_trades)

        logger.info("Trading bot stopped")
        logger.info(self.stats.get_stats_string())

    async def _trading_loop(self):
        """Main trading loop with proper rate limiting"""
        while self.running:
            try:
                # Enforce minimum time between trades
                time_since_last = time.time() - self.last_trade_time
                if time_since_last < self.min_seconds_between_trades:
                    wait_time = self.min_seconds_between_trades - time_since_last
                    await asyncio.sleep(wait_time)

                # Check rate limit before attempting trade
                if not self.rate_limiter.can_make_request(6):
                    wait_time = self.rate_limiter.get_wait_time(6)
                    logger.info(f"Rate limit approaching, waiting {wait_time:.1f}s")
                    await asyncio.sleep(wait_time)

                # Find available tokens (considering cooldown)
                available_tokens = []
                current_time = time.time()

                for token in Config.TRADING_TOKENS:
                    last_close = self.token_last_close_time.get(token, 0)
                    if current_time - last_close >= Config.DELAY_BETWEEN_TRADES:
                        # Check if we have room for more positions
                        token_positions = len(self.positions_by_token.get(token, []))
                        if token_positions < Config.MAX_POSITIONS_PER_TOKEN:
                            available_tokens.append(token)

                if available_tokens:
                    token = random.choice(available_tokens)
                    await self._open_position(token)
                    self.last_trade_time = time.time()
                else:
                    # No tokens available, wait
                    await asyncio.sleep(1)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(10)

    async def _open_position(self, token: str):
        """Open position with rate limiting"""
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            return

        position_id = str(uuid.uuid4())[:8]
        is_long = random.choice([True, False])
        position_type = "long" if is_long else "short"
        amount_usdc = round(random.uniform(Config.MIN_TRADE_AMOUNT, Config.MAX_TRADE_AMOUNT), 2)
        base_amount = int(amount_usdc)

        try:
            logger.info(f"📈 Opening {position_type} {token}: ${amount_usdc} (ID: {position_id})")

            await self._wait_for_rate_limit(6)

            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
                price=99999 if not is_long else 1,
                is_ask=not is_long,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,
                trigger_price=0,
                order_expiry=0,
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign: {error}")
                return

            result = await self._send_transaction_with_limit(
                self.client.TX_TYPE_CREATE_ORDER,
                tx_info
            )

            # Log to database
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=99999 if not is_long else 1,
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
                market_id=market_index
            )

            # Store position
            self.active_positions[position_id] = position

            if token not in self.positions_by_token:
                self.positions_by_token[token] = []
            self.positions_by_token[token].append(position_id)

            if market_index not in self.positions_by_market:
                self.positions_by_market[market_index] = []
            self.positions_by_market[market_index].append(position_id)

            logger.info(f"✅ Opened {position_type} {token}")
            self.stats.add_position(True, amount_usdc, is_long)

            # Schedule close (randomized hold time)
            hold_time = random.uniform(
                Config.POSITION_HOLD_TIME_MIN,
                Config.POSITION_HOLD_TIME_MAX
            )
            asyncio.create_task(self._schedule_close(position_id, hold_time))

        except Exception as e:
            logger.error(f"Failed to open position: {e}")

    async def _schedule_close(self, position_id: str, hold_time: float):
        """Schedule position close"""
        await asyncio.sleep(hold_time)
        await self._close_position(position_id)

    async def _close_position(self, position_id: str):
        """Close position with rate limiting"""
        position = self.active_positions.get(position_id)
        if not position or position.is_closing:
            return

        position.is_closing = True

        try:
            logger.info(f"📉 Closing {position.position_type} {position.token} (ID: {position_id})")

            await self._wait_for_rate_limit(6)

            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            tx_info, error = self.client.sign_create_order(
                market_index=position.market_id,
                client_order_index=order_index,
                base_amount=position.base_amount,
                price=1 if position.is_long else 99999,
                is_ask=position.is_long,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=True,
                trigger_price=0,
                order_expiry=0,
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign close: {error}")
                position.is_closing = False
                return

            result = await self._send_transaction_with_limit(
                self.client.TX_TYPE_CREATE_ORDER,
                tx_info
            )

            # Log to database
            tx = Transaction(
                tx_type="close",
                position_type=position.position_type,
                token=position.token,
                amount_usdc=position.amount_usdc,
                base_amount=position.base_amount,
                price=1 if position.is_long else 99999,
                is_success=True,
                dependency=position.open_tx_id,
                order_id=str(order_index),
                tx_hash=str(result) if result else None
            )
            await self.db.log_transaction(tx)

            # Update cooldown
            self.token_last_close_time[position.token] = time.time()

            # Remove position
            del self.active_positions[position_id]

            if position.token in self.positions_by_token:
                self.positions_by_token[position.token].remove(position_id)
                if not self.positions_by_token[position.token]:
                    del self.positions_by_token[position.token]

            if position.market_id in self.positions_by_market:
                self.positions_by_market[position.market_id].remove(position_id)
                if not self.positions_by_market[position.market_id]:
                    del self.positions_by_market[position.market_id]

            logger.info(f"✅ Closed {position.token} position")
            logger.info(self.stats.get_stats_string())

        except Exception as e:
            logger.error(f"Failed to close: {e}")
            position.is_closing = False