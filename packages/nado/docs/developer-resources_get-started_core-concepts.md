---
url: https://docs.nado.xyz/developer-resources/get-started/core-concepts
title: 📖Core Concepts
---

- Developer Resources
[Developer Resources](/developer-resources)
- 🚀Get Started
[🚀Get Started](/developer-resources/get-started)

# 📖Core Concepts

If you're coming from a centralized exchange (CEX) API, Nado works differently. This guide explains the fundamental concepts that are different from what you might expect, so you can integrate successfully without confusion.

## What Makes Nado Different?

Nado is adecentralized exchange. This means:

- ❌No API keys- You sign requests with your wallet's private key

❌No API keys- You sign requests with your wallet's private key

- ❌No username/password- Your wallet address is your identity

❌No username/password- Your wallet address is your identity

- ✅Full custody- You control your funds at all times

✅Full custody- You control your funds at all times

- ✅On-chain settlement- Trades settle on the blockchain

✅On-chain settlement- Trades settle on the blockchain

If these concepts are new to you, don't worry. This guide will walk you through everything step by step.

## 1. Authentication: Wallet Signatures, Not API Keys

TL;DR:Nado uses wallet signatures (EIP-712) instead of API keys. Your wallet's private key IS your authentication. Executes (writes) need signatures; queries (reads) don't.

### 🔑 The CEX Model (What You Might Expect)

On centralized exchanges like Binance or Coinbase:

- You create an account → get API key + secret

You create an account → get API key + secret

- You sign requests with HMAC using that secret

You sign requests with HMAC using that secret

- The exchange validates your API key

The exchange validates your API key

### 🔐 The Nado Model (How It Actually Works)

On Nado:

- You have a wallet (like MetaMask, a hardware wallet, or just a private key)

You have a wallet (like MetaMask, a hardware wallet, or just a private key)

- You sign requests with your wallet's private key usingEIP-712(EVM signing standard)

You sign requests with your wallet's private key usingEIP-712(EVM signing standard)

- Nado validates your cryptographic signature

Nado validates your cryptographic signature

Why no API keys?Because Nado is decentralized - there's no central server to issue API keys. Your wallet's private key IS your authentication.

### 📝 What This Means for You

Every write operation (execute) must be cryptographically signed.

This includes operations like:

- Placing orders

Placing orders

- Canceling orders

Canceling orders

- Depositing/withdrawing funds

Depositing/withdrawing funds

- Linking signers

Linking signers

Good news:Read operations (queries) don't require signing! Things like checking balances, getting market data, or querying order status work without signatures.

Here's a simple example of setting up a client that handles signing for you:

🔒 Security Critical:Your private key gives FULL access to your funds. Never share it, commit it to git, or send it over unencrypted channels.

### ✍️ Two Ways to Sign Executes

When performing write operations (executes), you can sign witheither:

- Your main wallet's private key(always works)

Your main wallet's private key(always works)

- A linked signer's private key(optional - explained in Section 3)

A linked signer's private key(optional - explained in Section 3)

Common Issue:Signature errors often happen when users don't realize they can use either key. Both are cryptographically valid!

## 2. Subaccounts: Your Trading Compartments

TL;DR:Subaccounts are trading compartments within your wallet. Format = wallet address (20 bytes) + name (12 bytes). Must deposit ≥$5 USDT0 to create. Start with "default" subaccount.

### 📦 What is a Subaccount?

A subaccount is atrading compartmentwithin your wallet. Think of it like having multiple trading accounts tied to the same wallet address.

Format: Subaccounts are identified by abytes32value that combines:

`bytes32`
- 20 bytes: Your wallet address (e.g.,0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb)

20 bytes: Your wallet address (e.g.,0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb)

`0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb`
- 12 bytes: Subaccount name (e.g.,default,strategy1, etc.)

12 bytes: Subaccount name (e.g.,default,strategy1, etc.)

`default`
`strategy1`

Example:

### 🎯 The Default Subaccount

When you first interact with Nado, you'll use the"default" subaccount. This is standard across Nado:

- UI users: Automatically use "default"

UI users: Automatically use "default"

- API users: Should use "default" to start

API users: Should use "default" to start

### 💰 Creating a Subaccount: The Critical Step

⚠️ CRITICAL: A subaccount doesn't exist until you make an initial deposit ofat least $5 USDT0(or equivalent).

This trips up almost everyone. Here's what happens:

Before deposit:

After deposit (≥ $5):

Why?Nado is on-chain. Creating a subaccount requires an on-chain transaction, which happens when you make your first deposit.

Common Error: Trying to place an order before depositing →"error": "The provided address has no previous deposits"

`"error": "The provided address has no previous deposits"`

Solution: Make an initial deposit first. See ourFirst Depositguide.

[First Deposit](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/get-started/first-deposit.md)

### 🔢 Multiple Subaccounts

- UI limit: 4 subaccounts (default,default_1,default_2,default_3)

UI limit: 4 subaccounts (default,default_1,default_2,default_3)

`default`
`default_1`
`default_2`
`default_3`
- API limit: Unlimited! You can create as many as you want programmatically

API limit: Unlimited! You can create as many as you want programmatically

