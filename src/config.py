import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration for futures trading with TP/SL"""

    # Lighter API
    BASE_URL = os.getenv("LIGHTER_BASE_URL", "https://mainnet.zklighter.elliot.ai")
    WS_URL = os.getenv("LIGHTER_WS_URL", "wss://mainnet.zklighter.elliot.ai/stream")
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
        SAFE_DELAY_BETWEEN_OPERATIONS = 0.5
    else:
        MAX_REQUESTS_PER_MINUTE = 10
        SAFE_DELAY_BETWEEN_OPERATIONS = 7

    # MongoDB
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "lighter_bot")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "transactions")

    # Trading
    MIN_TRADE_AMOUNT = float(os.getenv("MIN_TRADE_AMOUNT_USDC", "10.0"))
    MAX_TRADE_AMOUNT = float(os.getenv("MAX_TRADE_AMOUNT_USDC", "50.0"))
    TRADING_TOKENS: List[str] = os.getenv("TRADING_TOKENS", "ETH,BTC,SOL").split(",")
    DEFAULT_LEVERAGE = int(os.getenv("DEFAULT_LEVERAGE", "3"))

    # TP/SL Configuration (can be very small percentages)
    TAKE_PROFIT_PERCENT = float(os.getenv("TAKE_PROFIT_PERCENT", "0.1"))
    STOP_LOSS_PERCENT = float(os.getenv("STOP_LOSS_PERCENT", "0.5"))

    # Position timing
    POSITION_HOLD_TIME_MIN = float(os.getenv("POSITION_HOLD_TIME_MIN", "30"))
    POSITION_HOLD_TIME_MAX = float(os.getenv("POSITION_HOLD_TIME_MAX", "60"))
    DELAY_BETWEEN_TRADES_PER_TOKEN = float(os.getenv("DELAY_BETWEEN_TRADES_PER_TOKEN", "3"))

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Market indices
    MARKET_INDICES: Dict[str, int] = {
        "ETH": 0,
        "BTC": 1,
        "SOL": 2,
        "MATIC": 3,
        "AVAX": 4,
        "LINK": 5,
        "UNI": 6,
        "AAVE": 7,
        "HYPE": 24
    }

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