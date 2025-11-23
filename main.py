#!/usr/bin/env python3
"""
Lighter Futures Trading Bot
"""

import asyncio
import sys
from src.bot import TradingBot
from src.utils import setup_logger
from src.config import Config

logger = setup_logger("Main", Config.LOG_LEVEL)


async def main():
    """Main entry point"""
    bot = TradingBot()

    try:
        await bot.run()
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║       LIGHTER HEDGED FUTURES TRADING BOT                 ║
    ║       Low OI Farming - Dual Account Strategy             ║
    ╚══════════════════════════════════════════════════════════╝
    """)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass