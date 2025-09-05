# Lighter Protocol Trading Bot
## Enhanced with WebSocket Position Monitoring & Automatic TP/SL

### Key Enhancements

#### 1. **WebSocket Position Monitoring**
- Real-time subscription to `account_all/{ACCOUNT_INDEX}` channel
- Receives live position updates including average entry price, position value, and PnL
- Automatic reconnection on disconnect

#### 2. **Automatic Take Profit / Stop Loss**
- Sets TP/SL orders immediately after receiving position confirmation via WebSocket
- Configurable percentages (supports 0.00001 to 1.0)
- Uses TAKE_PROFIT_LIMIT and STOP_LOSS_LIMIT order types
- Automatically cancels TP/SL orders before closing positions

#### 3. **Per-Token Cooldown System**
- Independent cooldown timer for each token
- Prevents opening new positions for X seconds after closing
- Allows parallel trading (e.g., BTC can trade while ETH is in cooldown)

#### 4. **Time-Based Position Closing**
- Configurable maximum hold time (MAX_HOLD_SECONDS)
- Automatically closes positions that haven't hit TP/SL within time limit
- Runs in parallel with normal trading logic

### Configuration

Create a `.env` file with the following parameters:

```env
# API Keys (Required)
LIGHTER_API_KEY_PRIVATE_KEY=your_api_key
LIGHTER_ETH_PRIVATE_KEY=your_eth_key
LIGHTER_ACCOUNT_INDEX=1
LIGHTER_API_KEY_INDEX=2

# Trading Parameters
TRADING_TOKENS=ETH,BTC,SOL
MIN_TRADE_AMOUNT_USDC=10.0
MAX_TRADE_AMOUNT_USDC=50.0
DEFAULT_LEVERAGE=3

# TP/SL Configuration (as decimals)
TP_PERCENT=0.001  # 0.1%
SL_PERCENT=0.001  # 0.1%

# Timing Configuration
POSITION_HOLD_TIME_MIN=2  # Min seconds
POSITION_HOLD_TIME_MAX=5  # Max seconds
MAX_HOLD_SECONDS=300  # Force close after 5 minutes
DELAY_BETWEEN_TRADES=3  # Per-token cooldown

# MongoDB
MONGODB_URI=mongodb://localhost:27017
MONGODB_DATABASE=lighter_bot
```

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py
```

### How It Works

1. **Position Opening**
   - Bot checks which tokens are not in cooldown
   - Opens random long/short positions with market orders
   - Stores position in memory with unique ID

2. **WebSocket Monitoring**
   - Receives position update with average entry price
   - Calculates TP price: entry ± TP_PERCENT
   - Calculates SL price: entry ± SL_PERCENT
   - Places both orders automatically

3. **Position Closing** (Three ways)
   - **TP/SL Hit**: Position closes automatically via exchange
   - **Time Limit**: Force close after MAX_HOLD_SECONDS
   - **Random Hold**: Close after POSITION_HOLD_TIME_MIN/MAX

4. **Cooldown Management**
   - After closing, token enters cooldown for DELAY_BETWEEN_TRADES seconds
   - Other tokens can continue trading independently

### Database Schema

All trades are logged to MongoDB with:
- Transaction type (open/close)
- Position type (long/short)
- Token and amounts
- Order IDs and hashes
- Success/failure status
- Dependencies (close references open)

### Rate Limits

**Standard Account:**
- 60 weighted requests per minute
- sendTx weight: 6 (max 10 trades/minute)
- Safe delay: 7 seconds between trades

**Premium Account:**
- 4000 weighted requests per minute
- Lower latency for HFT
- Fees apply: 0.002% maker, 0.02% taker

### Safety Features

- Automatic position closing on shutdown
- Per-token position limits
- WebSocket auto-reconnection
- Nonce management for transaction ordering
- Comprehensive error logging

### Monitoring

The bot provides real-time statistics:
- Total positions opened
- Long vs Short distribution
- Total volume traded
- Positions per hour rate
- Individual position PnL (when available)

### Troubleshooting

1. **WebSocket Connection Issues**
   - Check auth token generation
   - Verify account index is correct
   - Ensure network connectivity

2. **TP/SL Not Setting**
   - Verify position updates are received
   - Check TP/SL percentages are valid
   - Ensure sufficient margin for orders

3. **Cooldown Not Working**
   - Check DELAY_BETWEEN_TRADES setting
   - Verify token tracking in memory
   - Review logs for timing issues

### Advanced Configuration

For very small TP/SL targets:
```env
TP_PERCENT=0.00001  # 0.001%
SL_PERCENT=0.00005  # 0.005%
```

For aggressive position management:
```env
MAX_POSITIONS_PER_TOKEN=5
MAX_HOLD_SECONDS=60  # 1 minute max
DELAY_BETWEEN_TRADES=1  # 1 second cooldown
```

### Architecture

```
main.py
├── bot.py (Main application controller)
├── trading_engine.py (Core trading logic + WebSocket)
├── database.py (MongoDB integration)
├── config.py (Configuration management)
└── utils.py (Logging and statistics)
```

### API Weight Usage

Per operation weight consumption:
- Open position: 6 (sendTx)
- Set TP order: 6 (sendTx)
- Set SL order: 6 (sendTx)
- Cancel order: 6 (sendTx)
- Close position: 6 (sendTx)

Total per position lifecycle: ~30 weight units

### Notes

- WebSocket provides real-time position data without polling
- TP/SL orders remain on exchange even if bot disconnects
- Database preserves full trading history for analysis
- Bot can recover from temporary disconnections
- Multiple instances should not share the same API key