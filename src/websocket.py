#!/usr/bin/env python3
"""
WebSocket Client for Lighter Protocol - Trade Monitoring
Monitors account_all_trades channel for position management
"""

import asyncio
import json
import time
import logging
from typing import Dict, Any, Optional, Callable, List
from dataclasses import dataclass, field
from collections import defaultdict
import websockets
import lighter
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("TradeMonitor")


@dataclass
class TradeData:
    """Structured trade data for position management"""
    trade_id: int
    tx_hash: str
    trade_type: str  # 'trade', 'liquidation', 'deleverage'
    market_id: int
    symbol: str
    size: float  # Base amount
    price: float  # Execution price
    usd_amount: float
    is_buyer: bool  # True if this account was buyer
    is_maker: bool
    timestamp: int
    fee: float

    # Position context
    position_size_before: float
    position_size_after: float
    position_sign_changed: bool
    avg_entry_price: Optional[float] = None
    realized_pnl: Optional[float] = None


@dataclass
class PositionInfo:
    """Complete position information for management"""
    market_id: int
    symbol: str
    is_long: bool
    size: float  # Current position size
    entry_price: float  # Average entry price
    current_value: float
    unrealized_pnl: float = 0.0
    realized_pnl: float = 0.0
    open_time: float = field(default_factory=time.time)
    trades: List[TradeData] = field(default_factory=list)

    def update_from_trade(self, trade: TradeData):
        """Update position info based on new trade"""
        self.trades.append(trade)
        self.size = abs(trade.position_size_after)

        # Update PnL if available
        if trade.realized_pnl is not None:
            self.realized_pnl = trade.realized_pnl


@dataclass
class WebSocketConfig:
    """Configuration for WebSocket connection"""
    ws_url: str = "wss://mainnet.zklighter.elliot.ai/stream"
    api_key_private_key: str = ""
    account_index: int = 1
    api_key_index: int = 2
    base_url: str = "https://mainnet.zklighter.elliot.ai"

    # Token configuration
    auth_token_lifetime_seconds: int = 600  # 10 minutes default
    token_refresh_buffer_seconds: int = 30

    # Reconnection settings
    reconnect_delay_seconds: int = 5
    max_reconnect_attempts: int = -1  # -1 for infinite


