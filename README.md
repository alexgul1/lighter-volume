# Lighter Hedged Futures Trading Bot

Automated hedged futures trading bot for Lighter Protocol. Uses dual accounts to open opposing long/short positions on low open interest tokens to maximize farming rewards while minimizing directional risk.

## Key Features

- **Hedged Trading Strategy**: Opens paired long/short positions across two accounts
- **Low OI Targeting**: Automatically selects tokens with low open interest (better rewards)
- **Proper Price Calculation**: Uses real market prices from API for accurate base_amount calculation
- **Risk Mitigation**: Hedges directional risk by opening opposing positions
- **Randomized Entry**: Adds variance in timing (1-5s) and amounts (±2%) to avoid exact matching
- **Long Hold Times**: Positions held for 1-3 hours for sustained farming
- **Dual Account Support**: Manages two separate accounts with independent nonces and order indices
- **Automatic Position Management**: Opens hedged pairs and closes them after hold time
- **Leverage Control**: Sets configurable leverage (default 3x) on both accounts
- **MongoDB Logging**: Complete audit trail of all positions
- **Automatic Recovery**: Pauses and restarts on consecutive failures
- **Telegram Notifications**: Real-time alerts for trades, positions, P/L, and errors
- **Position Monitoring**: Optional P/L tracking via REST polling (adaptive intervals)
- **Hedged Pair P/L Tracking**: Calculates combined profit/loss for paired positions
- **Rate Limit Aware**: Adaptive caching and polling based on account type (standard vs premium)

## How It Works

1. **Initialize Dual Accounts**: Connects to Account 1 and Account 2 with separate credentials
2. **Set Leverage**: Sets leverage for all configured markets on both accounts
3. **Select Low OI Tokens**: Fetches order book details and selects tokens with lowest open interest
4. **Open Hedged Pair**:
   - Gets current market price and calculates proper base_amount
   - Randomizes which account opens long vs short
   - Opens first position
   - Waits random delay (1-5 seconds)
   - Opens second position with opposite direction and slightly different amount
5. **Hold Positions**: Waits 1-3 hours (configurable)
6. **Close Pair**: Automatically closes both positions
7. **Repeat**: Selects next low OI token and opens new hedged pair

## Hedging Strategy Benefits

- **No Directional Risk**: Long and short positions offset price movements
- **Double Rewards**: Earns farming points from both accounts
- **Low OI Focus**: Targets tokens with lower competition for better rewards
- **Variance Protection**: Slight differences in amounts and timing reduce correlation

## Configuration (.env)

See `.env.example` for all available options.

### Required Configuration

```env
# Account 1 (Primary)
LIGHTER_ACCOUNT_1_PRIVATE_KEY=your_account_1_api_key_private_key
LIGHTER_ACCOUNT_1_INDEX=1
LIGHTER_ACCOUNT_1_API_KEY_INDEX=2

# Account 2 (Secondary)
LIGHTER_ACCOUNT_2_PRIVATE_KEY=your_account_2_api_key_private_key
LIGHTER_ACCOUNT_2_INDEX=1
LIGHTER_ACCOUNT_2_API_KEY_INDEX=2

# Trading Settings
MIN_TRADE_AMOUNT_USDC=10.0
MAX_TRADE_AMOUNT_USDC=50.0
TRADING_TOKENS=ETH,BTC,SOL
DEFAULT_LEVERAGE=3

# Position Timing (in seconds)
POSITION_HOLD_TIME_MIN=3600   # 1 hour
POSITION_HOLD_TIME_MAX=10800  # 3 hours
DELAY_BETWEEN_TRADES=10

# Telegram Notifications (optional)
TELEGRAM_BOT_TOKEN=your_bot_token_from_@BotFather
TELEGRAM_CHAT_ID=your_chat_id_or_group_id
TELEGRAM_TOPIC_ID=  # Optional: for groups with topics
TELEGRAM_ENABLE_NOTIFICATIONS=true

# Account Type - IMPORTANT for rate limits!
ACCOUNT_TYPE=standard  # or "premium"

# Position Monitoring
# WARNING: Uses many API calls! Disabled by default for standard accounts
ENABLE_POSITION_MONITORING=false  # Set to "true" only if you understand rate limits
POSITION_MONITOR_INTERVAL=90.0  # 90s for standard, 10s for premium
```

