"""
Nado.xyz Fast Token Rotation Bot - Configuration
"""
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration for Nado fast token rotation bot"""

    # Network Configuration (mainnet, testnet, or devnet)
    NETWORK = os.getenv("NADO_NETWORK", "mainnet")

    # Account Configuration
    PRIVATE_KEY = os.getenv("NADO_PRIVATE_KEY", "")
    SUBACCOUNT_NAME = os.getenv("NADO_SUBACCOUNT_NAME", "default")  # max 12 bytes

    # Trading Configuration
    # Product IDs: 0=USDT0, 2=ETH-PERP, 3=SOL-PERP, 4=BTC-PERP, 5=BNB-PERP, 6=XRP-PERP
    TRADING_PRODUCTS: List[int] = [
        int(x.strip()) for x in os.getenv("NADO_TRADING_PRODUCTS", "2,4").split(",") if x.strip()
    ]

    # Product ID to symbol mapping
    PRODUCT_SYMBOLS: Dict[int, str] = {
        0: "USDT0",
        2: "ETH-PERP",
        3: "SOL-PERP",
        4: "BTC-PERP",
        5: "BNB-PERP",
        6: "XRP-PERP",
    }

    # Trade amounts (in USD)
    MIN_TRADE_AMOUNT = float(os.getenv("NADO_MIN_TRADE_AMOUNT", "10.0"))
    MAX_TRADE_AMOUNT = float(os.getenv("NADO_MAX_TRADE_AMOUNT", "50.0"))

    # Fast rotation timing
    POSITION_HOLD_TIME_MIN = float(os.getenv("NADO_HOLD_TIME_MIN", "5.0"))  # seconds
    POSITION_HOLD_TIME_MAX = float(os.getenv("NADO_HOLD_TIME_MAX", "30.0"))  # seconds
    DELAY_BETWEEN_TRADES = float(os.getenv("NADO_DELAY_BETWEEN_TRADES", "2.0"))  # seconds

    # Rate limits
    # With spot leverage: 600 orders/min = 10/sec (weight=1 per order)
    # Without: 30 orders/min (weight=20 per order)
    USE_SPOT_LEVERAGE = os.getenv("NADO_USE_SPOT_LEVERAGE", "true").lower() == "true"

    @classmethod
    def get_rate_limit_delay(cls) -> float:
        """Minimum delay between orders to respect rate limits"""
        if cls.USE_SPOT_LEVERAGE:
            return 0.12  # ~8 orders/sec to be safe (600/min = 10/sec)
        return 2.2  # ~27 orders/min to be safe (30/min limit)

    # Telegram Notifications
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    TELEGRAM_TOPIC_ID = os.getenv("TELEGRAM_TOPIC_ID")
    TELEGRAM_ENABLE = os.getenv("TELEGRAM_ENABLE_NOTIFICATIONS", "true").lower() == "true"

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.PRIVATE_KEY:
            raise ValueError("NADO_PRIVATE_KEY is required")

        if not cls.PRIVATE_KEY.startswith("0x"):
            raise ValueError("NADO_PRIVATE_KEY must start with 0x")

        if len(cls.PRIVATE_KEY) != 66:  # 0x + 64 hex chars
            raise ValueError("NADO_PRIVATE_KEY must be 64 hex characters (+ 0x prefix)")

        subaccount_bytes = cls.SUBACCOUNT_NAME.encode('utf-8')
        if len(subaccount_bytes) > 12:
            raise ValueError(f"NADO_SUBACCOUNT_NAME must be <= 12 bytes, got {len(subaccount_bytes)}")

        if not cls.TRADING_PRODUCTS:
            raise ValueError("NADO_TRADING_PRODUCTS must not be empty")

        if cls.MIN_TRADE_AMOUNT <= 0 or cls.MAX_TRADE_AMOUNT <= 0:
            raise ValueError("Trade amounts must be positive")

        if cls.MIN_TRADE_AMOUNT > cls.MAX_TRADE_AMOUNT:
            raise ValueError("MIN_TRADE_AMOUNT cannot exceed MAX_TRADE_AMOUNT")

        if cls.NETWORK not in ("mainnet", "testnet", "devnet"):
            raise ValueError(f"NADO_NETWORK must be mainnet, testnet, or devnet, got {cls.NETWORK}")

    @classmethod
    def get_product_symbol(cls, product_id: int) -> str:
        return cls.PRODUCT_SYMBOLS.get(product_id, f"PRODUCT-{product_id}")
