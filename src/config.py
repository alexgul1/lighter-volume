import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration optimized for standard accounts"""

    # Lighter API
    BASE_URL = os.getenv("LIGHTER_BASE_URL", "https://mainnet.zklighter.elliot.ai")
    API_KEY_PRIVATE_KEY = os.getenv("LIGHTER_API_KEY_PRIVATE_KEY")
    ETH_PRIVATE_KEY = os.getenv("LIGHTER_ETH_PRIVATE_KEY")
    ACCOUNT_INDEX = int(os.getenv("LIGHTER_ACCOUNT_INDEX", "1"))
    API_KEY_INDEX = int(os.getenv("LIGHTER_API_KEY_INDEX", "2"))

    # Account Type
    ACCOUNT_TYPE = os.getenv("ACCOUNT_TYPE", "standard").lower()
    IS_PREMIUM = ACCOUNT_TYPE == "premium"

    # API Limits based on account type
    # Standard: 60 rpm total, but sendTx has weight 6, so max 10 transactions/minute
    # Premium: 24000 weighted rpm, so max 4000 transactions/minute with weight 6
    if IS_PREMIUM:
        MAX_REQUESTS_PER_MINUTE = 4000  # Premium can do much more
        SAFE_DELAY_BETWEEN_BATCHES = 0.1  # 100ms between batches
    else:
        MAX_REQUESTS_PER_MINUTE = 10  # Standard: 60/6 = 10 max
        SAFE_DELAY_BETWEEN_BATCHES = 6.5  # ~9 requests per minute to be safe

    # MongoDB
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "lighter_bot")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", "transactions")

    # Trading
    MIN_TRADE_AMOUNT = float(os.getenv("MIN_TRADE_AMOUNT_USDC", "10.0"))
    MAX_TRADE_AMOUNT = float(os.getenv("MAX_TRADE_AMOUNT_USDC", "100.0"))
    TRADING_TOKENS: List[str] = os.getenv("TRADING_TOKENS", "ETH,BTC,SOL").split(",")
    STABLE_COIN = os.getenv("STABLE_COIN", "USDC")

    # Batch Trading (to maximize efficiency)
    USE_BATCH_ORDERS = os.getenv("USE_BATCH_ORDERS", "true").lower() == "true"
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", "2"))  # Buy + Sell in one batch

    # Bot Settings (less frequent checks to save API calls)
    RETRY_FAILED_SELLS_INTERVAL = int(os.getenv("RETRY_FAILED_SELLS_INTERVAL", "120"))
    CHECK_UNPAIRED_INTERVAL = int(os.getenv("CHECK_UNPAIRED_INTERVAL", "300"))

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Market indices mapping (update based on actual Lighter markets)
    MARKET_INDICES: Dict[str, int] = {
        "ETH": 0,
        "BTC": 1,
        "SOL": 2,
        "MATIC": 3,
        "AVAX": 4,
        "LINK": 5,
        "UNI": 6,
        "AAVE": 7
    }

    # Maximum slippage prices (essentially infinite for market orders)
    # For buys: very high price, for sells: very low price
    MAX_BUY_PRICE = 999999999  # Essentially no limit
    MIN_SELL_PRICE = 1  # Accept any price

    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.API_KEY_PRIVATE_KEY:
            raise ValueError("LIGHTER_API_KEY_PRIVATE_KEY is required")
        if not cls.ETH_PRIVATE_KEY:
            raise ValueError("LIGHTER_ETH_PRIVATE_KEY is required")
        for token in cls.TRADING_TOKENS:
            if token not in cls.MARKET_INDICES:
                raise ValueError(f"Unknown token: {token}. Please update MARKET_INDICES in config.")