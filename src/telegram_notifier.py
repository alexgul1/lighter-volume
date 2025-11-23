import asyncio
import aiohttp
from typing import Optional, Dict, Any
from datetime import datetime
from src.utils import setup_logger
from src.config import Config

logger = setup_logger(__name__, Config.LOG_LEVEL)


class TelegramNotifier:
    """
    Telegram notification service for trading events.
    Sends notifications about position opens/closes, PnL, and errors.
    """

    def __init__(self, bot_token: str, chat_id: str, message_thread_id: Optional[int] = None):
        """
        Initialize Telegram notifier.

        Args:
            bot_token: Telegram bot token from @BotFather
            chat_id: Chat ID or group ID to send messages to
            message_thread_id: Topic ID in a group (for supergroups with topics)
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.message_thread_id = message_thread_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.session: Optional[aiohttp.ClientSession] = None
        self.enabled = bool(bot_token and chat_id)

        if not self.enabled:
            logger.warning("Telegram notifications disabled (missing token or chat_id)")
        else:
            logger.info(f"Telegram notifications enabled for chat {chat_id}")

    async def initialize(self):
        """Initialize HTTP session"""
        if self.enabled:
            self.session = aiohttp.ClientSession()
            # Test connection
            try:
                await self.send_message("🤖 Lighter Bot Started\n\n"
                                      "Hedged trading bot is now active and monitoring markets.")
            except Exception as e:
                logger.error(f"Failed to send test message to Telegram: {e}")

    async def cleanup(self):
        """Cleanup HTTP session"""
        if self.session:
            await self.session.close()

    async def send_message(self, text: str, parse_mode: str = "HTML") -> bool:
        """
        Send a message to Telegram.

        Args:
            text: Message text
            parse_mode: HTML or Markdown

        Returns:
            True if sent successfully, False otherwise
        """
        if not self.enabled or not self.session:
            return False

        try:
            data = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": parse_mode,
                "disable_web_page_preview": True
            }

            # Add topic ID if specified (for groups with topics)
            if self.message_thread_id:
                data["message_thread_id"] = self.message_thread_id

            async with self.session.post(
                f"{self.base_url}/sendMessage",
                json=data,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status == 200:
                    return True
                else:
                    error_text = await response.text()
                    logger.error(f"Telegram API error {response.status}: {error_text}")
                    return False

        except asyncio.TimeoutError:
            logger.error("Telegram API timeout")
            return False
        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False

    async def notify_position_opened(
        self,
        position_id: str,
        token: str,
        position_type: str,
        account_num: int,
        amount_usdc: float,
        entry_price: float,
        base_amount: int,
        open_interest: float,
        pair_id: Optional[str] = None
    ):
        """Notify when a position is opened"""
        emoji = "📈" if position_type == "long" else "📉"

        message = (
            f"{emoji} <b>Position Opened</b>\n\n"
            f"<b>Token:</b> {token}\n"
            f"<b>Type:</b> {position_type.upper()}\n"
            f"<b>Account:</b> {account_num}\n"
            f"<b>Size:</b> ${amount_usdc:.2f}\n"
            f"<b>Entry Price:</b> ${entry_price:.4f}\n"
            f"<b>Base Amount:</b> {base_amount}\n"
            f"<b>Open Interest:</b> ${open_interest:,.0f}\n"
            f"<b>Position ID:</b> <code>{position_id}</code>\n"
        )

        if pair_id:
            message += f"<b>Pair ID:</b> <code>{pair_id}</code>\n"

        message += f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"

        await self.send_message(message)

    async def notify_hedged_pair_opened(
        self,
        token: str,
        position_1_id: str,
        position_1_type: str,
        position_1_amount: float,
        position_1_account: int,
        position_2_id: str,
        position_2_type: str,
        position_2_amount: float,
        position_2_account: int,
        entry_price: float,
        open_interest: float
    ):
        """Notify when a hedged pair is opened"""
        total_size = position_1_amount + position_2_amount

        message = (
            f"🎯 <b>Hedged Pair Opened</b>\n\n"
            f"<b>Token:</b> {token}\n"
            f"<b>Price:</b> ${entry_price:.4f}\n"
            f"<b>Open Interest:</b> ${open_interest:,.0f}\n"
            f"<b>Total Size:</b> ${total_size:.2f}\n\n"

            f"📈 <b>Position 1 ({position_1_type.upper()}):</b>\n"
            f"  Account: {position_1_account}\n"
            f"  Size: ${position_1_amount:.2f}\n"
            f"  ID: <code>{position_1_id}</code>\n\n"

            f"📉 <b>Position 2 ({position_2_type.upper()}):</b>\n"
            f"  Account: {position_2_account}\n"
            f"  Size: ${position_2_amount:.2f}\n"
            f"  ID: <code>{position_2_id}</code>\n\n"

            f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_position_closed(
        self,
        position_id: str,
        token: str,
        position_type: str,
        account_num: int,
        amount_usdc: float,
        entry_price: float,
        exit_price: Optional[float] = None,
        hold_time_hours: Optional[float] = None,
        pnl: Optional[float] = None
    ):
        """Notify when a position is closed"""
        emoji = "✅" if (pnl and pnl >= 0) else "❌"

        message = (
            f"{emoji} <b>Position Closed</b>\n\n"
            f"<b>Token:</b> {token}\n"
            f"<b>Type:</b> {position_type.upper()}\n"
            f"<b>Account:</b> {account_num}\n"
            f"<b>Size:</b> ${amount_usdc:.2f}\n"
            f"<b>Entry:</b> ${entry_price:.4f}\n"
        )

        if exit_price:
            message += f"<b>Exit:</b> ${exit_price:.4f}\n"
            price_change = ((exit_price - entry_price) / entry_price) * 100
            message += f"<b>Price Change:</b> {price_change:+.2f}%\n"

        if pnl is not None:
            pnl_emoji = "💚" if pnl >= 0 else "❤️"
            message += f"<b>P/L:</b> {pnl_emoji} ${pnl:+.2f}\n"

        if hold_time_hours:
            message += f"<b>Hold Time:</b> {hold_time_hours:.1f}h\n"

        message += (
            f"<b>Position ID:</b> <code>{position_id}</code>\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_hedged_pair_closed(
        self,
        token: str,
        position_1_id: str,
        position_1_pnl: float,
        position_2_id: str,
        position_2_pnl: float,
        total_pnl: float,
        entry_price: float,
        exit_price: Optional[float] = None,
        hold_time_hours: Optional[float] = None
    ):
        """Notify when a hedged pair is closed with combined P/L"""
        emoji = "✅" if total_pnl >= 0 else "❌"
        pnl_emoji = "💚" if total_pnl >= 0 else "❤️"

        message = (
            f"{emoji} <b>Hedged Pair Closed</b>\n\n"
            f"<b>Token:</b> {token}\n"
            f"<b>Entry:</b> ${entry_price:.4f}\n"
        )

        if exit_price:
            message += f"<b>Exit:</b> ${exit_price:.4f}\n"

        message += (
            f"\n<b>Position 1:</b>\n"
            f"  ID: <code>{position_1_id}</code>\n"
            f"  P/L: ${position_1_pnl:+.2f}\n\n"

            f"<b>Position 2:</b>\n"
            f"  ID: <code>{position_2_id}</code>\n"
            f"  P/L: ${position_2_pnl:+.2f}\n\n"

            f"<b>Net P/L:</b> {pnl_emoji} <b>${total_pnl:+.2f}</b>\n"
        )

        if hold_time_hours:
            message += f"<b>Hold Time:</b> {hold_time_hours:.1f}h\n"

        message += f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"

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

    async def notify_restart(self, reason: str):
        """Notify about bot restart"""
        message = (
            f"🔄 <b>Bot Restarting</b>\n\n"
            f"<b>Reason:</b> {reason}\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)

    async def notify_summary(
        self,
        total_positions: int,
        successful_trades: int,
        failed_trades: int,
        total_pnl: float,
        uptime_hours: float
    ):
        """Send daily/hourly summary"""
        pnl_emoji = "💚" if total_pnl >= 0 else "❤️"

        message = (
            f"📊 <b>Trading Summary</b>\n\n"
            f"<b>Uptime:</b> {uptime_hours:.1f}h\n"
            f"<b>Total Positions:</b> {total_positions}\n"
            f"<b>Successful:</b> {successful_trades}\n"
            f"<b>Failed:</b> {failed_trades}\n"
            f"<b>Success Rate:</b> {(successful_trades/(total_positions or 1))*100:.1f}%\n"
            f"<b>Net P/L:</b> {pnl_emoji} <b>${total_pnl:+.2f}</b>\n"
            f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )

        await self.send_message(message)
