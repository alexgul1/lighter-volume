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