## Telegram Setup

The bot can send real-time notifications to Telegram about trading activity:

1. **Create a Bot:**
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` and follow instructions
   - Copy the bot token

2. **Get Chat ID:**
   - For private messages: Send a message to your bot, then visit:
     `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - For groups: Add bot to group, send a message, use same URL
   - Look for `"chat":{"id":...}` in the response

3. **Optional - Topic ID:**
   - For groups with topics/forums enabled
   - Right-click on topic → Copy link → Extract topic ID from URL
   - Format: `-1001234567890/12345` (the `12345` is the topic ID)

4. **Configure:**
   - Add `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` to `.env`
   - Optionally add `TELEGRAM_TOPIC_ID` for topic-specific messages

### Notification Types

The bot sends notifications for:
- **Position Opened**: Token, type (long/short), size, price, OI
- **Hedged Pair Opened**: Both positions with full details
- **Position Closed**: P/L, hold time, price change
- **Hedged Pair Closed**: Combined P/L for both positions
- **Errors**: Trading errors, API failures
- **Restart Events**: Bot restarts and recovery
- **Summary**: Periodic trading statistics

### Example Notification

```
🎯 Hedged Pair Opened

Token: SOL
Price: $98.45
Open Interest: $234,567
Total Size: $50.00

📈 Position 1 (LONG):
  Account: 1
  Size: $25.50
  ID: a1b2c3d4

📉 Position 2 (SHORT):
  Account: 2
  Size: $24.50
  ID: e5f6g7h8

⏰ 2025-11-18 20:30:45 UTC
```

## API Rate Limits ⚠️

**CRITICAL:** Lighter Protocol has strict API rate limits that vary by account type:

| Account Type | Rate Limit | Safe Delay |
|--------------|-----------|------------|
| **Standard (Free)** | 10 requests/minute | 7 seconds |
| **Premium** | 4000 requests/minute | 0.5 seconds |

### Rate Limit Considerations

**For Standard Accounts:**
- Position monitoring is **DISABLED by default** (uses too many API calls)
- If enabled, use minimum 90-second polling intervals
- Market data cache: 120 seconds (2 minutes)
- Price cache: 30 seconds
- Expect slower operation but within rate limits

**For Premium Accounts:**
- Position monitoring **ENABLED by default**
- Can use 10-second polling intervals safely
- Market data cache: 30 seconds
- Price cache: 5 seconds
- Near real-time monitoring available

**API Call Estimation:**

Standard account budget: **10 calls/minute**
- Position monitor (if enabled): 2-4 calls per cycle
- Market data refresh: 1 call per token
- Trading operations: 2-4 calls per position open/close

With monitoring disabled and proper caching, standard accounts stay well within limits.

### Configuring for Your Account Type

Set `ACCOUNT_TYPE=premium` in `.env` if you have a premium account. This will automatically:
- Enable position monitoring with optimal intervals
- Use shorter cache TTLs for fresher data
- Allow faster trading operations

## Position Monitoring

The bot can monitor open positions via REST API polling:

- **Real-time P/L**: Tracks unrealized profit/loss
- **Liquidation Risk**: Warns when price approaches liquidation
- **Price Updates**: Fetches latest market prices
- **Hedged Pair Tracking**: Calculates combined P/L for paired positions

**Important:** Since Lighter Protocol doesn't support WebSockets, monitoring uses REST polling which consumes API rate limit. For standard accounts, this feature is disabled by default. Enable only if you understand the rate limit implications.