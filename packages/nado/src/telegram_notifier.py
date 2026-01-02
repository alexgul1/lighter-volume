"""
Telegram Notifications for Nado Bot
"""
import logging
from typing import Optional

import httpx

from src.config import Config

logger = logging.getLogger(__name__)


class TelegramNotifier:
    """Simple Telegram notification sender"""

    def __init__(self):
        self.enabled = Config.TELEGRAM_ENABLE and Config.TELEGRAM_BOT_TOKEN and Config.TELEGRAM_CHAT_ID
        self.bot_token = Config.TELEGRAM_BOT_TOKEN
        self.chat_id = Config.TELEGRAM_CHAT_ID
        self.topic_id = Config.TELEGRAM_TOPIC_ID
        self.http = httpx.AsyncClient(timeout=10.0)

        if self.enabled:
            logger.info("Telegram notifications enabled")
        else:
            logger.info("Telegram notifications disabled")

    async def send_message(self, text: str, parse_mode: str = "Markdown") -> bool:
        """
        Send a message to Telegram.

        Args:
            text: Message text (supports Markdown)
            parse_mode: Parse mode (Markdown or HTML)

        Returns:
            True if sent successfully
        """
        if not self.enabled:
            return False

        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

            payload = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": parse_mode
            }

            if self.topic_id:
                payload["message_thread_id"] = int(self.topic_id)

            response = await self.http.post(url, json=payload)
            response.raise_for_status()

            result = response.json()
            if not result.get("ok"):
                logger.warning(f"Telegram API error: {result}")
                return False

            return True

        except Exception as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False

    async def notify_trade(
        self,
        symbol: str,
        direction: str,
        amount_usd: float,
        price: float,
        pnl: Optional[float] = None
    ):
        """Notify about a trade"""
        emoji = "🟢" if direction.upper() == "LONG" else "🔴"

        text = f"{emoji} *{direction.upper()} {symbol}*\n"
        text += f"Amount: ${amount_usd:.2f}\n"
        text += f"Price: ${price:.2f}"

        if pnl is not None:
            pnl_emoji = "💚" if pnl >= 0 else "❤️"
            text += f"\nPnL: {pnl_emoji} ${pnl:+.4f}"

        await self.send_message(text)

    async def notify_error(self, error: str):
        """Notify about an error"""
        await self.send_message(f"⚠️ *Error*\n\n`{error}`")

    async def close(self):
        """Close HTTP client"""
        await self.http.aclose()
