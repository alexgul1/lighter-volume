---
url: https://docs.nado.xyz/developer-resources/get-started/linked-signers
title: 🔗Linked Signers
---

- Developer Resources
[Developer Resources](/developer-resources)
- 🚀Get Started
[🚀Get Started](/developer-resources/get-started)

# 🔗Linked Signers

TL;DR:Linked signers let you delegate trading permissions to a separate private key, keeping your main wallet secure. This is Nado's "1-Click Trading" feature.

This guide addresses the most common questions about linked signers.

## 🤔 What is a Linked Signer?

Alinked signeris a separate private key that you authorize to sign trading operations on behalf of your subaccount.

Think of it like this:

- Main wallet: Your master key (high value, kept secure)

Main wallet: Your master key (high value, kept secure)

- Linked signer: Delegated key (trading only, can be rotated)

Linked signer: Delegated key (trading only, can be rotated)

### Key Facts

- One per subaccount: Each subaccount can have exactly one linked signer

One per subaccount: Each subaccount can have exactly one linked signer

- Full permissions: Linked signer can do ANYTHING your main wallet can (trade, withdraw, etc.)

Full permissions: Linked signer can do ANYTHING your main wallet can (trade, withdraw, etc.)

- Optional: You don't need a linked signer - your main wallet always works

Optional: You don't need a linked signer - your main wallet always works

- UI's "1-Click Trading": This is just a linked signer with a random key

UI's "1-Click Trading": This is just a linked signer with a random key

Important: When you have a linked signer set, you can sign requests with EITHER your main wallet key OR the linked signer key. Both work.

## 🎯 Why Use a Linked Signer?

### 🔐 Security

Keep your main wallet (with all your assets) offline or in cold storage. Use a linked signer key only for trading on Nado.

