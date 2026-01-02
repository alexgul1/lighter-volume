#!/usr/bin/env python3
"""
Nado.xyz Fast Token Rotation Bot

Entry point for the trading bot.
"""
import asyncio
import signal
import logging
import sys

from src.config import Config
from src.trading_engine import TradingEngine
from src.telegram_notifier import TelegramNotifier


def setup_logging():
    """Configure logging"""
    level = getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Reduce noise from libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)


async def main():
    """Main entry point"""
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("=" * 60)
    logger.info("  Nado.xyz Fast Token Rotation Bot")
    logger.info("=" * 60)

    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)

    # Initialize components
    telegram = TelegramNotifier()
    engine = TradingEngine(telegram_notifier=telegram)

    # Setup graceful shutdown
    shutdown_event = asyncio.Event()

    def handle_shutdown(signum, frame):
        logger.info(f"Received signal {signum}, initiating shutdown...")
        shutdown_event.set()

    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    try:
        # Initialize engine
        await engine.initialize()

        # Create trading task
        trading_task = asyncio.create_task(engine.start())

        # Wait for shutdown signal
        await shutdown_event.wait()

        # Stop engine
        await engine.stop()
        trading_task.cancel()

        try:
            await trading_task
        except asyncio.CancelledError:
            pass

    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        if telegram.enabled:
            await telegram.notify_error(str(e))
        sys.exit(1)

    finally:
        await engine.cleanup()
        await telegram.close()
        logger.info("Shutdown complete")


if __name__ == "__main__":
    asyncio.run(main())