class TradeMonitorClient:
    """
    WebSocket client that monitors trades for position management
    """

    def __init__(self, config: WebSocketConfig):
        self.config = config
        self.ws = None
        self.signer_client = None
        self.running = False

        # Authentication
        self.auth_token = None
        self.token_expiry_time = 0

        # Tasks
        self.auth_renewal_task = None
        self.message_handler_task = None

        # Position tracking
        self.active_positions: Dict[int, PositionInfo] = {}  # market_id -> PositionInfo
        self.closed_positions: List[PositionInfo] = []
        self.trade_history: List[TradeData] = []

        # Callbacks for position events (return position data)
        self.on_position_opened: Optional[Callable[[PositionInfo], Any]] = None
        self.on_position_closed: Optional[Callable[[PositionInfo], Any]] = None
        self.on_position_modified: Optional[Callable[[PositionInfo, TradeData], Any]] = None

        # Stats
        self.connection_start_time = None
        self.messages_received = 0
        self.trades_processed = 0

    async def initialize(self):
        """Initialize the signer client"""
        try:
            self.signer_client = lighter.SignerClient(
                url=self.config.base_url,
                private_key=self.config.api_key_private_key,
                account_index=self.config.account_index,
                api_key_index=self.config.api_key_index
            )

            err = self.signer_client.check_client()
            if err is not None:
                raise Exception(f"Signer client check failed: {err}")

            logger.info("Signer client initialized")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def generate_auth_token(self):
        """Generate authentication token"""
        try:
            token, err = self.signer_client.create_auth_token_with_expiry(
                self.config.auth_token_lifetime_seconds
            )

            if err:
                raise Exception(f"Token creation failed: {err}")

            self.auth_token = token
            self.token_expiry_time = time.time() + self.config.auth_token_lifetime_seconds

            logger.info(f"Auth token generated, expires at {datetime.fromtimestamp(self.token_expiry_time)}")
            return token

        except Exception as e:
            logger.error(f"Token generation failed: {e}")
            raise

    async def should_renew_token(self) -> bool:
        """Check if token needs renewal"""
        if not self.auth_token or not self.token_expiry_time:
            return True

        time_until_expiry = self.token_expiry_time - time.time()
        return time_until_expiry <= self.config.token_refresh_buffer_seconds

    async def auth_renewal_loop(self):
        """Renew authentication token periodically"""
        while self.running:
            try:
                if await self.should_renew_token():
                    logger.info("Renewing auth token...")
                    await self.generate_auth_token()

                    # Resubscribe with new token
                    if self.ws and not self.ws.closed:
                        await self.subscribe_to_trades()

                await asyncio.sleep(10)  # Check every 10 seconds

            except Exception as e:
                logger.error(f"Auth renewal error: {e}")
                await asyncio.sleep(10)

    async def subscribe_to_trades(self):
        """Subscribe to account_all_trades channel"""
        if not self.ws or self.ws.closed:
            return False

        try:
            subscribe_msg = {
                "type": "subscribe",
                "channel": f"account_all_trades/{self.config.account_index}",
                "auth": self.auth_token
            }

            await self.ws.send(json.dumps(subscribe_msg))
            logger.info(f"Subscribed to account_all_trades/{self.config.account_index}")
            return True

        except Exception as e:
            logger.error(f"Subscribe failed: {e}")
            return False

    def parse_trade(self, trade_data: Dict[str, Any]) -> TradeData:
        """Parse raw trade data into TradeData object"""
        # Determine if we were buyer/seller
        is_buyer = trade_data.get("bid_account_id") == self.config.account_index

        # Get the appropriate side data
        if is_buyer:
            fee = trade_data.get("bid_fee", 0)
            position_before = trade_data.get("bid_position_size_before", 0)
            position_after = position_before + float(trade_data.get("size", 0))
        else:
            fee = trade_data.get("ask_fee", 0)
            position_before = trade_data.get("ask_position_size_before", 0)
            position_after = position_before - float(trade_data.get("size", 0))

        return TradeData(
            trade_id=trade_data.get("trade_id"),
            tx_hash=trade_data.get("tx_hash", ""),
            trade_type=trade_data.get("type", "trade"),
            market_id=trade_data.get("market_id"),
            symbol=trade_data.get("symbol", f"Market-{trade_data.get('market_id')}"),
            size=float(trade_data.get("size", 0)),
            price=float(trade_data.get("price", 0)),
            usd_amount=float(trade_data.get("usd_amount", 0)),
            is_buyer=is_buyer,
            is_maker=trade_data.get("is_maker_ask") != is_buyer,
            timestamp=trade_data.get("timestamp", int(time.time())),
            fee=fee,
            position_size_before=position_before,
            position_size_after=position_after,
            position_sign_changed=trade_data.get("taker_position_sign_changed", False),
            avg_entry_price=trade_data.get("avg_entry_price"),
            realized_pnl=trade_data.get("realized_pnl")
        )

    async def process_trade(self, trade_data: Dict[str, Any]):
        """Process a trade and update position tracking"""
        try:
            trade = self.parse_trade(trade_data)
            self.trade_history.append(trade)
            self.trades_processed += 1

            market_id = trade.market_id

            # Determine position state after trade
            position_exists_before = abs(trade.position_size_before) > 0
            position_exists_after = abs(trade.position_size_after) > 0

            # Position OPENED (from 0 to non-zero)
            if not position_exists_before and position_exists_after:
                position = PositionInfo(
                    market_id=market_id,
                    symbol=trade.symbol,
                    is_long=trade.position_size_after > 0,
                    size=abs(trade.position_size_after),
                    entry_price=trade.price,
                    current_value=trade.usd_amount,
                    open_time=time.time()
                )
                position.trades.append(trade)

                self.active_positions[market_id] = position

                logger.info(f"📈 POSITION OPENED: {trade.symbol} "
                            f"{'LONG' if position.is_long else 'SHORT'} "
                            f"Size: {position.size} @ {position.entry_price} "
                            f"Value: ${position.current_value:.2f}")

                if self.on_position_opened:
                    await self.on_position_opened(position)

            # Position CLOSED (from non-zero to 0)
            elif position_exists_before and not position_exists_after:
                position = self.active_positions.get(market_id)
                if position:
                    position.update_from_trade(trade)

                    # Move to closed positions
                    self.closed_positions.append(position)
                    del self.active_positions[market_id]

                    logger.info(f"📉 POSITION CLOSED: {trade.symbol} "
                                f"Entry: {position.entry_price} Exit: {trade.price} "
                                f"PnL: ${position.realized_pnl:.2f}" if position.realized_pnl else "")

                    if self.on_position_closed:
                        await self.on_position_closed(position)

            # Position MODIFIED (size changed but still exists)
            elif position_exists_before and position_exists_after:
                position = self.active_positions.get(market_id)

                # Check if position flipped (long to short or vice versa)
                if trade.position_sign_changed:
                    # Close old position
                    if position and self.on_position_closed:
                        await self.on_position_closed(position)

                    # Create new position in opposite direction
                    new_position = PositionInfo(
                        market_id=market_id,
                        symbol=trade.symbol,
                        is_long=trade.position_size_after > 0,
                        size=abs(trade.position_size_after),
                        entry_price=trade.price,
                        current_value=trade.usd_amount
                    )
                    new_position.trades.append(trade)
                    self.active_positions[market_id] = new_position

                    logger.info(f"🔄 POSITION FLIPPED: {trade.symbol} to "
                                f"{'LONG' if new_position.is_long else 'SHORT'}")

                    if self.on_position_opened:
                        await self.on_position_opened(new_position)

                # Position just modified (partial close or add)
                elif position:
                    old_size = position.size
                    position.update_from_trade(trade)

                    action = "INCREASED" if position.size > old_size else "REDUCED"
                    logger.info(f"📊 POSITION {action}: {trade.symbol} "
                                f"{old_size} -> {position.size} @ {trade.price}")

                    if self.on_position_modified:
                        await self.on_position_modified(position, trade)

        except Exception as e:
            logger.error(f"Trade processing error: {e}")

    async def process_message(self, message: str):
        """Process incoming WebSocket message"""
        try:
            data = json.loads(message)
            self.messages_received += 1

            msg_type = data.get("type")
            channel = data.get("channel", "")

            # Handle subscription confirmation
            if msg_type == "subscribed":
                logger.info(f"Subscription confirmed: {channel}")

            # Process trade data - correct structure
            elif "account_all_trades" in channel or msg_type == "update/account_all_trades":
                # Trades are organized by market_index as a dictionary
                trades_by_market = data.get("trades", {})

                # Process trades for each market
                for market_index, trades_list in trades_by_market.items():
                    # trades_list is an array of trades for this market
                    if isinstance(trades_list, list):
                        for trade_data in trades_list:
                            await self.process_trade(trade_data)
                    elif isinstance(trades_list, dict):
                        # Single trade
                        await self.process_trade(trades_list)

                # Log volume stats if available
                if "total_volume" in data:
                    logger.debug(f"Volume stats - Total: {data.get('total_volume')}, "
                                 f"Daily: {data.get('daily_volume')}")

            # Handle errors
            elif msg_type == "error":
                logger.error(f"Server error: {data.get('message')}")

        except json.JSONDecodeError:
            logger.error(f"Invalid JSON: {message[:100]}")
        except Exception as e:
            logger.error(f"Message processing error: {e}")

    async def connect(self):
        """Main connection loop"""
        self.running = True
        reconnect_attempts = 0

        # Start auth renewal task
        self.auth_renewal_task = asyncio.create_task(self.auth_renewal_loop())

        while self.running:
            try:
                # Generate token before connecting
                if await self.should_renew_token():
                    await self.generate_auth_token()

                logger.info(f"Connecting to {self.config.ws_url}...")

                async with websockets.connect(self.config.ws_url) as websocket:
                    self.ws = websocket
                    self.connection_start_time = time.time()
                    reconnect_attempts = 0

                    logger.info("Connected successfully")

                    # Subscribe to trades
                    if await self.subscribe_to_trades():
                        # Process messages
                        async for message in websocket:
                            await self.process_message(message)

            except websockets.exceptions.ConnectionClosed:
                logger.warning("Connection closed")

            except Exception as e:
                logger.error(f"Connection error: {e}")

            finally:
                self.ws = None

                if not self.running:
                    break

                # Reconnection logic
                reconnect_attempts += 1

                if (self.config.max_reconnect_attempts > 0 and
                        reconnect_attempts >= self.config.max_reconnect_attempts):
                    logger.error("Max reconnection attempts reached")
                    break

                logger.info(f"Reconnecting in {self.config.reconnect_delay_seconds}s... "
                            f"(Attempt {reconnect_attempts})")
                await asyncio.sleep(self.config.reconnect_delay_seconds)

    async def disconnect(self):
        """Disconnect and cleanup"""
        logger.info("Disconnecting...")
        self.running = False

        if self.auth_renewal_task:
            self.auth_renewal_task.cancel()

        if self.ws and not self.ws.closed:
            await self.ws.close()

        if self.signer_client:
            await self.signer_client.close()

        logger.info("Disconnected")

    def get_position_info(self, market_id: int) -> Optional[PositionInfo]:
        """Get current position info for a market"""
        return self.active_positions.get(market_id)

    def get_all_positions(self) -> Dict[int, PositionInfo]:
        """Get all active positions"""
        return self.active_positions.copy()

    def get_stats(self) -> Dict[str, Any]:
        """Get client statistics"""
        return {
            "connected": self.ws is not None and not self.ws.closed,
            "messages_received": self.messages_received,
            "trades_processed": self.trades_processed,
            "active_positions": len(self.active_positions),
            "closed_positions": len(self.closed_positions),
            "positions": {
                mid: {
                    "symbol": pos.symbol,
                    "side": "LONG" if pos.is_long else "SHORT",
                    "size": pos.size,
                    "entry_price": pos.entry_price,
                    "unrealized_pnl": pos.unrealized_pnl
                }
                for mid, pos in self.active_positions.items()
            }
        }