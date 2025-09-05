#!/usr/bin/env python3
"""
Lighter Futures Trading Bot
"""

import asyncio
import sys
from src.bot import TradingBot
from src.utils import setup_logger
from src.config import Config
from src.websocket import WebSocketConfig, LighterWebSocketClient

logger = setup_logger("Main", Config.LOG_LEVEL)


async def main():
    """Main entry point"""
    bot = TradingBot()

    # Configure the client
    config = WebSocketConfig(
        api_key_private_key=Config.API_KEY_PRIVATE_KEY,
        account_index= Config.ACCOUNT_INDEX,
        api_key_index=Config.API_KEY_INDEX,
        auth_token_lifetime_seconds=600,  # 10 minutes
        token_refresh_buffer_seconds=30,  # Refresh 30 seconds before expiry
    )

    # Create client
    client = LighterWebSocketClient(config)

    async def on_position_opened(position):
        print(f"New position opened: {position}")

    async def on_position_closed(position):
        print(f"Position closed: {position}")

    async def on_position_updated(new_position, old_position):
        print(f"Position updated: {new_position}")

        # Register callbacks

    client.on_position_opened = on_position_opened
    client.on_position_closed = on_position_closed
    client.on_position_updated = on_position_updated

    try:
        await bot.run()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)

    # Initialize and connect
    try:
        await client.initialize()
        await client.connect()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")




if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║          LIGHTER FUTURES TRADING BOT                     ║
    ║          Points Farming - Zero Fees (Standard)           ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass