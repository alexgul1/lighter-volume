import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration for futures trading"""

    # Lighter API
    BASE_URL = os.getenv("LIGHTER_BASE_URL", "https://mainnet.zklighter.elliot.ai")
    API_KEY_PRIVATE_KEY = os.getenv("LIGHTER_API_KEY_PRIVATE_KEY")
    ETH_PRIVATE_KEY = os.getenv("LIGHTER_ETH_PRIVATE_KEY")
    ACCOUNT_INDEX = int(os.getenv("LIGHTER_ACCOUNT_INDEX", "1"))
    API_KEY_INDEX = int(os.getenv("LIGHTER_API_KEY_INDEX", "2"))

    # Account Type
    ACCOUNT_TYPE = os.getenv("ACCOUNT_TYPE", "standard").lower()
    IS_PREMIUM = ACCOUNT_TYPE == "premium"

    # API Limits
    if IS_PREMIUM:
        MAX_REQUESTS_PER_MINUTE = 4000
        SAFE_DELAY_BETWEEN_TRADES = 0.5
    else:
        MAX_REQUESTS_PER_MINUTE = 10  # Standard: 60/6 = 10 max
        SAFE_DELAY_BETWEEN_TRADES = 7  # Safe for standard account

    # MongoDB
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "lighter_bot")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "transactions")

    # Trading
    MIN_TRADE_AMOUNT = float(os.getenv("MIN_TRADE_AMOUNT_USDC", "10.0"))
    MAX_TRADE_AMOUNT = float(os.getenv("MAX_TRADE_AMOUNT_USDC", "50.0"))
    TRADING_TOKENS: List[str] = os.getenv("TRADING_TOKENS", "ETH,BTC,SOL").split(",")
    DEFAULT_LEVERAGE = int(os.getenv("DEFAULT_LEVERAGE", "3"))

    # Position timing
    POSITION_HOLD_TIME_MIN = float(os.getenv("POSITION_HOLD_TIME_MIN", "2"))
    POSITION_HOLD_TIME_MAX = float(os.getenv("POSITION_HOLD_TIME_MAX", "5"))
    DELAY_BETWEEN_TRADES = float(os.getenv("DELAY_BETWEEN_TRADES", "3"))

    # Error handling and recovery
    MAX_CONSECUTIVE_FAILURES = int(os.getenv("MAX_CONSECUTIVE_FAILURES", "7"))  # 5-10 range, default 7
    PAUSE_DURATION_SECONDS = int(os.getenv("PAUSE_DURATION_SECONDS", "60"))  # 1 minute pause

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Market indices (from Lighter)
    MARKET_INDICES: Dict[str, int] = {
        "ETH": 0,
        "BTC": 1,
        "SOL": 2,
        "MATIC": 3,
        "AVAX": 4,
        "LINK": 5,
        "UNI": 6,
        "AAVE": 7,
        "HYPE": 24  # Added from your example
    }

    # Price scaling (Lighter uses integer prices with 2 decimal places)
    PRICE_SCALE = 100  # For price conversion
    BASE_AMOUNT_SCALE = 1  # BaseAmount seems to be in smallest units

    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.API_KEY_PRIVATE_KEY:
            raise ValueError("LIGHTER_API_KEY_PRIVATE_KEY is required")
        if not cls.ETH_PRIVATE_KEY:
            raise ValueError("LIGHTER_ETH_PRIVATE_KEY is required")
        for token in cls.TRADING_TOKENS:
            if token not in cls.MARKET_INDICES:
                raise ValueError(f"Unknown token: {token}")