Example: Your main wallet has $1M in assets. Create a linked signer for trading bots with only $10K exposure on Nado. If the bot key is compromised, attacker can only access your Nado subaccount (limited by what's deposited).

### 🤖 Programmatic Trading

Run trading bots without exposing your main wallet private key to servers.

Example: Deploy a market-making bot to a cloud server. Use a linked signer key instead of your main wallet key. If the server is compromised, you can revoke the linked signer and your main wallet remains safe.

### ⚡ Convenience (1-Click Trading)

The Nado UI's "1-Click Trading" feature generates a random linked signer key and stores it encrypted in your browser. This means:

- No MetaMask popup for every trade

No MetaMask popup for every trade

- Faster execution

Faster execution

- Same security (key never leaves your device)

Same security (key never leaves your device)

## 🛠️ How to Set Up a Linked Signer

Before you start: Your subaccount must exist (requires initial deposit >= $5 USDT0). SeeCore Conceptsif you haven't created a subaccount yet.

[Core Concepts](/developer-resources/get-started/core-concepts)

### Method 1: Via API (Recommended for Developers)

#### Step 1: Generate a New Private Key

#### Step 2: Link the Signer to Your Subaccount

Critical: This request must be signed with yourMAIN WALLETprivate key, not the linked signer key!

#### Step 3: Verify It Worked

### Method 2: Via UI (1-Click Trading)

This is the easiest method if you're just getting started:

- Go to Nado UI:app.nado.xyz

Go to Nado UI:app.nado.xyz

[app.nado.xyz](https://app.nado.xyz)
- Connect your wallet(MetaMask, WalletConnect, etc.)

Connect your wallet(MetaMask, WalletConnect, etc.)

- Open Settings(gear icon)

Open Settings(gear icon)

- Find "1-Click Trading"section

Find "1-Click Trading"section

- Click "Enable"

Click "Enable"

The UI will:

- Generate a random private key

Generate a random private key

- Link it to your default subaccount

Link it to your default subaccount

- Store it encrypted in your browser

Store it encrypted in your browser

- You're done!

You're done!

UI-generated vs API: If you enable 1-Click Trading in the UI, then later link a different signer via API, the UI's 1-Click Trading will break (it'll be using the old key). Seetroubleshooting below.

[troubleshooting below](/developer-resources/get-started/linked-signers#error-ui-1-click-trading-broken)

## 🔍 How to Check Your Current Linked Signer

### Via API

### Via Raw API Call

Response:

## ✍️ How to Sign Requests with Your Linked Signer

Once you've linked a signer, you have two options for signing trading requests:

### Option 1: Use Main Wallet Key (Always Works)

### Option 2: Use Linked Signer Key (Recommended for Trading Bots)

Critical Understanding: When using a linked signer, thesenderfield isALWAYS your main wallet's subaccount, but the signature comes from thelinked signer's private key. This is the core concept of linked signers.

`sender`

How linked signers work:

- Sender field: Always your main wallet's subaccount (the account that owns the funds)

Sender field: Always your main wallet's subaccount (the account that owns the funds)

- Signature: Created by the linked signer's private key

Signature: Created by the linked signer's private key

- Verification: Nado checks if the signature matches either the main wallet OR the linked signer for that subaccount

Verification: Nado checks if the signature matches either the main wallet OR the linked signer for that subaccount

- Result: Request is accepted if the linked signer is authorized for that subaccount

Result: Request is accepted if the linked signer is authorized for that subaccount

## 🏗️ Advanced: On-Chain Linked Signer Setup (Smart Contracts & Safe Wallets)

Use Cases: This advanced setup method enables:

- Smart contract integration: Your smart contract can trade on Nado by linking an EOA signer

Smart contract integration: Your smart contract can trade on Nado by linking an EOA signer

- Safe (Gnosis Safe) wallet trading: Multi-sig Safe wallets can link an EOA for trading

Safe (Gnosis Safe) wallet trading: Multi-sig Safe wallets can link an EOA for trading

- Contract-to-contract: Non-EOA accounts (contracts) as the main account, EOA as the trading signer

Contract-to-contract: Non-EOA accounts (contracts) as the main account, EOA as the trading signer

### Why Use On-Chain Setup?

The standard linked signer setup (via API) requires an EOA (Externally Owned Account) with a private key to sign the link request. But what if:

- Your main account is asmart contract(not an EOA)?

Your main account is asmart contract(not an EOA)?

- You want to use aSafe wallet(multi-sig contract) to trade?

You want to use aSafe wallet(multi-sig contract) to trade?

- You're building aprotocol integrationwhere the main account is a contract?

You're building aprotocol integrationwhere the main account is a contract?

Solution: Useslow mode transactionsto link a signer directly on-chain. This bypasses the EIP-712 signature requirement and allows contracts to link signers.

### How It Works

- Your smart contractcallssubmitSlowModeTransactionon the Nado Endpoint contract

Your smart contractcallssubmitSlowModeTransactionon the Nado Endpoint contract

`submitSlowModeTransaction`
- Transaction includes: LinkSigner data (sender = contract address, signer = EOA address)

Transaction includes: LinkSigner data (sender = contract address, signer = EOA address)

- Nado sequencerpicks up the on-chain transaction

Nado sequencerpicks up the on-chain transaction

- Result: The EOA is now authorized to sign trades for the contract's subaccount

Result: The EOA is now authorized to sign trades for the contract's subaccount

### Setup Steps

#### Prerequisites

- Smart contract deployed on-chain (or Safe wallet)

Smart contract deployed on-chain (or Safe wallet)

- ≥ 1 USDT0 for slow mode fee

≥ 1 USDT0 for slow mode fee

- EOA private key to use as the linked signer

EOA private key to use as the linked signer

#### Step 1: Deposit Funds to Contract Subaccount

Your contract must first deposit into Nado to create its subaccount:

#### Step 2: Link Signer via Slow Mode Transaction

After submission:

- Wait ~5-10 seconds for sequencer to process

Wait ~5-10 seconds for sequencer to process

- EOA can now sign trades for the contract's subaccount

EOA can now sign trades for the contract's subaccount

For Safe (Gnosis Safe) wallets:

- Generate an EOAto use as linked signer:

Generate an EOAto use as linked signer:

- Option A: Use Nado UIConnect your Safe wallet toapp.nado.xyzGo to Settings → 1-Click TradingEnable 1-Click TradingPaste the EOA private key(from step 1) instead of generating randomSafe will propose a transaction to owners for approvalOnce approved and executed, EOA is linked

Option A: Use Nado UI

- Connect your Safe wallet toapp.nado.xyz

Connect your Safe wallet toapp.nado.xyz

[app.nado.xyz](https://app.nado.xyz)
- Go to Settings → 1-Click Trading

Go to Settings → 1-Click Trading

- Enable 1-Click Trading

Enable 1-Click Trading

- Paste the EOA private key(from step 1) instead of generating random

Paste the EOA private key(from step 1) instead of generating random

- Safe will propose a transaction to owners for approval

Safe will propose a transaction to owners for approval

- Once approved and executed, EOA is linked

Once approved and executed, EOA is linked

- Option B: Use Safe Transaction BuilderGo to Safe's Transaction Builder appCallsubmitSlowModeTransactionon Nado EndpointUse the Solidity code above as reference for transaction dataOwners approve and execute

Option B: Use Safe Transaction Builder

- Go to Safe's Transaction Builder app

Go to Safe's Transaction Builder app

- CallsubmitSlowModeTransactionon Nado Endpoint

CallsubmitSlowModeTransactionon Nado Endpoint

`submitSlowModeTransaction`
- Use the Solidity code above as reference for transaction data

Use the Solidity code above as reference for transaction data

- Owners approve and execute

Owners approve and execute

### Important Notes

Slow Mode Fee: Requires 1 USDT0 fee for each slow mode transaction. Make sure your contract has approved the Nado Endpoint for this amount.

Processing Time: Slow mode transactions take ~5-10 seconds to be picked up by the Nado sequencer. Query the linked signer endpoint to verify it's been processed.

Use Cases:

- DeFi protocols: Your lending protocol's contract can trade on Nado

DeFi protocols: Your lending protocol's contract can trade on Nado

- DAOs: DAO treasury (multi-sig) can link a trading bot EOA

DAOs: DAO treasury (multi-sig) can link a trading bot EOA

- Automated strategies: Contract-based strategies can execute trades via linked EOA

Automated strategies: Contract-based strategies can execute trades via linked EOA

- Safe wallets: Use Safe for custody, EOA for trading (best of both worlds)

Safe wallets: Use Safe for custody, EOA for trading (best of both worlds)

### Verification

After submitting the slow mode transaction, verify the link worked:

Expected response:

### Complete Example: Safe Wallet Trading

Scenario: You have a Safe wallet with $100K and want to trade on Nado without exposing the Safe's keys.

Setup:

- Generate a random EOA (linked signer)

Generate a random EOA (linked signer)

- Deposit $100K from Safe to Nado (creates Safe's subaccount)

Deposit $100K from Safe to Nado (creates Safe's subaccount)

- Use Nado UI or Safe Transaction Builder to link the EOA

Use Nado UI or Safe Transaction Builder to link the EOA

- Run a trading bot with the EOA's private key

Run a trading bot with the EOA's private key

- Bot places trades for the Safe's subaccount

Bot places trades for the Safe's subaccount

- Withdrawals go back to the Safe wallet address

Withdrawals go back to the Safe wallet address

Security: Even if the EOA key is compromised, attacker can only trade (not withdraw to their own address). Funds always return to the Safe.

### Learn More

For complete smart contract integration details, see:

- Integrate via Smart Contracts- Full technical documentation

Integrate via Smart Contracts- Full technical documentation

[Integrate via Smart Contracts](/developer-resources/api/integrate-via-smart-contracts)
- Endpoint Contract Source- Nado's on-chain contracts

Endpoint Contract Source- Nado's on-chain contracts

[Endpoint Contract Source](https://github.com/nadohq/nado-contracts/blob/main/core/contracts/Endpoint.sol)

## 🔄 How to Update Your Linked Signer

Need to rotate your linked signer key? Here's how:

Important: Linking a new signer immediately revokes the old one. There's no grace period. Update your trading bots to use the new key before revoking.

## ❌ How to Disable (Revoke) Your Linked Signer

To completely remove the linked signer:

## ⚠️ Common Issues & Solutions

### Error: "Signature does not match" (Error 2028)

Cause: You're signing with the wrong private key.

Debug steps:

- Check what linked signer is currently set:

Check what linked signer is currently set:

- Verify your signing key's address:

Verify your signing key's address:

- Compare:If no linked signer (zero address): Use main wallet keyIf linked signer is set: Use that key OR main wallet key

Compare:

- If no linked signer (zero address): Use main wallet key

If no linked signer (zero address): Use main wallet key

- If linked signer is set: Use that key OR main wallet key

If linked signer is set: Use that key OR main wallet key

Solution: Use the correct private key when creating your client.

### Error: UI 1-Click Trading Broken

Symptoms:

- 1-Click Trading worked before

1-Click Trading worked before

- You updated linked signer via API

You updated linked signer via API

- Now UI shows errors when placing orders

Now UI shows errors when placing orders

Cause: UI is still using the old linked signer key, but you changed it via API.

Solution Option 1 (Easiest):

- Go to UI Settings

Go to UI Settings

- Disable 1-Click Trading

Disable 1-Click Trading

- Re-enable 1-Click Trading

Re-enable 1-Click Trading

- UI will generate a NEW key and link it

UI will generate a NEW key and link it

Solution Option 2 (Keep Your API Key):

- Query your current linked signer via API (the one you want to keep)

Query your current linked signer via API (the one you want to keep)

- In UI Settings: Disable 1-Click Trading

In UI Settings: Disable 1-Click Trading

- Enable 1-Click Trading with "Use existing key"

Enable 1-Click Trading with "Use existing key"

- Paste your API's linked signer private key

Paste your API's linked signer private key

Solution Option 3 (Admin Tools):

- Go toapp.nado.xyz/admin-tools

Go toapp.nado.xyz/admin-tools

[app.nado.xyz/admin-tools](https://app.nado.xyz/admin-tools)
- Use "Reset Linked Signer" to sync API and UI

Use "Reset Linked Signer" to sync API and UI

### Error: Hit Rate Limit When Updating Linked Signer

Cause: You've changed linked signer 50+ times in the past 7 days.

Solution:

Check your rate limit usage:

Response shows how many operations you have left. Wait for the 7-day window to roll over, or use your current linked signer.

## 🔒 Security Considerations

### Linked Signer Has Full Access

Critical: A linked signer can do ANYTHING your main wallet can do on your subaccount:

- Place and cancel orders

Place and cancel orders

- Withdraw funds (funds go to themain wallet, not the linked signer)

Withdraw funds (funds go to themain wallet, not the linked signer)

- Change the linked signer

Change the linked signer

- Mint/burn NLP

Mint/burn NLP

Treat the linked signer private key like your main wallet key.

Important: While a linked signer can initiate withdrawals,all withdrawals always go to the main wallet address(the subaccount owner). The linked signer cannot withdraw funds to its own address or any other address.

### Best Practices

- Generate unique keys: Don't reuse private keys across subaccounts or platforms

Generate unique keys: Don't reuse private keys across subaccounts or platforms

- Rotate regularly: Change linked signer every 30-90 days

Rotate regularly: Change linked signer every 30-90 days

- Monitor activity: Check your subaccount for unexpected activity

Monitor activity: Check your subaccount for unexpected activity

- Limit exposure: Only deposit what you need for trading

Limit exposure: Only deposit what you need for trading

- Secure storage: Store linked signer keys in environment variables or secrets manager, never in code

Secure storage: Store linked signer keys in environment variables or secrets manager, never in code

### Compromised Linked Signer?

If you suspect your linked signer key was compromised:

- Immediately revokeit (set to zero address) using your main wallet

Immediately revokeit (set to zero address) using your main wallet

- Withdraw fundsfrom the subaccount if needed

Withdraw fundsfrom the subaccount if needed

- Generate a newlinked signer key

Generate a newlinked signer key

- Investigatehow the compromise happened

Investigatehow the compromise happened

## 📊 Rate Limits

Limit: 50 linked signer operations per subaccount per 7-day rolling window

What counts as an operation:

- Linking a new signer

Linking a new signer

- Updating linked signer

Updating linked signer

- Revoking linked signer (setting to zero)

Revoking linked signer (setting to zero)

Check your usage:

50 operations per week is generous for normal use. If you hit the limit, you're likely testing or have a misconfigured bot updating the signer repeatedly.

## 📚 Related Documentation

- Core Concepts- Fundamentals of authentication and subaccounts

Core Concepts- Fundamentals of authentication and subaccounts

[Core Concepts](/developer-resources/get-started/core-concepts)
- Common Errors- Troubleshooting signature errors

Common Errors- Troubleshooting signature errors

[Common Errors](/developer-resources/get-started/common-errors)
- API Reference: Link Signer- Technical API docs

API Reference: Link Signer- Technical API docs

[API Reference: Link Signer](/developer-resources/api/gateway/executes/link-signer)
- API Reference: Query Linked Signer- Query endpoint docs

API Reference: Query Linked Signer- Query endpoint docs

[API Reference: Query Linked Signer](/developer-resources/api/gateway/queries/linked-signer)

## 🆘 Need Help?

Still confused about linked signers?

- Telegram Community:Join our Telegram- Ask questions, we're here to help!

Telegram Community:Join our Telegram- Ask questions, we're here to help!

[Join our Telegram](https://t.me/+whsZJKpiiVwwNjQ0)
- Submit a ticket:Nado Support

Submit a ticket:Nado Support

[Nado Support](https://nado-90114.zendesk.com/hc/en-us/requests/new?ticket_form_id=52275013155481)

You've got this!Linked signers seem complex at first, but once set up, they make trading much more convenient and secure. Take your time, follow the examples above, and don't hesitate to ask for help.

[PreviousFirst Deposit](/developer-resources/get-started/first-deposit)
[NextCommon Errors](/developer-resources/get-started/common-errors)

Last updated9 days ago