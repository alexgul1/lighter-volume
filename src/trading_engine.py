import os
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

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


@dataclass
class PositionTPSL:
    """Take Profit and Stop Loss settings for a position"""
    take_profit_price: int
    stop_loss_price: int
    tp_order_index: Optional[int] = None
    sl_order_index: Optional[int] = None
    tp_order_id: Optional[str] = None
    sl_order_id: Optional[str] = None


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

        # Time-based close
        self.max_hold_time: float = 0


class TradingEngine:
    """
    Enhanced futures trading engine for Lighter Protocol.
    Features:
    - WebSocket position monitoring
    - Automatic TP/SL management
    - Per-token cooldown delays
    - Time-based position closing
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None
        self.ws_client = None
        self.ws_task = None

        # Trading state
        self.active_positions: Dict[str, Position] = {}  # position_id -> Position
        self.positions_by_token: Dict[str, List[str]] = {}  # token -> list of position_ids
        self.positions_by_market: Dict[int, List[str]] = {}  # market_id -> list of position_ids
        self.running = False
        self.stats = Stats()

        # Per-token cooldown tracking
        self.token_last_close_time: Dict[str, float] = {}  # token -> last close timestamp
        self.token_cooldown_seconds: float = Config.DELAY_BETWEEN_TRADES

        # Track order indices
        self.next_order_index = 1000
        self._order_index_lock = asyncio.Lock()

        # Track nonces
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

        # WebSocket authentication
        self.auth_token = None

        # TP/SL configuration (as percentage)
        self.tp_percent = float(os.getenv("TP_PERCENT", "0.001"))  # 0.1%
        self.sl_percent = float(os.getenv("SL_PERCENT", "0.001"))  # 0.1%

        # Max position hold time (seconds)
        self.max_hold_seconds = float(os.getenv("MAX_HOLD_SECONDS", "300"))  # 5 minutes

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
            self.auth_token, err = self.client.create_auth_token_with_expiry(60000)  # 10 min expiry
            if err:
                raise Exception(f"Failed to create auth token: {err}")

            # Set leverage for all markets
            await self._set_leverage_for_markets()

            # Start WebSocket connection
            await self._start_websocket()

            logger.info(f"Trading engine initialized (Account type: {Config.ACCOUNT_TYPE})")
            logger.info(f"Default leverage: {Config.DEFAULT_LEVERAGE}x")
            logger.info(f"TP/SL: {self.tp_percent * 100}%/{self.sl_percent * 100}%")
            logger.info(f"Max hold time: {self.max_hold_seconds}s")
            logger.info(f"Per-token cooldown: {self.token_cooldown_seconds}s")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def _start_websocket(self):
        """Start WebSocket connection and subscribe to account updates"""
        self.ws_task = asyncio.create_task(self._websocket_handler())

    async def _websocket_handler(self):
        """Handle WebSocket connection and messages"""
        ws_url = "wss://mainnet.zklighter.elliot.ai/stream"

        while self.running:
            try:
                async with websockets.connect(ws_url) as websocket:
                    self.ws_client = websocket
                    logger.info("WebSocket connected")

                    # Authenticate
                    auth_msg = {
                        "type": "authenticate",
                        "data": {
                            "auth_token": self.auth_token
                        }
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
                            logger.error(f"Invalid JSON in WebSocket message: {message}")
                        except Exception as e:
                            logger.error(f"Error processing WebSocket message: {e}")

            except websockets.exceptions.ConnectionClosed:
                logger.warning("WebSocket connection closed, reconnecting...")
                await asyncio.sleep(5)
            except Exception as e:
                logger.error(f"WebSocket error: {e}")
                await asyncio.sleep(5)

    async def _process_websocket_message(self, data: Dict[str, Any]):
        """Process WebSocket message for position updates"""
        if data.get("channel", "").startswith("account_all"):
            positions = data.get("data", {}).get("positions", [])

            for pos_data in positions:
                market_id = pos_data.get("market_id")
                if market_id is None:
                    continue

                # Find our positions for this market
                position_ids = self.positions_by_market.get(market_id, [])

                for position_id in position_ids:
                    position = self.active_positions.get(position_id)
                    if not position:
                        continue

                    # Update position data from WebSocket
                    position.avg_entry_price = pos_data.get("avg_entry_price")
                    position.position_value = pos_data.get("position_value")
                    position.unrealized_pnl = pos_data.get("unrealized_pnl")

                    # Set TP/SL if not already set
                    if position.avg_entry_price and not position.tp_sl:
                        await self._set_tp_sl_for_position(position)

    async def _set_tp_sl_for_position(self, position: Position):
        """Set take profit and stop loss orders for a position"""
        if not position.avg_entry_price:
            return

        try:
            # Calculate TP/SL prices
            if position.is_long:
                tp_price = int(position.avg_entry_price * (1 + self.tp_percent))
                sl_price = int(position.avg_entry_price * (1 - self.sl_percent))
            else:
                tp_price = int(position.avg_entry_price * (1 - self.tp_percent))
                sl_price = int(position.avg_entry_price * (1 + self.sl_percent))

            # Create TP/SL orders
            tp_order_index = await self.get_next_order_index()
            sl_order_index = await self.get_next_order_index()

            # Sign take profit order
            tp_is_ask = position.is_long  # Sell for long TP, Buy for short TP
            tp_tx_info, tp_error = self.client.sign_create_order(
                market_index=position.market_id,
                client_order_index=tp_order_index,
                base_amount=position.base_amount,
                price=tp_price,
                is_ask=tp_is_ask,
                order_type=self.client.ORDER_TYPE_TAKE_PROFIT_LIMIT,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
                reduce_only=True,
                trigger_price=tp_price,
                order_expiry=0,
                nonce=await self.get_next_nonce()
            )

            if tp_error:
                logger.error(f"Failed to sign TP order: {tp_error}")
                return

            # Sign stop loss order
            sl_is_ask = position.is_long  # Sell for long SL, Buy for short SL
            sl_tx_info, sl_error = self.client.sign_create_order(
                market_index=position.market_id,
                client_order_index=sl_order_index,
                base_amount=position.base_amount,
                price=sl_price,
                is_ask=sl_is_ask,
                order_type=self.client.ORDER_TYPE_STOP_LOSS_LIMIT,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_GOOD_TILL_TIME,
                reduce_only=True,
                trigger_price=sl_price,
                order_expiry=0,
                nonce=await self.get_next_nonce()
            )

            if sl_error:
                logger.error(f"Failed to sign SL order: {sl_error}")
                return

            # Send both orders
            tp_result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tp_tx_info
            )

            sl_result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=sl_tx_info
            )

            # Store TP/SL info
            position.tp_sl = PositionTPSL(
                take_profit_price=tp_price,
                stop_loss_price=sl_price,
                tp_order_index=tp_order_index,
                sl_order_index=sl_order_index,
                tp_order_id=str(tp_result) if tp_result else None,
                sl_order_id=str(sl_result) if sl_result else None
            )

            logger.info(f"✅ Set TP/SL for {position.token} position {position.position_id}: "
                        f"Entry: {position.avg_entry_price}, TP: {tp_price}, SL: {sl_price}")

        except Exception as e:
            logger.error(f"Failed to set TP/SL for position {position.position_id}: {e}")

    async def _cancel_tp_sl_orders(self, position: Position):
        """Cancel TP/SL orders for a position"""
        if not position.tp_sl:
            return

        try:
            # Cancel TP order if exists
            if position.tp_sl.tp_order_index:
                cancel_tp_info, error = self.client.sign_cancel_order(
                    market_index=position.market_id,
                    order_index=position.tp_sl.tp_order_index,
                    nonce=await self.get_next_nonce()
                )
                if not error:
                    await self.transaction_api.send_tx(
                        tx_type=self.client.TX_TYPE_CANCEL_ORDER,
                        tx_info=cancel_tp_info
                    )

            # Cancel SL order if exists
            if position.tp_sl.sl_order_index:
                cancel_sl_info, error = self.client.sign_cancel_order(
                    market_index=position.market_id,
                    order_index=position.tp_sl.sl_order_index,
                    nonce=await self.get_next_nonce()
                )
                if not error:
                    await self.transaction_api.send_tx(
                        tx_type=self.client.TX_TYPE_CANCEL_ORDER,
                        tx_info=cancel_sl_info
                    )

            logger.info(f"Cancelled TP/SL orders for position {position.position_id}")

        except Exception as e:
            logger.error(f"Failed to cancel TP/SL orders: {e}")

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

    async def _can_open_position_for_token(self, token: str) -> bool:
        """Check if we can open a position for a token based on cooldown"""
        last_close = self.token_last_close_time.get(token, 0)
        time_since_close = time.time() - last_close
        return time_since_close >= self.token_cooldown_seconds

    async def start(self):
        """Start trading bot"""
        self.running = True
        logger.info("🚀 Enhanced futures trading bot started")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Position size: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")
        logger.info(f"Hold time: {Config.POSITION_HOLD_TIME_MIN}-{Config.POSITION_HOLD_TIME_MAX}s")
        logger.info(f"Per-token cooldown: {self.token_cooldown_seconds}s")

        # Start position monitor task
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

                    # Check if position exceeded max hold time
                    if current_time - position.open_time >= position.max_hold_time:
                        positions_to_close.append(position_id)

                # Close positions that exceeded time limit
                for position_id in positions_to_close:
                    logger.info(f"⏰ Time limit reached for position {position_id}")
                    asyncio.create_task(self._close_position(position_id))

                await asyncio.sleep(1)  # Check every second

            except Exception as e:
                logger.error(f"Position monitor error: {e}")
                await asyncio.sleep(1)

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
        """Main trading loop with per-token cooldowns"""
        while self.running:
            try:
                # Find tokens that are available (not in cooldown)
                available_tokens = []
                for token in Config.TRADING_TOKENS:
                    if await self._can_open_position_for_token(token):
                        available_tokens.append(token)

                if available_tokens:
                    # Choose from available tokens
                    token = random.choice(available_tokens)
                    await self._open_position(token)
                else:
                    # All tokens in cooldown, wait a bit
                    await asyncio.sleep(1)

                # Small delay between position checks
                await asyncio.sleep(0.5)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(5)

    async def _open_position(self, token: str):
        """Open a long or short position"""
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            logger.error(f"Unknown market for token {token}")
            return

        position_id = str(uuid.uuid4())[:8]
        is_long = random.choice([True, False])
        position_type = "long" if is_long else "short"
        amount_usdc = round(random.uniform(Config.MIN_TRADE_AMOUNT, Config.MAX_TRADE_AMOUNT), 2)
        base_amount = int(amount_usdc)

        if is_long:
            price = 999999999
            is_ask = False
        else:
            price = 1
            is_ask = True

        try:
            token_positions = self.positions_by_token.get(token, [])
            logger.info(f"📈 Opening {position_type.upper()} {token}: ${amount_usdc} "
                        f"(ID: {position_id}, Active: {len(token_positions)})")

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

            # Create position with hold time
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

            # Set max hold time
            position.max_hold_time = random.uniform(
                Config.POSITION_HOLD_TIME_MIN,
                max(Config.POSITION_HOLD_TIME_MAX, self.max_hold_seconds)
            )

            # Store position
            self.active_positions[position_id] = position

            # Update positions by token
            if token not in self.positions_by_token:
                self.positions_by_token[token] = []
            self.positions_by_token[token].append(position_id)

            # Update positions by market
            if market_index not in self.positions_by_market:
                self.positions_by_market[market_index] = []
            self.positions_by_market[market_index].append(position_id)

            logger.info(f"✅ Opened {position_type} {token} (ID: {position_id})")
            self.stats.add_position(True, amount_usdc, is_long)

        except Exception as e:
            logger.error(f"Failed to open position for {token}: {e}")
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

    async def _close_position(self, position_id: str):
        """Close a specific position by ID"""
        position = self.active_positions.get(position_id)
        if not position or position.is_closing:
            return

        position.is_closing = True
        market_index = Config.MARKET_INDICES.get(position.token)
        if market_index is None:
            return

        # Cancel TP/SL orders first
        await self._cancel_tp_sl_orders(position)

        if position.is_long:
            price = 1
            is_ask = True
        else:
            price = 999999999
            is_ask = False

        try:
            logger.info(f"📉 Closing {position.position_type.upper()} {position.token} "
                        f"(ID: {position_id})")

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

            # Update token cooldown
            self.token_last_close_time[position.token] = time.time()

            # Remove from active positions
            del self.active_positions[position_id]

            # Remove from positions by token
            if position.token in self.positions_by_token:
                self.positions_by_token[position.token].remove(position_id)
                if not self.positions_by_token[position.token]:
                    del self.positions_by_token[position.token]

            # Remove from positions by market
            if position.market_id in self.positions_by_market:
                self.positions_by_market[position.market_id].remove(position_id)
                if not self.positions_by_market[position.market_id]:
                    del self.positions_by_market[position.market_id]

            remaining = len(self.positions_by_token.get(position.token, []))
            logger.info(f"✅ Closed {position.position_type} {position.token} "
                        f"(ID: {position_id}, Remaining: {remaining})")

            # Log PnL if available
            if position.unrealized_pnl is not None:
                pnl_usd = position.unrealized_pnl / 100  # Convert from cents
                logger.info(f"💰 PnL: ${pnl_usd:.2f}")

            logger.info(self.stats.get_stats_string())

        except Exception as e:
            logger.error(f"Failed to close position {position_id}: {e}")
            position.is_closing = False

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
