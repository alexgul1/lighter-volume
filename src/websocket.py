#!/usr/bin/env python3
"""
Standalone WebSocket Client for Lighter Protocol
Handles authentication, re-authentication, and position monitoring
"""

import asyncio
import json
import time
import logging
from typing import Dict, Any, Optional, Callable
from dataclasses import dataclass
import websockets
import lighter
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("WebSocketClient")


@dataclass
class WebSocketConfig:
    """Configuration for WebSocket connection"""
    ws_url: str = "wss://mainnet.zklighter.elliot.ai/stream"
    api_key_private_key: str = ""  # Your API key
    account_index: int = 1
    api_key_index: int = 2
    base_url: str = "https://mainnet.zklighter.elliot.ai"

    # Token configuration
    auth_token_lifetime_seconds: int = 600  # 10 minutes default
    token_refresh_buffer_seconds: int = 30  # Refresh 30 seconds before expiry

    # Reconnection settings
    reconnect_delay_seconds: int = 5
    max_reconnect_attempts: int = -1  # -1 for infinite

    # Heartbeat settings
    heartbeat_interval_seconds: int = 30
    heartbeat_timeout_seconds: int = 10


class LighterWebSocketClient:
    """
    WebSocket client for Lighter Protocol
    Handles authentication, auto-renewal, and position tracking
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
        self.heartbeat_task = None
        self.message_handler_task = None

        # Callbacks for position events
        self.on_position_opened: Optional[Callable] = None
        self.on_position_closed: Optional[Callable] = None
        self.on_position_updated: Optional[Callable] = None

        # Track positions
        self.current_positions: Dict[int, Dict] = {}  # market_id -> position data

        # Stats
        self.connection_start_time = None
        self.messages_received = 0
        self.reconnect_count = 0

    async def initialize(self):
        """Initialize the signer client for authentication"""
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

            logger.info("Signer client initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize signer client: {e}")
            raise

    async def generate_auth_token(self):
        """Generate a new authentication token"""
        try:
            token, err = self.signer_client.create_auth_token_with_expiry(
                self.config.auth_token_lifetime_seconds
            )

            if err:
                raise Exception(f"Failed to create auth token: {err}")

            self.auth_token = token
            self.token_expiry_time = time.time() + self.config.auth_token_lifetime_seconds

            logger.info(f"Generated new auth token, expires at {datetime.fromtimestamp(self.token_expiry_time)} {token}")
            return token

        except Exception as e:
            logger.error(f"Failed to generate auth token: {e}")
            raise

    async def should_renew_token(self) -> bool:
        """Check if token needs renewal"""
        if not self.auth_token or not self.token_expiry_time:
            return True

        time_until_expiry = self.token_expiry_time - time.time()
        return time_until_expiry <= self.config.token_refresh_buffer_seconds

    async def auth_renewal_loop(self):
        """Background task to renew authentication token"""
        while self.running:
            try:
                if await self.should_renew_token():
                    logger.info("Token renewal needed")
                    await self.generate_auth_token()

                    # Re-authenticate with new token if connected
                    if self.ws and not self.ws.closed:
                        await self.authenticate()

                # Check every 10 seconds
                await asyncio.sleep(10)

            except Exception as e:
                logger.error(f"Error in auth renewal loop: {e}")
                await asyncio.sleep(10)

    async def authenticate(self):
        """Send authentication message to WebSocket"""
        if not self.ws or self.ws.closed:
            logger.error("Cannot authenticate - WebSocket not connected")
            return False

        try:
            auth_msg = {
                "type": "authenticate",
                "data": {
                    "auth_token": self.auth_token
                }
            }

            await self.ws.send(json.dumps(auth_msg))
            logger.info("Authentication message sent")
            return True

        except Exception as e:
            logger.error(f"Failed to send authentication: {e}")
            return False

    async def subscribe_to_account(self):
        """Subscribe to account updates channel"""
        if not self.ws or self.ws.closed:
            return False

        try:
            subscribe_msg = {
                "type": "subscribe",
                "channel": f"account_all/{self.config.account_index}"
            }

            await self.ws.send(json.dumps(subscribe_msg))
            logger.info(f"Subscribed to account_all/{self.config.account_index}")
            return True

        except Exception as e:
            logger.error(f"Failed to subscribe: {e}")
            return False

    async def heartbeat_loop(self):
        """Send periodic heartbeat to keep connection alive"""
        while self.running:
            try:
                if self.ws and not self.ws.closed:
                    ping_msg = {"type": "ping"}
                    await self.ws.send(json.dumps(ping_msg))
                    logger.debug("Heartbeat sent")

                await asyncio.sleep(self.config.heartbeat_interval_seconds)

            except Exception as e:
                logger.error(f"Heartbeat failed: {e}")
                # Connection might be dead, will be handled by main loop

    async def process_message(self, message: str):
        """Process incoming WebSocket message"""
        try:
            data = json.loads(message)
            self.messages_received += 1

            msg_type = data.get("type")
            channel = data.get("channel", "")

            # Handle different message types
            if msg_type == "pong":
                logger.debug("Heartbeat acknowledged")

            elif msg_type == "authenticated":
                logger.info("Authentication successful")

            elif msg_type == "subscribed":
                logger.info(f"Successfully subscribed to {data.get('channel')}")

            elif "account_all" in channel:
                await self.process_account_update(data)

            else:
                logger.debug(f"Received message type: {msg_type}")

        except json.JSONDecodeError:
            logger.error(f"Invalid JSON message: {message[:100]}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    async def process_account_update(self, data: Dict[str, Any]):
        """Process account update message containing positions"""
        try:
            account_data = data.get("data", {})

            # Extract positions
            positions = account_data.get("positions", [])

            # Track current position states
            new_positions = {}

            for pos in positions:
                market_id = pos.get("market_id")
                if market_id is None:
                    continue

                # Extract key position data
                position_info = {
                    "market_id": market_id,
                    "symbol": pos.get("symbol"),
                    "sign": pos.get("sign"),  # 1 for long, -1 for short
                    "position": pos.get("position"),  # base amount
                    "avg_entry_price": pos.get("avg_entry_price"),
                    "position_value": pos.get("position_value"),
                    "unrealized_pnl": pos.get("unrealized_pnl"),
                    "realized_pnl": pos.get("realized_pnl"),
                    "liquidation_price": pos.get("liquidation_price"),
                    "margin_mode": pos.get("margin_mode"),
                    "allocated_margin": pos.get("allocated_margin"),
                    "timestamp": time.time()
                }

                new_positions[market_id] = position_info

                # Check if this is a new position
                if market_id not in self.current_positions:
                    logger.info(f"📈 New position opened: {position_info['symbol']} "
                                f"{'LONG' if position_info['sign'] > 0 else 'SHORT'} "
                                f"Size: {position_info['position']} "
                                f"Entry: {position_info['avg_entry_price']}")

                    if self.on_position_opened:
                        await self.on_position_opened(position_info)

                # Check if position was updated
                elif self.current_positions[market_id] != position_info:
                    old_pos = self.current_positions[market_id]

                    # Log significant changes
                    if old_pos.get("position") != position_info.get("position"):
                        logger.info(f"Position size changed for {position_info['symbol']}: "
                                    f"{old_pos.get('position')} -> {position_info.get('position')}")

                    if self.on_position_updated:
                        await self.on_position_updated(position_info, old_pos)

            # Check for closed positions
            for market_id, old_position in self.current_positions.items():
                if market_id not in new_positions:
                    logger.info(f"📉 Position closed: {old_position['symbol']} "
                                f"PnL: {old_position.get('unrealized_pnl', 0)}")

                    if self.on_position_closed:
                        await self.on_position_closed(old_position)

            # Update current positions
            self.current_positions = new_positions

            # Log account summary
            if positions:
                total_unrealized_pnl = sum(p.get("unrealized_pnl", 0) for p in positions)
                logger.info(f"Account update: {len(positions)} positions, "
                            f"Total unrealized PnL: {total_unrealized_pnl}")

        except Exception as e:
            logger.error(f"Error processing account update: {e}")

    async def connect(self):
        """Main connection loop with automatic reconnection"""
        self.running = True
        reconnect_attempts = 0

        # Start background tasks
        self.auth_renewal_task = asyncio.create_task(self.auth_renewal_loop())
        self.heartbeat_task = asyncio.create_task(self.heartbeat_loop())

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

                    logger.info("WebSocket connected successfully")

                    # Authenticate
                    if await self.authenticate():
                        # Subscribe to account updates
                        await self.subscribe_to_account()

                        # Process incoming messages
                        async for message in websocket:
                            await self.process_message(message)

            except websockets.exceptions.ConnectionClosed:
                logger.warning("WebSocket connection closed")

            except Exception as e:
                logger.error(f"WebSocket error: {e}")

            finally:
                self.ws = None

                if not self.running:
                    break

                # Handle reconnection
                reconnect_attempts += 1
                self.reconnect_count += 1

                if (self.config.max_reconnect_attempts > 0 and
                        reconnect_attempts >= self.config.max_reconnect_attempts):
                    logger.error("Max reconnection attempts reached")
                    break

                logger.info(f"Reconnecting in {self.config.reconnect_delay_seconds} seconds... "
                            f"(Attempt {reconnect_attempts})")
                await asyncio.sleep(self.config.reconnect_delay_seconds)

    async def disconnect(self):
        """Disconnect and cleanup"""
        logger.info("Disconnecting WebSocket client...")
        self.running = False

        # Cancel background tasks
        if self.auth_renewal_task:
            self.auth_renewal_task.cancel()
        if self.heartbeat_task:
            self.heartbeat_task.cancel()

        # Close WebSocket
        if self.ws and not self.ws.closed:
            await self.ws.close()

        # Close signer client
        if self.signer_client:
            await self.signer_client.close()

        logger.info("WebSocket client disconnected")

    def get_stats(self) -> Dict[str, Any]:
        """Get connection statistics"""
        uptime = 0
        if self.connection_start_time:
            uptime = time.time() - self.connection_start_time

        return {
            "connected": self.ws is not None and not self.ws.closed,
            "uptime_seconds": uptime,
            "messages_received": self.messages_received,
            "reconnect_count": self.reconnect_count,
            "active_positions": len(self.current_positions),
            "positions": self.current_positions
        }

