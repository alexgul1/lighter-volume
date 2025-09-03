# src/websocket_manager.py
import asyncio
import json
import websockets
from typing import Dict, Any, Optional, Callable
from src.utils import setup_logger
from src.config import Config

logger = setup_logger(__name__, Config.LOG_LEVEL)


class WebSocketManager:
    """Manages WebSocket connection to Lighter"""

    def __init__(self, account_index: int, auth_token: str):
        self.ws_url = Config.WS_URL
        self.account_index = account_index
        self.auth_token = auth_token
        self.ws = None
        self.running = False
        self.callbacks = {}
        self.reconnect_delay = 5

    async def connect(self):
        """Connect to WebSocket"""
        try:
            self.ws = await websockets.connect(self.ws_url)
            logger.info("WebSocket connected")
            self.running = True

            await self._subscribe()
            asyncio.create_task(self._message_handler())

        except Exception as e:
            logger.error(f"WebSocket connection failed: {e}")
            await self._reconnect()

    async def disconnect(self):
        """Disconnect WebSocket"""
        self.running = False
        if self.ws:
            await self.ws.close()
            logger.info("WebSocket disconnected")

    async def _reconnect(self):
        """Reconnect WebSocket after delay"""
        if not self.running:
            return

        logger.info(f"Reconnecting WebSocket in {self.reconnect_delay}s...")
        await asyncio.sleep(self.reconnect_delay)
        await self.connect()

    async def _subscribe(self):
        """Subscribe to necessary channels"""
        channels = [
            f"account_all_positions/{self.account_index}",
            f"account_all_orders/{self.account_index}",
            f"account_all_trades/{self.account_index}"
        ]

        for channel in channels:
            await self._send_message({
                "type": "subscribe",
                "channel": channel,
                "auth": self.auth_token
            })

        logger.info(f"Subscribed to account channels")

    async def _send_message(self, message: Dict[str, Any]):
        """Send message to WebSocket"""
        if self.ws:
            await self.ws.send(json.dumps(message))

    async def send_transaction(self, tx_type: int, tx_info: str):
        """Send transaction through WebSocket"""
        await self._send_message({
            "type": "jsonapi/sendtx",
            "data": {
                "tx_type": tx_type,
                "tx_info": json.loads(tx_info) if isinstance(tx_info, str) else tx_info
            }
        })

    async def _message_handler(self):
        """Handle incoming WebSocket messages"""
        try:
            async for message in self.ws:
                data = json.loads(message)

                if "type" in data:
                    msg_type = data["type"]

                    if msg_type == "update/account_all_positions":
                        await self._handle_position_update(data)
                    elif msg_type == "update/account_all_orders":
                        await self._handle_order_update(data)
                    elif msg_type == "update/account_all_trades":
                        await self._handle_trade_update(data)

        except websockets.exceptions.ConnectionClosed:
            logger.warning("WebSocket connection closed")
            await self._reconnect()
        except Exception as e:
            logger.error(f"WebSocket message handler error: {e}")

    async def _handle_position_update(self, data: Dict[str, Any]):
        """Handle position update"""
        positions = data.get("positions", {})
        for market_id, position in positions.items():
            if "on_position_update" in self.callbacks:
                await self.callbacks["on_position_update"](market_id, position)

    async def _handle_order_update(self, data: Dict[str, Any]):
        """Handle order update"""
        orders = data.get("orders", {})
        for market_id, market_orders in orders.items():
            if "on_order_update" in self.callbacks:
                await self.callbacks["on_order_update"](market_id, market_orders)

    async def _handle_trade_update(self, data: Dict[str, Any]):
        """Handle trade update"""
        trades = data.get("trades", {})
        for market_id, market_trades in trades.items():
            if "on_trade_update" in self.callbacks:
                await self.callbacks["on_trade_update"](market_id, market_trades)

    def register_callback(self, event_type: str, callback: Callable):
        """Register callback for specific event type"""
        self.callbacks[event_type] = callback