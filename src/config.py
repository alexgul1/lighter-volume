import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration for hedged futures trading with dual accounts"""

    # Lighter API
    BASE_URL = os.getenv("LIGHTER_BASE_URL", "https://mainnet.zklighter.elliot.ai")

    # Account 1 (Primary)
    ACCOUNT_1_PRIVATE_KEY = os.getenv("LIGHTER_ACCOUNT_1_PRIVATE_KEY")
    ACCOUNT_1_INDEX = int(os.getenv("LIGHTER_ACCOUNT_1_INDEX", "1"))
    ACCOUNT_1_API_KEY_INDEX = int(os.getenv("LIGHTER_ACCOUNT_1_API_KEY_INDEX", "2"))

    # Account 2 (Secondary)
    ACCOUNT_2_PRIVATE_KEY = os.getenv("LIGHTER_ACCOUNT_2_PRIVATE_KEY")
    ACCOUNT_2_INDEX = int(os.getenv("LIGHTER_ACCOUNT_2_INDEX", "1"))
    ACCOUNT_2_API_KEY_INDEX = int(os.getenv("LIGHTER_ACCOUNT_2_API_KEY_INDEX", "2"))

    # Legacy support (fallback to single account if dual not configured)
    LEGACY_API_KEY_PRIVATE_KEY = os.getenv("LIGHTER_API_KEY_PRIVATE_KEY")
    LEGACY_ACCOUNT_INDEX = int(os.getenv("LIGHTER_ACCOUNT_INDEX", "1"))
    LEGACY_API_KEY_INDEX = int(os.getenv("LIGHTER_API_KEY_INDEX", "2"))

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

    # Trading Strategy
    MIN_TRADE_AMOUNT = float(os.getenv("MIN_TRADE_AMOUNT_USDC", "10.0"))
    MAX_TRADE_AMOUNT = float(os.getenv("MAX_TRADE_AMOUNT_USDC", "50.0"))
    TRADING_TOKENS: List[str] = os.getenv("TRADING_TOKENS", "ETH,BTC,SOL").split(",")
    DEFAULT_LEVERAGE = int(os.getenv("DEFAULT_LEVERAGE", "3"))

    # Hedging Configuration
    # Randomization between dual account trades to avoid exact matching
    TRADE_AMOUNT_VARIANCE_PERCENT = float(os.getenv("TRADE_AMOUNT_VARIANCE_PERCENT", "2.0"))  # 1-3% variance
    TRADE_TIMING_DELAY_MIN = float(os.getenv("TRADE_TIMING_DELAY_MIN", "1.0"))  # Min seconds between paired trades
    TRADE_TIMING_DELAY_MAX = float(os.getenv("TRADE_TIMING_DELAY_MAX", "5.0"))  # Max seconds between paired trades

    # Position Timing (in seconds)
    # Default: 1-3 hours = 3600-10800 seconds
    POSITION_HOLD_TIME_MIN = float(os.getenv("POSITION_HOLD_TIME_MIN", "3600"))  # 1 hour
    POSITION_HOLD_TIME_MAX = float(os.getenv("POSITION_HOLD_TIME_MAX", "10800"))  # 3 hours
    DELAY_BETWEEN_TRADES = float(os.getenv("DELAY_BETWEEN_TRADES", "10"))

    # Error handling and recovery
    MAX_CONSECUTIVE_FAILURES = int(os.getenv("MAX_CONSECUTIVE_FAILURES", "7"))  # 5-10 range, default 7
    PAUSE_DURATION_SECONDS = int(os.getenv("PAUSE_DURATION_SECONDS", "60"))  # 1 minute pause

    # Low OI Token Selection
    # Enable filtering for low open interest tokens (better rewards)
    ENABLE_LOW_OI_FILTER = os.getenv("ENABLE_LOW_OI_FILTER", "true").lower() == "true"
    MAX_OPEN_INTEREST_THRESHOLD = float(os.getenv("MAX_OPEN_INTEREST_THRESHOLD", "1000000"))  # Max OI in USDC
    MIN_MARKETS_FOR_OI_FILTER = int(os.getenv("MIN_MARKETS_FOR_OI_FILTER", "2"))  # Require at least N markets

    # Telegram Notifications
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    TELEGRAM_TOPIC_ID = os.getenv("TELEGRAM_TOPIC_ID")  # Optional: for groups with topics
    TELEGRAM_ENABLE_NOTIFICATIONS = os.getenv("TELEGRAM_ENABLE_NOTIFICATIONS", "true").lower() == "true"

    # Position Monitoring (for real-time PnL tracking)
    # IMPORTANT: Aggressive monitoring uses many API calls!
    # Standard accounts have only 10 req/min limit - monitoring disabled by default
    # Premium accounts have 4000 req/min - can enable with shorter intervals
    if IS_PREMIUM:
        # Premium: Can afford frequent monitoring (5-10 seconds)
        ENABLE_POSITION_MONITORING = os.getenv("ENABLE_POSITION_MONITORING", "true").lower() == "true"
        POSITION_MONITOR_INTERVAL = float(os.getenv("POSITION_MONITOR_INTERVAL", "10.0"))  # 10 seconds safe
    else:
        # Standard: Disabled by default to respect rate limits
        # If enabled, use very long intervals (60-120 seconds minimum)
        ENABLE_POSITION_MONITORING = os.getenv("ENABLE_POSITION_MONITORING", "false").lower() == "true"
        POSITION_MONITOR_INTERVAL = float(os.getenv("POSITION_MONITOR_INTERVAL", "90.0"))  # 90 seconds safe

    # API Caching (to reduce API calls and respect rate limits)
    # Premium accounts can use shorter TTLs, standard accounts need longer TTLs
    if IS_PREMIUM:
        MARKET_DATA_CACHE_TTL = float(os.getenv("MARKET_DATA_CACHE_TTL", "30"))  # 30 seconds
        PRICE_CACHE_TTL = float(os.getenv("PRICE_CACHE_TTL", "5"))  # 5 seconds
    else:
        # Standard: Longer caching to minimize API usage
        MARKET_DATA_CACHE_TTL = float(os.getenv("MARKET_DATA_CACHE_TTL", "120"))  # 2 minutes
        PRICE_CACHE_TTL = float(os.getenv("PRICE_CACHE_TTL", "30"))  # 30 seconds

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
        "HYPE": 24
    }

    @classmethod
    def validate(cls):
        """Validate configuration for dual account setup"""
        # Check if dual account mode or legacy mode
        has_dual_accounts = cls.ACCOUNT_1_PRIVATE_KEY and cls.ACCOUNT_2_PRIVATE_KEY
        has_legacy = cls.LEGACY_API_KEY_PRIVATE_KEY

        if not has_dual_accounts and not has_legacy:
            raise ValueError(
                "Either dual accounts (LIGHTER_ACCOUNT_1_PRIVATE_KEY + LIGHTER_ACCOUNT_2_PRIVATE_KEY) "
                "or legacy single account (LIGHTER_API_KEY_PRIVATE_KEY) is required"
            )

        if has_dual_accounts:
            if not cls.ACCOUNT_1_PRIVATE_KEY:
                raise ValueError("LIGHTER_ACCOUNT_1_PRIVATE_KEY is required for dual account mode")
            if not cls.ACCOUNT_2_PRIVATE_KEY:
                raise ValueError("LIGHTER_ACCOUNT_2_PRIVATE_KEY is required for dual account mode")

        # Validate trading tokens
        for token in cls.TRADING_TOKENS:
            if token not in cls.MARKET_INDICES:
                raise ValueError(f"Unknown token: {token}")

        # Validate variance is reasonable
        if cls.TRADE_AMOUNT_VARIANCE_PERCENT > 10:
            raise ValueError("TRADE_AMOUNT_VARIANCE_PERCENT should not exceed 10%")

    @classmethod
    def is_dual_account_mode(cls) -> bool:
        """Check if running in dual account (hedged) mode"""
        return bool(cls.ACCOUNT_1_PRIVATE_KEY and cls.ACCOUNT_2_PRIVATE_KEY)