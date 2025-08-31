import asyncio
import signal
from typing import Optional

from src.config import Config
from src.database import DatabaseManager
from src.trading_engine import TradingEngine
from src.utils import setup_logger

logger = setup_logger("TradingBot", Config.LOG_LEVEL)


class TradingBot:
    """Main trading bot application"""

    def __init__(self):
        self.db_manager: Optional[DatabaseManager] = None
        self.trading_engine: Optional[TradingEngine] = None
        self.running = False
        self._shutdown_event = asyncio.Event()

    async def initialize(self):
        """Initialize all components"""
        try:
            # Validate configuration
            Config.validate()

            # Show configuration
            logger.info("=" * 60)
            logger.info("LIGHTER TRADING BOT - MAXIMUM EFFICIENCY MODE")
            logger.info("=" * 60)
            logger.info(f"Account Type: {Config.ACCOUNT_TYPE.upper()}")
            logger.info(f"Max Transactions/Minute: {Config.MAX_REQUESTS_PER_MINUTE}")
            logger.info(f"Batch Trading: {'ENABLED' if Config.USE_BATCH_ORDERS else 'DISABLED'}")
            logger.info(f"Delay Between Batches: {Config.SAFE_DELAY_BETWEEN_BATCHES}s")
            logger.info("=" * 60)

            # Initialize database
            self.db_manager = DatabaseManager(
                Config.MONGODB_URI,
                Config.MONGODB_DATABASE,
                Config.MONGODB_COLLECTION
            )
            await self.db_manager.connect()

            # Initialize trading engine
            self.trading_engine = TradingEngine(self.db_manager)
            await self.trading_engine.initialize()

            logger.info("Bot initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize bot: {e}")
            await self.cleanup()
            raise

    async def start(self):
        """Start the trading bot"""
        try:
            self.running = True
            await self.trading_engine.start()

        except Exception as e:
            logger.error(f"Bot error: {e}")
            await self.stop()

    async def stop(self):
        """Stop the trading bot"""
        if not self.running:
            return

        logger.info("Stopping trading bot...")
        self.running = False

        if self.trading_engine:
            await self.trading_engine.stop()

        self._shutdown_event.set()

    async def cleanup(self):
        """Cleanup all resources"""
        try:
            if self.trading_engine:
                await self.trading_engine.cleanup()

            if self.db_manager:
                await self.db_manager.disconnect()

            logger.info("Cleanup completed")

        except Exception as e:
            logger.error(f"Cleanup error: {e}")

    async def run(self):
        """Run the bot"""
        try:
            await self.initialize()

            # Setup signal handlers
            loop = asyncio.get_event_loop()
            for sig in (signal.SIGTERM, signal.SIGINT):
                loop.add_signal_handler(
                    sig,
                    lambda s=sig: asyncio.create_task(self._handle_signal(s))
                )

            # Start trading
            trading_task = asyncio.create_task(self.start())

            # Wait for shutdown
            await self._shutdown_event.wait()

            # Cancel trading task
            trading_task.cancel()
            try:
                await trading_task
            except asyncio.CancelledError:
                pass

        except Exception as e:
            logger.error(f"Fatal error: {e}")

        finally:
            await self.cleanup()

    async def _handle_signal(self, sig):
        """Handle shutdown signals"""
        logger.info(f"Received signal {sig.name}")
        await self.stop()