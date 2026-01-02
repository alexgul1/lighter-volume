"""
Telegram Notifications for Nado Bot

Full-featured Telegram notifier with topic support and command handling.
"""
import asyncio
import logging
from typing import Optional, Dict, Any, Callable, Awaitable
from datetime import datetime

import httpx

from src.config import Config

logger = logging.getLogger(__name__)


class TelegramNotifier:
    """
    Telegram notification service for trading events.
    Sends notifications about position opens/closes, PnL, and errors.
    Supports topics in supergroups and command handling.
    """

    def __init__(
        self,
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None,
        topic_id: Optional[int] = None
    ):
        """
        Initialize Telegram notifier.

        Args:
            bot_token: Telegram bot token from @BotFather (defaults to Config)
            chat_id: Chat ID or group ID to send messages to (defaults to Config)
            topic_id: Topic ID in a group (for supergroups with topics)
        """
        self.bot_token = bot_token or Config.TELEGRAM_BOT_TOKEN
        self.chat_id = chat_id or Config.TELEGRAM_CHAT_ID
        self.topic_id = topic_id or (int(Config.TELEGRAM_TOPIC_ID) if Config.TELEGRAM_TOPIC_ID else None)

        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        self.http: Optional[httpx.AsyncClient] = None
        self.enabled = Config.TELEGRAM_ENABLE and bool(self.bot_token and self.chat_id)

        # Command handling
        self.command_handlers: Dict[str, Callable[[], Awaitable[str]]] = {}
        self.last_update_id = 0
        self.polling_task: Optional[asyncio.Task] = None
        self.polling_enabled = False

        if not self.enabled:
            logger.warning("Telegram notifications disabled (missing token or chat_id)")
        else:
            topic_info = f", topic={self.topic_id}" if self.topic_id else ""
            logger.info(f"Telegram notifications enabled for chat {self.chat_id}{topic_info}")

    async def initialize(self):
        """Initialize HTTP session and send startup message"""
        if self.enabled:
            self.http = httpx.AsyncClient(timeout=30.0)
            try:
                await self.send_message(
                    "🤖 <b>Nado Bot Started</b>\n\n"
                    f"Network: <code>{Config.NETWORK}</code>\n"
                    f"Products: {[Config.get_product_symbol(p) for p in Config.TRADING_PRODUCTS]}\n"
                    f"Trade size: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}"
                )
            except Exception as e:
                logger.error(f"Failed to send startup message to Telegram: {e}")

    async def cleanup(self):
        """Cleanup HTTP session and stop command polling"""
        await self.stop_command_polling()
        if self.http:
            await self.http.aclose()

    async def close(self):
        """Alias for cleanup"""
        await self.cleanup()

    # ==================== Command Handling ====================

    def register_command(self, command: str, handler: Callable[[], Awaitable[str]]):
        """
        Register a command handler.

        Args:
            command: Command name (without leading /)
            handler: Async function that returns response text
        """
        self.command_handlers[command] = handler
        logger.info(f"Registered Telegram command: /{command}")

    async def start_command_polling(self):
        """Start polling for Telegram commands"""
        if not self.enabled:
            return

        self.polling_enabled = True
        self.polling_task = asyncio.create_task(self._command_polling_loop())
        logger.info("Started Telegram command polling")

    async def stop_command_polling(self):
        """Stop command polling"""
        if self.polling_task:
            self.polling_enabled = False
            self.polling_task.cancel()
            try:
                await self.polling_task
            except asyncio.CancelledError:
                pass
            self.polling_task = None

    async def _command_polling_loop(self):
        """Background task for polling Telegram commands"""
        while self.polling_enabled:
            try:
                await self._poll_commands()
                await asyncio.sleep(2)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Command polling error: {e}")
                await asyncio.sleep(5)

    async def _poll_commands(self):
        """Poll for new Telegram commands"""
        if not self.http:
            return

        try:
            params = {
                "offset": self.last_update_id + 1,
                "timeout": 1,
                "allowed_updates": ["message"]
            }

            response = await self.http.get(
                f"{self.base_url}/getUpdates",
                params=params,
                timeout=5.0
            )

            if response.status_code != 200:
                return

            data = response.json()
            if not data.get("ok"):
                return

            updates = data.get("result", [])
            for update in updates:
                self.last_update_id = update["update_id"]
                await self._handle_update(update)

        except httpx.TimeoutException:
            pass
        except Exception as e:
            logger.debug(f"Polling error: {e}")

    async def _handle_update(self, update: Dict[str, Any]):
        """Handle a single Telegram update"""
        message = update.get("message")
        if not message:
            return

        # Check if message is from our configured chat
        chat_id = str(message.get("chat", {}).get("id", ""))
        if chat_id != str(self.chat_id):
            return

        # Check topic if configured
        if self.topic_id:
            msg_topic = message.get("message_thread_id")
            if msg_topic != self.topic_id:
                return

        text = message.get("text", "")
        if not text.startswith("/"):
            return

        # Extract command (remove leading / and parameters)
        command = text[1:].split()[0].lower()

        # Find and execute handler
        handler = self.command_handlers.get(command)
        if handler:
            try:
                logger.info(f"Executing command: /{command}")
                response = await handler()
                await self.send_message(response)
            except Exception as e:
                logger.error(f"Command handler error for /{command}: {e}")
                await self.send_message(f"❌ Error executing command: {e}")

    # ==================== Message Sending ====================

    async def send_message(self, text: str, parse_mode: str = "HTML") -> bool:
        """
        Send a message to Telegram.

        Args:
            text: Message text
            parse_mode: HTML or Markdown

        Returns:
            True if sent successfully, False otherwise
        """
        if not self.enabled:
            return False

        # Create client if needed
        if not self.http:
            self.http = httpx.AsyncClient(timeout=30.0)

        try:
            data = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": parse_mode,
                "disable_web_page_preview": True
            }

            # Add topic ID if specified
            if self.topic_id:
                data["message_thread_id"] = self.topic_id

            response = await self.http.post(
                f"{self.base_url}/sendMessage",
                json=data,
                timeout=10.0
            )

            if response.status_code == 200:
                return True
            else:
                error_text = response.text
                logger.error(f"Telegram API error {response.status_code}: {error_text}")
                return False

        except httpx.TimeoutException:
            logger.error("Telegram API timeout")
            return False
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False

    # ==================== Trading Notifications ====================

    async def notify_position_opened(
        self,
        symbol: str,
        direction: str,
        amount_usd: float,
        entry_price: float,
        base_amount: float
    ):
        """Notify when a position is opened"""
        emoji = "📈" if direction.upper() == "LONG" else "📉"

        message = (
            f"{emoji} <b>Position Opened</b>\n\n"
            f"<b>Symbol:</b> {symbol}\n"
            f"<b>Direction:</b> {direction.upper()}\n"
            f"<b>Size:</b> ${amount_usd:.2f}\n"
            f"<b>Entry Price:</b> ${entry_price:.4f}\n"
            f"<b>Base Amount:</b> {base_amount:.6f}\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_position_closed(
        self,
        symbol: str,
        direction: str,
        amount_usd: float,
        entry_price: float,
        exit_price: float,
        pnl: float,
        hold_time_seconds: float
    ):
        """Notify when a position is closed"""
        emoji = "✅" if pnl >= 0 else "❌"
        pnl_emoji = "💚" if pnl >= 0 else "❤️"

        # Format hold time
        if hold_time_seconds >= 3600:
            hold_time_str = f"{hold_time_seconds/3600:.1f}h"
        elif hold_time_seconds >= 60:
            hold_time_str = f"{hold_time_seconds/60:.0f}m"
        else:
            hold_time_str = f"{hold_time_seconds:.0f}s"

        price_change = ((exit_price - entry_price) / entry_price) * 100

        message = (
            f"{emoji} <b>Position Closed</b>\n\n"
            f"<b>Symbol:</b> {symbol}\n"
            f"<b>Direction:</b> {direction.upper()}\n"
            f"<b>Size:</b> ${amount_usd:.2f}\n"
            f"<b>Entry:</b> ${entry_price:.4f}\n"
            f"<b>Exit:</b> ${exit_price:.4f}\n"
            f"<b>Price Change:</b> {price_change:+.2f}%\n"
            f"<b>P/L:</b> {pnl_emoji} ${pnl:+.4f}\n"
            f"<b>Hold Time:</b> {hold_time_str}\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_rotation_complete(
        self,
        symbol: str,
        direction: str,
        entry_price: float,
        exit_price: float,
        pnl: float,
        volume_usd: float,
        hold_time_seconds: float
    ):
        """Notify when a rotation cycle (open + close) is complete"""
        emoji = "✅" if pnl >= 0 else "❌"
        pnl_emoji = "💚" if pnl >= 0 else "❤️"

        if hold_time_seconds >= 60:
            hold_time_str = f"{hold_time_seconds/60:.1f}m"
        else:
            hold_time_str = f"{hold_time_seconds:.0f}s"

        message = (
            f"{emoji} <b>Rotation Complete</b>\n\n"
            f"<b>Symbol:</b> {symbol}\n"
            f"<b>Direction:</b> {direction.upper()}\n"
            f"<b>Entry:</b> ${entry_price:.4f}\n"
            f"<b>Exit:</b> ${exit_price:.4f}\n"
            f"<b>Volume:</b> ${volume_usd:.2f}\n"
            f"<b>P/L:</b> {pnl_emoji} ${pnl:+.4f}\n"
            f"<b>Hold Time:</b> {hold_time_str}\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_error(self, error_type: str, error_message: str, details: Optional[Dict[str, Any]] = None):
        """Notify about errors"""
        message = (
            f"⚠️ <b>Error: {error_type}</b>\n\n"
            f"<b>Message:</b> {error_message}\n"
        )

        if details:
            message += "\n<b>Details:</b>\n"
            for key, value in details.items():
                message += f"  • {key}: {value}\n"

        message += f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"

        await self.send_message(message)

    async def notify_summary(
        self,
        total_trades: int,
        successful_trades: int,
        failed_trades: int,
        total_volume: float,
        total_pnl: float,
        uptime_hours: float
    ):
        """Send trading summary"""
        pnl_emoji = "💚" if total_pnl >= 0 else "❤️"
        success_rate = (successful_trades / total_trades * 100) if total_trades > 0 else 0

        message = (
            f"📊 <b>Trading Summary</b>\n\n"
            f"<b>Uptime:</b> {uptime_hours:.1f}h\n"
            f"<b>Total Trades:</b> {total_trades}\n"
            f"<b>Successful:</b> {successful_trades}\n"
            f"<b>Failed:</b> {failed_trades}\n"
            f"<b>Success Rate:</b> {success_rate:.1f}%\n"
            f"<b>Total Volume:</b> ${total_volume:,.2f}\n"
            f"<b>Net P/L:</b> {pnl_emoji} <b>${total_pnl:+.2f}</b>\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_status(
        self,
        running: bool,
        balance_usd: float,
        health: float,
        open_positions: int,
        total_trades: int,
        success_rate: float,
        total_volume: float,
        uptime_hours: float
    ):
        """Send current bot status"""
        status_emoji = "🟢" if running else "🔴"
        status_text = "Running" if running else "Stopped"

        message = (
            f"📊 <b>Nado Bot Status</b>\n\n"
            f"<b>Status:</b> {status_emoji} {status_text}\n"
            f"<b>Network:</b> {Config.NETWORK}\n"
            f"<b>Balance:</b> ${balance_usd:,.2f}\n"
            f"<b>Health:</b> {health:.4f}\n"
            f"<b>Open Positions:</b> {open_positions}\n\n"
            f"<b>Session Stats:</b>\n"
            f"  Total Trades: {total_trades}\n"
            f"  Success Rate: {success_rate:.1f}%\n"
            f"  Volume: ${total_volume:,.2f}\n"
            f"  Uptime: {uptime_hours:.1f}h\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_balance(
        self,
        balance_usd: float,
        health: float,
        pnl: Optional[float] = None
    ):
        """Send balance update"""
        message = f"💰 <b>Account Balance</b>\n\n"
        message += f"<b>Balance:</b> ${balance_usd:,.2f}\n"
        message += f"<b>Health:</b> {health:.4f}\n"

        if pnl is not None:
            pnl_emoji = "💚" if pnl >= 0 else "❤️"
            message += f"<b>Session P/L:</b> {pnl_emoji} ${pnl:+.2f}\n"

        message += f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"

        await self.send_message(message)

    async def notify_shutdown(
        self,
        reason: str,
        total_trades: int,
        total_volume: float,
        uptime_hours: float
    ):
        """Notify about bot shutdown"""
        message = (
            f"🛑 <b>Nado Bot Stopped</b>\n\n"
            f"<b>Reason:</b> {reason}\n"
            f"<b>Total Trades:</b> {total_trades}\n"
            f"<b>Volume:</b> ${total_volume:,.2f}\n"
            f"<b>Uptime:</b> {uptime_hours:.1f}h\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)
