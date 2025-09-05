import asyncio
import signal
from typing import Optional

from src.config import Config
from src.database import DatabaseManager
from src.trading_engine import TradingEngine
from src.utils import setup_logger

logger = setup_logger("TradingBot", Config.LOG_LEVEL)


class TradingBot:
    """Enhanced trading bot with WebSocket position monitoring"""

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

            # Show enhanced configuration
            logger.info("=" * 60)
            logger.info("LIGHTER FUTURES TRADING BOT V10")
            logger.info("Enhanced with WebSocket Position Monitoring")
            logger.info("=" * 60)
            logger.info(f"Account Type: {Config.ACCOUNT_TYPE.upper()}")
            logger.info(f"Leverage: {Config.DEFAULT_LEVERAGE}x")
            logger.info(f"Tokens: {Config.TRADING_TOKENS}")
            logger.info(f"Position Size: ${Config.MIN_TRADE_AMOUNT}-${Config.MAX_TRADE_AMOUNT}")
            logger.info(f"Hold Time: {Config.POSITION_HOLD_TIME_MIN}-{Config.POSITION_HOLD_TIME_MAX}s")
            logger.info(f"Max Hold: {Config.MAX_HOLD_SECONDS}s")
            logger.info(f"TP/SL: {Config.TP_PERCENT*100:.3f}%/{Config.SL_PERCENT*100:.3f}%")
            logger.info(f"Per-Token Cooldown: {Config.DELAY_BETWEEN_TRADES}s")
            logger.info(f"Max Positions per Token: {Config.MAX_POSITIONS_PER_TOKEN}")
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

            logger.info("Bot initialized successfully with WebSocket support")

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