Each subaccount is completely independent:

- Independent balances and positions

Independent balances and positions

- Independent health (risk) calculations

Independent health (risk) calculations

- Can be liquidated independently (one doesn't affect others)

Can be liquidated independently (one doesn't affect others)

- Can have its own linked signer (see Section 3)

Can have its own linked signer (see Section 3)

Common use cases:

- 🎯 Separate strategies (one for spot, one for perps)

🎯 Separate strategies (one for spot, one for perps)

- 📊 Different risk levels (conservative vs aggressive)

📊 Different risk levels (conservative vs aggressive)

- 👥 Team management (each trader gets a subaccount)

👥 Team management (each trader gets a subaccount)

- 🧪 Testing (use a separate subaccount to test new strategies)

🧪 Testing (use a separate subaccount to test new strategies)

## 3. Linked Signers: Delegation for Security

TL;DR:Linked signers let you authorize a separate key to trade on your behalf. Optional but recommended for security. Main wallet = master key, linked signer = trading-only key. Can revoke anytime.

Skip this if you're just getting started.Linked signers are optional. You can always sign with your main wallet's private key.

Come back here when you see "1-Click Trading" or "1CT" mentioned, or when you're ready to set up delegated signing for security.

### 🔗 What is a Linked Signer?

Alinked signeris a separate private key that you authorize to trade on behalf of your subaccount.

Think of it like this:

- 🔑Your main wallet= Your master key (controls everything, including funds)

🔑Your main wallet= Your master key (controls everything, including funds)

- ✍️Linked signer= A trading-only key (can place orders, cancel orders, but you control the authorization)

✍️Linked signer= A trading-only key (can place orders, cancel orders, but you control the authorization)

### 🛡️ Why Would You Use One?

Security: Keep your main wallet private key offline/secure, use a linked signer for day-to-day trading.

Common scenario:

- Main wallet: Hardware wallet (very secure, inconvenient for API trading)

Main wallet: Hardware wallet (very secure, inconvenient for API trading)

- Linked signer: Hot wallet private key (less secure, convenient for API)

Linked signer: Hot wallet private key (less secure, convenient for API)

- If linked signer is compromised → disable it, main wallet is still safe

If linked signer is compromised → disable it, main wallet is still safe

### ⚙️ How It Works

- Generate a new private key(or use an existing one):

Generate a new private key(or use an existing one):

- Link it to your subaccount(must sign with main wallet):

Link it to your subaccount(must sign with main wallet):

- To revoke/unlink a signer(set back to empty):

To revoke/unlink a signer(set back to empty):

- Now you can sign executes with either:Main wallet private key (always works!)Linked signer private key (if one is set)

Now you can sign executes with either:

- Main wallet private key (always works!)

Main wallet private key (always works!)

- Linked signer private key (if one is set)

Linked signer private key (if one is set)

### ✅ Verifying Your Current Linked Signer

Common Issue: "Why is my signature failing?" → Often because you're using the wrong private key.

Solution: Check which linked signer is currently set for your subaccount.

### 🖱️ UI 1-Click Trading (1CT)

If you see "1-Click Trading" or "1CT" in the Nado UI:

- This is a linked signer that the UI creates for you

This is a linked signer that the UI creates for you

- It generates a random private key and stores it locally

It generates a random private key and stores it locally

- It makes trading faster (no wallet popup for every order)

It makes trading faster (no wallet popup for every order)

Important for API users:

- If you set a linked signer via API, the UI's 1CT key becomes invalid

If you set a linked signer via API, the UI's 1CT key becomes invalid

- If the UI breaks after you change the linked signer via API:Go to UI settingsDisable 1-Click TradingRe-enable it with your new linked signer's private key (or let it generate a new one)

If the UI breaks after you change the linked signer via API:

- Go to UI settings

Go to UI settings

- Disable 1-Click Trading

Disable 1-Click Trading

- Re-enable it with your new linked signer's private key (or let it generate a new one)

Re-enable it with your new linked signer's private key (or let it generate a new one)

For a complete guide on linked signers, see ourLinked Signers Deep Dive.

[Linked Signers Deep Dive](/developer-resources/get-started/linked-signers)

## 4. Signing Requests: EIP-712

TL;DR:EIP-712 is the EVM signing standard. Executes (writes) need EIP-712 signatures; queries (reads) don't. SDKs handle this automatically.

### 🔐 What is EIP-712?

EIP-712 is the EVM standard for signing structured data. Every execute (write operation) you make to Nado—like placing orders, canceling orders, depositing, withdrawing—must be signed using EIP-712.

Queries (reads) don't need signing!Operations like checking balances or getting market data work without signatures.

Good news: The SDKs handle all of this automatically. You don't need to understand the details unless you're implementing raw API calls.

### ⚙️ The Signing Process (Behind the Scenes)

When you callclient.place_order(...), here's what happens:

`client.place_order(...)`
- SDK creates structured data:

SDK creates structured data:

- SDK signs it with your private keyusing EIP-712

SDK signs it with your private keyusing EIP-712

- SDK sends requestwith the signature

SDK sends requestwith the signature

- Nado verifiesthe signature matches your wallet or linked signer

Nado verifiesthe signature matches your wallet or linked signer

### ⚠️ Common Signing Errors

Error: "Signature does not match with sender's or linked signer's"

This means Nado couldn't verify your signature. This is the most common error when getting started.

🔑 Cause 1: Wrong Private Key

You're signing with a key that isn't:

- Your main wallet's private key, OR

Your main wallet's private key, OR

- Your linked signer's private key

Your linked signer's private key

Solution: Verify which linked signer is set (see Section 3 above), then use the correct key.

🌐 Cause 2: Wrong Chain ID

Using the wrong network identifier:

- Mainnet:57073

Mainnet:57073

`57073`
- Testnet:763373

Testnet:763373

`763373`

Solution: Make sure you're using the correct network when creating your client.

📝 Cause 3: Wrong Verifying Contract

TheverifyingContractfield in EIP-712 must match the operation:

`verifyingContract`
- Forplace_order: Useaddress(productId)(e.g., product 2 →0x0000000000000000000000000000000000000002)

Forplace_order: Useaddress(productId)(e.g., product 2 →0x0000000000000000000000000000000000000002)

`place_order`
`address(productId)`
`0x0000000000000000000000000000000000000002`
- For other operations: Use the endpoint contract address

For other operations: Use the endpoint contract address

Solution: The SDK handles this automatically. If you're making raw API calls, check theSigning Reference.

[Signing Reference](/developer-resources/api/gateway/signing)

🔢 Cause 4: Wrong Data Types

Type mismatches in the signature payload:

- expirationmust beuint64(number), not string

expirationmust beuint64(number), not string

`expiration`
`uint64`
- noncemust beuint64(number), not string

noncemust beuint64(number), not string

`nonce`
`uint64`

Solution: The SDK handles this. If implementing manually, check theEIP-712 Examples.

[EIP-712 Examples](/developer-resources/api/gateway/signing/examples)

For detailed troubleshooting and more error scenarios, see ourCommon Errors Guide.

[Common Errors Guide](/developer-resources/get-started/common-errors)

## 📋 Quick Reference

### 🔐 Authentication

- ❌ No API keys

❌ No API keys

- ✅ Executes (writes) require wallet signature (EIP-712)

✅ Executes (writes) require wallet signature (EIP-712)

- ✅ Queries (reads) don't require signatures

✅ Queries (reads) don't require signatures

- ✅ Can sign executes with main wallet OR linked signer

✅ Can sign executes with main wallet OR linked signer

### 👤 Subaccounts

- Format:bytes32= wallet address (20 bytes) + name (12 bytes)

Format:bytes32= wallet address (20 bytes) + name (12 bytes)

`bytes32`
- Default subaccount:"default"

Default subaccount:"default"

`"default"`
- Must deposit ≥ $5 to create

Must deposit ≥ $5 to create

- Check if exists:client.get_subaccount_info("default")→ look for"exists": true

Check if exists:client.get_subaccount_info("default")→ look for"exists": true

`client.get_subaccount_info("default")`
`"exists": true`

### 🔗 Linked Signers

- Optional delegation mechanism for signing executes

Optional delegation mechanism for signing executes

- One per subaccount

One per subaccount

- Can sign executes with EITHER main wallet OR linked signer

Can sign executes with EITHER main wallet OR linked signer

- Verify current:client.get_linked_signer("default")

Verify current:client.get_linked_signer("default")

`client.get_linked_signer("default")`
- UI "1-Click Trading" = linked signer

UI "1-Click Trading" = linked signer

### ✍️ Signing

- All executes (writes) use EIP-712 signatures

All executes (writes) use EIP-712 signatures

- Queries (reads) don't require signatures

Queries (reads) don't require signatures

- SDKs handle signing automatically

SDKs handle signing automatically

- Mainnet chain ID:57073

Mainnet chain ID:57073

`57073`
- Testnet chain ID:763373

Testnet chain ID:763373

`763373`

## Next Steps

Now that you understand the core concepts, you're ready to:

- Make Your First Deposit- Fund your subaccount

Make Your First Deposit- Fund your subaccount

[Make Your First Deposit](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/get-started/first-deposit.md)
- Place Your First Order- Start trading

Place Your First Order- Start trading

[Place Your First Order](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/get-started/first-trade.md)
- Set Up a Linked Signer- Optional: For better security

Set Up a Linked Signer- Optional: For better security

[Set Up a Linked Signer](/developer-resources/get-started/linked-signers)

If you run into issues, check ourCommon Errorstroubleshooting guide.

[Common Errors](/developer-resources/get-started/common-errors)

Remember: If you're confused, you're not alone. These concepts are different from traditional exchanges. Take your time, and don't hesitate to ask for help in ourTelegram communityorreport an issue.

[Telegram community](https://t.me/+whsZJKpiiVwwNjQ0)
[report an issue](https://nado-90114.zendesk.com/hc/en-us/requests/new?ticket_form_id=52275013155481)
[PreviousQuickstart](/developer-resources/get-started/quickstart)
[NextFirst Deposit](/developer-resources/get-started/first-deposit)

Last updated14 days ago