# Nado Token Rotation Bot

Fast token rotation trading bot for [nado.xyz](https://nado.xyz) DEX. Opens and closes positions rapidly to generate trading volume.

## Features

- **Official SDK**: Uses `nado-protocol` Python SDK
- **Fast Rotation**: Opens position → holds briefly → closes → repeat
- **Multi-Product**: Trade multiple perpetual markets (ETH, BTC, SOL, etc.)
- **Telegram Notifications**: Real-time alerts with topic support
- **Telegram Commands**: Interactive `/status`, `/balance`, `/stats`, `/help`
- **Rate Limit Aware**: Configurable delays to respect API limits

## Requirements

- Python 3.10+
- Nado account with USDT0 deposited
- PM2 (optional, for production)

## Installation

```bash
cd packages/nado

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials
```

## Configuration

Edit `.env` file:

```env
# Required
NADO_PRIVATE_KEY=0x...  # Your wallet private key
NADO_NETWORK=mainnet    # mainnet, testnet, or devnet

# Trading
NADO_TRADING_PRODUCTS=2,4          # 2=ETH, 4=BTC
NADO_MIN_TRADE_AMOUNT=10.0         # Min trade size in USD
NADO_MAX_TRADE_AMOUNT=50.0         # Max trade size in USD
NADO_HOLD_TIME_MIN=5.0             # Min hold time (seconds)
NADO_HOLD_TIME_MAX=30.0            # Max hold time (seconds)

# Telegram (optional)
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=-1001234567890
TELEGRAM_TOPIC_ID=123              # For supergroups with topics
```

### Product IDs

| ID | Product |
|----|---------|
| 0  | USDT0 (collateral) |
| 2  | ETH-PERP |
| 3  | SOL-PERP |
| 4  | BTC-PERP |
| 5  | BNB-PERP |
| 6  | XRP-PERP |

## Usage

### Manual Run

```bash
# Activate virtual environment
source venv/bin/activate

# Run bot
python main.py
```

### PM2 (Production)

```bash
# Create logs directory
mkdir -p logs

# Start with PM2
pm2 start ecosystem.config.js

# View logs
pm2 logs nado-bot

# Monitor
pm2 monit

# Stop
pm2 stop nado-bot

# Restart
pm2 restart nado-bot

# Remove from PM2
pm2 delete nado-bot
```

### PM2 Startup (Auto-start on boot)

```bash
# Generate startup script
pm2 startup

# Save current process list
pm2 save
```

## Telegram Setup

1. **Create Bot**: Message [@BotFather](https://t.me/BotFather), send `/newbot`
2. **Get Chat ID**:
   - Send message to bot
   - Visit: `https://api.telegram.org/bot<TOKEN>/getUpdates`
   - Find `"chat":{"id":...}`
3. **Topic ID** (for supergroups):
   - Right-click topic → Copy link
   - Extract number after last `/` (e.g., `-1001234567890/123` → topic is `123`)

### Telegram Commands

| Command | Description |
|---------|-------------|
| `/status` | Bot status, balance, stats |
| `/balance` | Account balance and health |
| `/stats` | Trading statistics |
| `/help` | Show commands |

## Rate Limits

Nado has rate limits based on `spot_leverage` setting:

| Setting | Rate Limit | Recommended Delay |
|---------|-----------|-------------------|
| `spot_leverage=true` | 600 orders/min | 0.12s |
| `spot_leverage=false` | 30 orders/min | 2.2s |

The bot uses `spot_leverage=true` by default for faster operation.

## Project Structure

```
packages/nado/
├── main.py              # Entry point
├── ecosystem.config.js  # PM2 configuration
├── requirements.txt     # Python dependencies
├── .env.example         # Configuration template
├── src/
│   ├── config.py        # Configuration loader
│   ├── trading_engine.py    # Trading logic
│   └── telegram_notifier.py # Telegram integration
├── docs/
│   └── sdk/             # SDK documentation
└── logs/                # Log files (created by PM2)
```

## Troubleshooting

### "Subaccount does not exist"
Deposit at least $5 USDT0 to your Nado account first.

### Rate limit errors
Increase `NADO_DELAY_BETWEEN_TRADES` or set `NADO_USE_SPOT_LEVERAGE=true`.

### Telegram not working
1. Check bot token is correct
2. Ensure bot is added to chat/group
3. For topics: bot must have permission to post in topic

## License

MIT
