---
url: https://docs.nado.xyz/developer-resources/get-started/first-deposit
title: 💰First Deposit
---

- Developer Resources
[Developer Resources](/developer-resources)
- 🚀Get Started
[🚀Get Started](/developer-resources/get-started)

# 💰First Deposit

Step-by-step guide to make your first deposit on Nado

TL;DR: You need >= $5 USDT0 to create a subaccount. Three methods: (1)UI Deposit(easiest - start here!), (2)On-Chain Contract Call(recommended for developers), or (3)Direct Deposit(alternative, requires caution). We recommend starting on testnet with free faucet tokens!

## 📋 Prerequisites

Before depositing, you'll need:

- A wallet with a private key

A wallet with a private key

- Funds to deposit:Testnet: Free tokens fromNado Testnet FaucetMainnet: >= $5 USDT0 or equivalent

Funds to deposit:

- Testnet: Free tokens fromNado Testnet Faucet

Testnet: Free tokens fromNado Testnet Faucet

[Nado Testnet Faucet](https://testnet.nado.xyz/portfolio/faucet)
- Mainnet: >= $5 USDT0 or equivalent

Mainnet: >= $5 USDT0 or equivalent

- Gas for transaction fees:Testnet: Free Ink Sepolia ETH fromInk FaucetMainnet: Ink ETH

Gas for transaction fees:

- Testnet: Free Ink Sepolia ETH fromInk Faucet

Testnet: Free Ink Sepolia ETH fromInk Faucet

[Ink Faucet](https://docs.inkonchain.com/tools/faucets)
- Mainnet: Ink ETH

Mainnet: Ink ETH

Starting on testnet?You can get both testnet USDT0 (for trading) and Ink Sepolia ETH (for gas) completely free from the faucets above. This is the recommended way to learn!

## 🎯 Why You Need to Deposit

On Nado,subaccounts are created automatically when you make your first deposit(>= $5 USDT0). Unlike centralized exchanges, there's no separate "account creation" step - depositing funds creates your subaccount.

Important: Subaccounts don't exist until you deposit. If you try to query a subaccount before depositing, you'll get"exists": false.

`"exists": false`

## 🚀 Method 1: UI Deposit (Easiest)

This is therecommended method for getting started- use the Nado web interface. Perfect for your first deposit!

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

- Send >= $5 USDT0 to complete deposit

Send >= $5 USDT0 to complete deposit

- Subaccount created automatically

Subaccount created automatically

Why start here?The UI handles all the complexity - approvals, contract calls, and verification. This is the safest method.

## ⚙️ Method 2: On-Chain Contract Call (Recommended for Developers)

This is therecommended method for programmatic deposits. Call the Endpoint contract directly to deposit funds.

### Step 1: Get Contract Addresses

### Step 2: Approve Token Allowance and Deposit

### Step 3: Verify Your Deposit

Wait ~30 seconds for blockchain confirmation, then check if your subaccount was created:

Success!Ifexists: true, your subaccount is ready and you can start trading! 🎉

`exists: true`

## 🔄 Method 3: Direct Deposit (Alternative)

Each subaccount has a unique deposit address. You can send funds directly to this address and they will automatically be credited.

⚠️ Use with Caution: This method is the easiest but requires extreme care.Only send supported tokens- sending unsupported tokens will result in permanent loss of funds. We recommend using Method 1 (UI) or Method 2 (On-Chain) instead.

### Step 1: Get Your Direct Deposit Address

### Step 2: Verify Supported Tokens (CRITICAL)

Before sending any funds,you MUST verify the token is supported:

### Step 3: Send Funds Directly (From Any Wallet)

That's it!Just send the supported token to your direct deposit address:

- From MetaMask: Send transaction to the deposit address

From MetaMask: Send transaction to the deposit address

- From CEX: Withdraw to the deposit address (use correct network!)

From CEX: Withdraw to the deposit address (use correct network!)

- From another wallet: Transfer tokens to the deposit address

From another wallet: Transfer tokens to the deposit address

The funds will be automatically credited to your Nado subaccountwithin ~30 seconds.

CRITICAL WARNINGS:

- ⚠️ONLY send supported tokens(verify with Step 2 above)

⚠️ONLY send supported tokens(verify with Step 2 above)

- ⚠️Use the correct network: Ink Mainnet or Ink Sepolia Testnet

⚠️Use the correct network: Ink Mainnet or Ink Sepolia Testnet

- ⚠️Sending wrong tokens = permanent loss- no refunds possible

⚠️Sending wrong tokens = permanent loss- no refunds possible

- ⚠️Double-check before sending- you cannot undo this

⚠️Double-check before sending- you cannot undo this

### Step 4: Verify Your Deposit

Use the same verification code from Method 2, Step 4 to confirm your subaccount was created and has the deposited balance.

## 🎁 Testnet Faucet

New to Nado?Start on testnet with free tokens!

- Get Free Testnet USDT0:https://testnet.nado.xyz/portfolio/faucet

Get Free Testnet USDT0:https://testnet.nado.xyz/portfolio/faucet

- Get Free Ink Sepolia ETH(for gas):Ink Faucet

Get Free Ink Sepolia ETH(for gas):Ink Faucet

[Ink Faucet](https://docs.inkonchain.com/tools/faucets)

## 🤔 Which Method Should I Use?

UI Deposit

First-time users, getting started quickly

Safest, handles everything

Requires web interface

On-Chain Contract

Developers, bots, programmatic deposits

Type-safe, explicit, fails early

Requires code

Direct Deposit

CEX withdrawals, simple transfers

No contract calls, works with any wallet

Risk of sending wrong token

Recommendation: Start withMethod 1 (UI)to get familiar, then useMethod 2 (On-Chain)for your production bots and applications.

## 🆘 Troubleshooting

### Subaccount not created

Possible causes:

- Deposit amount < $5 USDT0 minimum

Deposit amount < $5 USDT0 minimum

- Transaction still confirming (wait 30-60 seconds)

Transaction still confirming (wait 30-60 seconds)

- Wrong token sent (if using direct deposit)

Wrong token sent (if using direct deposit)

Debug steps:

- Check transaction status on block explorer

Check transaction status on block explorer

- Verify balance with the verification code above

Verify balance with the verification code above

- CheckCommon Errorsfor help

CheckCommon Errorsfor help

[Common Errors](/developer-resources/get-started/common-errors)

### Transaction failed

Possible causes:

- Insufficient gas

Insufficient gas

- Token allowance not approved (Method 2 only)

Token allowance not approved (Method 2 only)

- Wrong product ID or amount

Wrong product ID or amount

Solution: Review error message and check your parameters

## 🎯 Next Steps

Now that you have funds deposited, you're ready to trade!

- 📈Place Your First Order- Start trading

📈Place Your First Order- Start trading

[Place Your First Order](/developer-resources/api/gateway/executes/place-order)
- 🔗Set Up Linked Signers- Enable 1-Click Trading

🔗Set Up Linked Signers- Enable 1-Click Trading

[Set Up Linked Signers](/developer-resources/get-started/linked-signers)
- 📖Read Core Concepts- Understand how Nado works

📖Read Core Concepts- Understand how Nado works

[Read Core Concepts](/developer-resources/get-started/core-concepts)

Success!You've completed your first deposit. Happy trading! 🎉

[PreviousCore Concepts](/developer-resources/get-started/core-concepts)
[NextLinked Signers](/developer-resources/get-started/linked-signers)

Last updated9 days ago