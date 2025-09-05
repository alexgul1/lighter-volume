# Lighter Futures Trading Bot

Automated futures trading bot for Lighter Protocol. Opens and closes long/short positions to maximize volume during the zero-fee beta period.

## Key Features

- **Futures Trading**: Opens both LONG and SHORT positions randomly
- **Automatic Position Management**: Opens positions and closes them after 2-5 seconds
- **Leverage Control**: Sets configurable leverage (default 3x) at startup
- **Smart Timing**: Configurable delays between trades and position hold times
- **MongoDB Logging**: Complete audit trail of all positions
- **Zero Fees**: Optimized for standard accounts with 0% fees during beta

## How It Works

1. **Set Leverage**: On startup, sets leverage for all configured markets
2. **Open Position**: Randomly selects token and direction (long/short)
3. **Hold Position**: Waits 2-5 seconds (configurable)
4. **Close Position**: Automatically closes with opposite order
5. **Repeat**: Waits configured delay, then opens next position

## Configuration (.env)

```env
# API Keys (REQUIRED)
LIGHTER_API_KEY_PRIVATE_KEY=your_api_key_here
LIGHTER_ETH_PRIVATE_KEY=your_eth_private_key_here
LIGHTER_ACCOUNT_INDEX=1
LIGHTER_API_KEY_INDEX=2

# Trading Settings
MIN_TRADE_AMOUNT_USDC=10.0
MAX_TRADE_AMOUNT_USDC=50.0
TRADING_TOKENS=ETH,BTC,SOL
DEFAULT_LEVERAGE=3

# Position Timing
POSITION_HOLD_TIME_MIN=2
POSITION_HOLD_TIME_MAX=5
DELAY_BETWEEN_TRADES=3