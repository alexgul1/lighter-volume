#!/usr/bin/env python3
"""
Nado.xyz Fast Token Rotation Bot

Entry point for the trading bot with Telegram command support.
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
        # Initialize telegram
        await telegram.initialize()

        # Register Telegram commands
        async def cmd_status() -> str:
            """Handle /status command"""
            try:
                status = await engine.get_status()
                return (
                    f"📊 <b>Nado Bot Status</b>\n\n"
                    f"<b>Status:</b> {'🟢 Running' if status['running'] else '🔴 Stopped'}\n"
                    f"<b>Network:</b> {Config.NETWORK}\n"
                    f"<b>Address:</b> <code>{status['address'][:10]}...</code>\n"
                    f"<b>Balance:</b> ${status['balance_usd']:,.2f}\n"
                    f"<b>Health:</b> {status['health']:.4f}\n"
                    f"<b>Open Positions:</b> {status['open_positions']}\n\n"
                    f"<b>Session Stats:</b>\n"
                    f"  Total Trades: {status['stats']['total_trades']}\n"
                    f"  Success Rate: {status['stats']['success_rate']:.1f}%\n"
                    f"  Volume: ${status['stats']['total_volume']:,.2f}\n"
                    f"  Uptime: {status['stats']['uptime_hours']:.1f}h"
                )
            except Exception as e:
                return f"❌ Failed to get status: {e}"

        async def cmd_balance() -> str:
            """Handle /balance command"""
            try:
                status = await engine.get_status()
                return (
                    f"💰 <b>Account Balance</b>\n\n"
                    f"<b>Balance:</b> ${status['balance_usd']:,.2f}\n"
                    f"<b>Health:</b> {status['health']:.4f}\n"
                    f"<b>Open Positions:</b> {status['open_positions']}"
                )
            except Exception as e:
                return f"❌ Failed to get balance: {e}"

        async def cmd_stats() -> str:
            """Handle /stats command"""
            try:
                status = await engine.get_status()
                stats = status['stats']
                return (
                    f"📈 <b>Trading Statistics</b>\n\n"
                    f"<b>Total Trades:</b> {stats['total_trades']}\n"
                    f"<b>Successful:</b> {stats['successful_trades']}\n"
                    f"<b>Success Rate:</b> {stats['success_rate']:.1f}%\n"
                    f"<b>Total Volume:</b> ${stats['total_volume']:,.2f}\n"
                    f"<b>Uptime:</b> {stats['uptime_hours']:.1f}h"
                )
            except Exception as e:
                return f"❌ Failed to get stats: {e}"

        async def cmd_help() -> str:
            """Handle /help command"""
            return (
                "🤖 <b>Nado Bot Commands</b>\n\n"
                "/status - Show bot status and balance\n"
                "/balance - Show account balance\n"
                "/stats - Show trading statistics\n"
                "/help - Show this help message"
            )

        telegram.register_command("status", cmd_status)
        telegram.register_command("balance", cmd_balance)
        telegram.register_command("stats", cmd_stats)
        telegram.register_command("help", cmd_help)

        # Start command polling
        await telegram.start_command_polling()

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

        # Send shutdown notification
        await telegram.notify_shutdown(
            reason="Manual shutdown",
            total_trades=engine.stats.total_trades,
            total_volume=engine.stats.total_volume_usd,
            uptime_hours=engine.stats.uptime_hours
        )

    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        if telegram.enabled:
            await telegram.notify_error("Fatal Error", str(e))
        sys.exit(1)

    finally:
        await engine.cleanup()
        await telegram.close()
        logger.info("Shutdown complete")


if __name__ == "__main__":
    asyncio.run(main())
