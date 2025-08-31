# Lighter Trading Bot - Maximum Efficiency Edition

Optimized trading bot for Lighter Protocol's zero-fee beta on standard accounts. Maximizes swap frequency while respecting strict API limits.

## ⚡ Key Features

- **Maximum Efficiency**: Batch transactions (buy+sell in single API call)
- **Zero API Waste**: No price checks, no balance queries, minimal API usage
- **Standard Account Optimized**: ~9 swaps/minute (18 trades) on standard account
- **Premium Account Ready**: Can switch to premium for 4000+ swaps/minute
- **100% Slippage Tolerance**: Trades execute at any price (high liquidity tokens only)
- **MongoDB Logging**: Full audit trail of all transactions
- **Docker Ready**: Easy deployment with docker-compose

## 🚀 Performance

### Standard Account (60 weighted requests/minute)
- **Max theoretical**: 10 batches/minute (20 trades)
- **Safe operation**: 9 batches/minute (18 trades)
- **Daily volume**: ~25,920 trades

### Premium Account (24,000 weighted requests/minute)  
- **Max theoretical**: 4,000 batches/minute (8,000 trades)
- **Safe operation**: 3,600 batches/minute (7,200 trades)
- **Daily volume**: ~10,368,000 trades

## ⚠️ Risk Disclaimer

**THIS BOT USES 100% SLIPPAGE TOLERANCE**
- Trades execute at ANY market price
- Only use with high liquidity tokens (ETH, BTC, SOL)
- You WILL experience slippage losses
- This is designed for beta farming, not profit
- USE AT YOUR OWN RISK

## 📋 Prerequisites

- Python 3.11+
- MongoDB 7.0+
- Lighter account with API keys
- USDC balance for trading

## 🔧 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd lighter-trading-bot
pip install -r requirements.txt