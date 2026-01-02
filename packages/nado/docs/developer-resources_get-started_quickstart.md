---
url: https://docs.nado.xyz/developer-resources/get-started/quickstart
title: ⚡Quickstart
---

- Developer Resources
[Developer Resources](/developer-resources)
- 🚀Get Started
[🚀Get Started](/developer-resources/get-started)

# ⚡Quickstart

Goal:Get from zero to your first trade on Nado in ~5 minutes.

This guide assumes you have basic blockchain knowledge and want to jump straight in. For deeper understanding, seeCore Concepts.

[Core Concepts](/developer-resources/get-started/core-concepts)

## ✅ Prerequisites

Before you start, make sure you have:

- Ink wallet with private key(any EVM-compatible wallet works)

Ink wallet with private key(any EVM-compatible wallet works)

- Ink Sepolia ETH for gas- Get free testnet ETH fromInk Faucet

Ink Sepolia ETH for gas- Get free testnet ETH fromInk Faucet

[Ink Faucet](https://docs.inkonchain.com/tools/faucets)
- Testnet USDT0(≥ $5) - Mint free tokens fromNado Testnet Faucet

Testnet USDT0(≥ $5) - Mint free tokens fromNado Testnet Faucet

[Nado Testnet Faucet](https://testnet.nado.xyz/portfolio/faucet)

This guide uses Testnet (Ink Sepolia)for safe learning without real funds.

Get testnet tokens:

- Gas (Ink Sepolia ETH):Ink Faucet- Free testnet ETH for transaction fees

Gas (Ink Sepolia ETH):Ink Faucet- Free testnet ETH for transaction fees

[Ink Faucet](https://docs.inkonchain.com/tools/faucets)
- Trading funds (USDT0, KBTC, etc.):Nado Testnet Faucet- Mint testnet tokens

Trading funds (USDT0, KBTC, etc.):Nado Testnet Faucet- Mint testnet tokens

[Nado Testnet Faucet](https://testnet.nado.xyz/portfolio/faucet)

When ready for real trading, use Mainnet (Ink) and replacetestnetwithmainnetin all examples.

`testnet`
`mainnet`

## 📦 Step 1: Install SDK (2 minutes)

Choose your preferred language and install the SDK:

Verify installation:

Verify installation:

Or manually add to Cargo.toml:

Verify installation:

## 🌐 Step 2: Connect to Nado (30 seconds)

Create a client and verify connection:

Security:Never commit private keys to git! Use environment variables:

- Python:os.getenv('PRIVATE_KEY')

Python:os.getenv('PRIVATE_KEY')

`os.getenv('PRIVATE_KEY')`
- TypeScript:process.env.PRIVATE_KEY

TypeScript:process.env.PRIVATE_KEY

`process.env.PRIVATE_KEY`
- Rust:std::env::var("PRIVATE_KEY")

Rust:std::env::var("PRIVATE_KEY")

`std::env::var("PRIVATE_KEY")`

## 💰 Step 3: Create Subaccount (Deposit Funds) (1 minute)

Subaccounts are created automatically on your first deposit. You need≥ $5 USDT0to create a subaccount.

Multiple deposit methods available:

- UI Faucet(easiest for testnet - shown below)

UI Faucet(easiest for testnet - shown below)

- Direct Deposit(send tokens to your unique deposit address)

Direct Deposit(send tokens to your unique deposit address)

- Smart Contract(on-chain depositCollateral call)

Smart Contract(on-chain depositCollateral call)

See theDepositing Guidefor all methods and advanced options.

[Depositing Guide](/developer-resources/api/depositing)

### Option A: Deposit via UI (Easiest)

For Testnet (Ink Sepolia):

- Go toNado Testnet Faucet

Go toNado Testnet Faucet

[Nado Testnet Faucet](https://testnet.nado.xyz/portfolio/faucet)
- Connect your wallet (make sure you're on Ink Sepolia network)

Connect your wallet (make sure you're on Ink Sepolia network)

- Mint testnet USDT0 (click "Mint" button - free!)

Mint testnet USDT0 (click "Mint" button - free!)

- Go toTestnet Tradingand verify your balance

Go toTestnet Tradingand verify your balance

[Testnet Trading](https://testnet.nado.xyz)
- You're ready to trade! (subaccount created automatically)

You're ready to trade! (subaccount created automatically)

For Mainnet (Ink):

- Go toNado Mainnet

Go toNado Mainnet

[Nado Mainnet](https://nado.xyz)
- Connect your wallet (make sure you're on Ink Mainnet network)

Connect your wallet (make sure you're on Ink Mainnet network)

- Click "Deposit" and follow the UI instructions

Click "Deposit" and follow the UI instructions

- Send ≥ $5 USDT0 to complete deposit

Send ≥ $5 USDT0 to complete deposit

- Subaccount created automatically

Subaccount created automatically

### Option B: Deposit via SDK

Wait time:Deposits take ~5-10 seconds on Ink Sepolia testnet. Querysubaccount_infoto check when your subaccount is created.

`subaccount_info`

## 📈 Step 4: Place Your First Order (1 minute)

Now let's place a simple limit order on BTC-PERP:

Congratulations!🎉 You just placed your first order on Nado! The order is a limit buy 1% below market, so it likely won't fill immediately (it'll rest on the order book).

## ✅ Step 5: Verify Your Order

Check that your order was accepted and is on the order book:

## 🎯 What You Just Did

In just 5 minutes, you:

- ✅ Installed the Nado SDK

✅ Installed the Nado SDK

- ✅ Connected to Nado testnet (Ink Sepolia)

✅ Connected to Nado testnet (Ink Sepolia)

- ✅ Created a subaccount (via deposit)

✅ Created a subaccount (via deposit)

- ✅ Placed a limit order on BTC-PERP

✅ Placed a limit order on BTC-PERP

- ✅ Verified the order is on the book

✅ Verified the order is on the book

## 🚀 Next Steps

### Learn More

- Core Concepts- Deep dive into authentication, subaccounts, linked signers, and signing

Core Concepts- Deep dive into authentication, subaccounts, linked signers, and signing

[Core Concepts](/developer-resources/get-started/core-concepts)
- First Deposit- Detailed deposit guide with multiple methods

First Deposit- Detailed deposit guide with multiple methods

[First Deposit](/developer-resources/get-started/first-deposit)
- Linked Signers Guide- Set up 1-Click Trading and secure bot keys

Linked Signers Guide- Set up 1-Click Trading and secure bot keys

[Linked Signers Guide](/developer-resources/get-started/linked-signers)

### Keep Building

- First Trade- Advanced order types and trading strategies

First Trade- Advanced order types and trading strategies

[First Trade](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/get-started/first-trade.md)
- API Reference- Complete API documentation

API Reference- Complete API documentation

[API Reference](/developer-resources/api)
- Common Errors- Troubleshoot signature errors and deposit issues

Common Errors- Troubleshoot signature errors and deposit issues

[Common Errors](/developer-resources/get-started/common-errors)

### SDK Documentation

- Python SDK- Full Python SDK docs

Python SDK- Full Python SDK docs

[Python SDK](https://nadohq.github.io/nado-python-sdk/index.html)
- TypeScript SDK- Complete TypeScript SDK guide

TypeScript SDK- Complete TypeScript SDK guide

[TypeScript SDK](/developer-resources/typescript-sdk)
- Rust SDK- Rust SDK on crates.io

Rust SDK- Rust SDK on crates.io

[Rust SDK](https://crates.io/crates/nado-sdk)

## 💡 Pro Tips

### Cancel Your Test Order

If you want to cancel the order you just placed:

### Place a Market Order (Fills Immediately)

Want instant execution? Use a market order by setting an aggressive price:

## 🆘 Troubleshooting

### "Signature does not match" Error

SeeCommon Errors: Error 2028for detailed troubleshooting.

[Common Errors: Error 2028](/developer-resources/get-started/common-errors#error-2028-signature-does-not-match-with-senders-or-linked-signers)

Quick fix:Verify you're using the correct private key and connected to testnet (Ink Sepolia).

### "Subaccount does not exist" Error

SeeCommon Errors: Error 2024for detailed troubleshooting.

[Common Errors: Error 2024](/developer-resources/get-started/common-errors#error-2024-provided-address-has-no-previous-deposits)

Quick fix:Make sure you deposited ≥ $5 USDT0 and waited for confirmation.

### Need Help?

- Telegram Community:Join our Telegram

Telegram Community:Join our Telegram

[Join our Telegram](https://t.me/+whsZJKpiiVwwNjQ0)
- Submit a ticket:Nado Support

Submit a ticket:Nado Support

[Nado Support](https://nado-90114.zendesk.com/hc/en-us/requests/new?ticket_form_id=52275013155481)

You're ready to trade!🎉

This quickstart got you up and running. For production use, read theCore ConceptsandLinked Signersguides to understand best practices and security considerations.

[Core Concepts](/developer-resources/get-started/core-concepts)
[Linked Signers](/developer-resources/get-started/linked-signers)
[PreviousGet Started](/developer-resources/get-started)
[NextCore Concepts](/developer-resources/get-started/core-concepts)

Last updated9 days ago