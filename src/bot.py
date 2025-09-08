import asyncio
import signal
from typing import Optional

from src.config import Config
from src.database import DatabaseManager
from src.trading_engine import TradingEngine
from src.utils import setup_logger

logger = setup_logger("TradingBot", Config.LOG_LEVEL)


class TradingBot:
    """Main trading bot application with TP/SL support"""

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

            # Show configuration with TP/SL info
            logger.info("=" * 60)
            logger.info("LIGHTER FUTURES TRADING BOT WITH TP/SL")
            logger.info("=" * 60)
            logger.info(f"Account Type: {Config.ACCOUNT_TYPE.upper()}")
            logger.info(f"Leverage: {Config.DEFAULT_LEVERAGE}x")
            logger.info(f"Tokens: {Config.TRADING_TOKENS}")
            logger.info(f"Position Size: ${Config.MIN_TRADE_AMOUNT}-${Config.MAX_TRADE_AMOUNT}")
            logger.info("-" * 60)
            logger.info("POSITION MANAGEMENT:")
            logger.info(f"Take Profit: {Config.TP_PERCENT * 100:.3f}%")
            logger.info(f"Stop Loss: {Config.SL_PERCENT * 100:.3f}%")
            logger.info(f"Hold Time: {Config.POSITION_HOLD_TIME_MIN}-{Config.POSITION_HOLD_TIME_MAX}s")
            logger.info(f"Max Hold: {Config.MAX_HOLD_SECONDS}s")
            logger.info(f"Per-Token Cooldown: {Config.DELAY_BETWEEN_TRADES}s")
            logger.info(f"Max Positions/Token: {Config.MAX_POSITIONS_PER_TOKEN}")
            logger.info("-" * 60)
            logger.info("RATE LIMITS:")
            if Config.IS_PREMIUM:
                logger.info(f"Premium Account: {Config.MAX_REQUESTS_PER_MINUTE} requests/min")
                logger.info(f"Min delay between trades: {Config.SAFE_DELAY_BETWEEN_TRADES}s")
            else:
                logger.info(f"Standard Account: {Config.MAX_REQUESTS_PER_MINUTE} trades/min max")
                logger.info(f"Safe delay between trades: {Config.SAFE_DELAY_BETWEEN_TRADES}s")
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

            logger.info("Bot initialized successfully with TP/SL support")

        except Exception as e:
            logger.error(f"Failed to initialize bot: {e}")
            await self.cleanup()
            raise

    async def start(self):
        """Start the trading bot"""
        try:
            self.running = True

            logger.info("-" * 60)
            logger.info("Trading Strategy:")
            logger.info("1. Open random long/short positions")
            logger.info("2. Set TP/SL orders automatically")
            logger.info("3. Positions close via:")
            logger.info("   - Take Profit hit")
            logger.info("   - Stop Loss hit")
            logger.info("   - Random hold time")
            logger.info("   - Max hold time reached")
            logger.info("4. Per-token cooldown after close")
            logger.info("-" * 60)

            await self.trading_engine.start()

        except Exception as e:
            logger.error(f"Bot error: {e}")
            await self.stop()

    async def stop(self):
        """Stop the trading bot gracefully"""
        if not self.running:
            return

        logger.info("Stopping trading bot...")
        logger.info("Cancelling pending TP/SL orders...")
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

            # Setup signal handlers for graceful shutdown
            loop = asyncio.get_event_loop()
            for sig in (signal.SIGTERM, signal.SIGINT):
                loop.add_signal_handler(
                    sig,
                    lambda s=sig: asyncio.create_task(self._handle_signal(s))
                )

            # Start trading
            trading_task = asyncio.create_task(self.start())

            # Wait for shutdown signal
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
        logger.info("Initiating graceful shutdown...")
        await self.stop()