---
url: https://docs.nado.xyz/developer-resources/get-started/common-errors
title: 🔧Common Errors
---

- Developer Resources
[Developer Resources](/developer-resources)
- 🚀Get Started
[🚀Get Started](/developer-resources/get-started)

# 🔧Common Errors

You're not alone.Most errors when integrating with Nado fall into a few categories. This guide shows you exactly how to fix them.

## 🚨 Error 2028: "Signature does not match with sender's or linked signer's"

Most Common Error

This means Nado couldn't verify your EIP-712 signature. This is the most common integration error.

### What It Means

Your signature verification failed. Nado checked your signature against:

- Your main wallet's address

Your main wallet's address

- Your subaccount's linked signer address (if one is set)

Your subaccount's linked signer address (if one is set)

And neither matched.

### 🔑 Cause 1: Wrong Private Key

You're signing with a key that doesn't match either:

- Your main wallet's private key, OR

Your main wallet's private key, OR

- Your current linked signer's private key

Your current linked signer's private key

How to fix:

### 🌐 Cause 2: Wrong Chain ID

Using the wrong network identifier in your EIP-712 domain.

Correct chain IDs:

- Mainnet:57073

Mainnet:57073

`57073`
- Testnet:763373

Testnet:763373

`763373`

How to fix:

### 📝 Cause 3: Wrong Verifying Contract

TheverifyingContractfield in your EIP-712 domain must match the operation type.

`verifyingContract`

The rules:

- Forplace_order: Useaddress(productId)(e.g., product 2 →0x0000000000000000000000000000000000000002)

Forplace_order: Useaddress(productId)(e.g., product 2 →0x0000000000000000000000000000000000000002)

`place_order`
`address(productId)`
`0x0000000000000000000000000000000000000002`
- For all other executes: Use the endpoint contract address

For all other executes: Use the endpoint contract address

This is a common gotcha!Order placement uses a different verifying contract than other operations.

How to fix:

If you're building raw API calls:Query/v1/query?type=contractsto get the endpoint address. For orders, useaddress(productId)as the verifying contract. For other executes, use the endpoint address.

`/v1/query?type=contracts`
`address(productId)`

### 🔢 Cause 4: Wrong Data Types

EIP-712 requires exact type matching. Common mistakes:

- expirationmust beuint64(number), not string

expirationmust beuint64(number), not string

`expiration`
`uint64`
- noncemust beuint64(number), not string

noncemust beuint64(number), not string

`nonce`
`uint64`
- amountmust beint128, not string

amountmust beint128, not string

`amount`
`int128`

How to fix:

The SDKs handle type conversion automatically. If you're building raw signatures:

### 🐛 Debug Checklist

If you're still getting signature errors, check these in order:

- Verify your key: Print the address of the key you're signing with

Verify your key: Print the address of the key you're signing with

- Check linked signer: Querylinked_signerendpoint to see what's currently set

Check linked signer: Querylinked_signerendpoint to see what's currently set

`linked_signer`
- Verify chain ID: Mainnet = 57073, Testnet = 763373

Verify chain ID: Mainnet = 57073, Testnet = 763373

- Check verifying contract: Order placement vs other executes use different addresses

Check verifying contract: Order placement vs other executes use different addresses

- Print EIP-712 payload: Before signing, log the entire typed data structure

Print EIP-712 payload: Before signing, log the entire typed data structure

- Use SDK examples: The SDKs are battle-tested - compare your code to SDK source

Use SDK examples: The SDKs are battle-tested - compare your code to SDK source

Pro tip: If signature works in the UI but fails via API, your linked signer is likely different. Query the linked signer endpoint to verify.

## 💰 Error 2024: "Provided address has no previous deposits"

What It Means

Your subaccount doesn't exist yet. Subaccounts are created on first deposit (minimum $5 USDT0).

### Common Causes

### 📭 Cause 1: No Initial Deposit

You haven't made a deposit yet, or it was less than $5 USDT0.

How to fix:

- Deposit at least $5 USDT0 to create the subaccount

Deposit at least $5 USDT0 to create the subaccount

- Wait for blockchain confirmation (~few seconds on Ink)

Wait for blockchain confirmation (~few seconds on Ink)

- Verify subaccount exists:

Verify subaccount exists:

See also:First Deposit Guidefor step-by-step deposit instructions

[First Deposit Guide](/developer-resources/get-started/first-deposit)

### 🌐 Cause 2: Wrong Network

You're querying the wrong network (testnet vs mainnet).

Symptoms:

- Subaccount shows balance in UI

Subaccount shows balance in UI

- But API returnsexists: false

But API returnsexists: false

`exists: false`

How to fix:

Verify you're using the correct endpoint:

- Mainnet:gateway.prod.nado.xyz(chain ID 57073)

Mainnet:gateway.prod.nado.xyz(chain ID 57073)

`gateway.prod.nado.xyz`
- Testnet:gateway.test.nado.xyz(chain ID 763373)

Testnet:gateway.test.nado.xyz(chain ID 763373)

`gateway.test.nado.xyz`

### 📝 Cause 3: Wrong Subaccount bytes32

Your subaccount bytes32 format is incorrect.

Format:bytes32 = wallet address (20 bytes) + subaccount name (12 bytes)

`bytes32 = wallet address (20 bytes) + subaccount name (12 bytes)`

How to fix:

## 🔄 Error: 1-Click Trading Broken After API Integration

Cause: Linked Signer Mismatch

You updated the linked signer via API, but the UI is still trying to use the old key.

### How to Fix

Option 1: Reset in UI(Easiest)

- Go to Nado UI atapp.nado.xyz

Go to Nado UI atapp.nado.xyz

[app.nado.xyz](https://app.nado.xyz)
- Disable 1-Click Trading

Disable 1-Click Trading

- Re-enable 1-Click Trading (UI will generate new key and link it)

Re-enable 1-Click Trading (UI will generate new key and link it)

Option 2: Use Admin Tools

- Go toapp.nado.xyz/admin-tools

Go toapp.nado.xyz/admin-tools

[app.nado.xyz/admin-tools](https://app.nado.xyz/admin-tools)
- Find "Reset Linked Signer" section

Find "Reset Linked Signer" section

- Follow instructions to sync API and UI

Follow instructions to sync API and UI

Option 3: Update UI to Use Your Key

If you want the UI to use YOUR linked signer (not a random one):

- Query your current linked signer:

Query your current linked signer:

- In UI: Manually enter that private key when enabling 1-Click Trading

In UI: Manually enter that private key when enabling 1-Click Trading

## 📡 Error: Wrong Endpoint / Network Mismatch

### Symptoms

- API returns errors but UI works fine

API returns errors but UI works fine

- "Subaccount not found" but you see balance in UI

"Subaccount not found" but you see balance in UI

- Signature works in UI but fails via API

Signature works in UI but fails via API

### Solution

Verify you're using matching endpoints:

Mainnet

gateway.prod.nado.xyz

`gateway.prod.nado.xyz`

57073

Real funds, production

Testnet

gateway.test.nado.xyz

`gateway.test.nado.xyz`

763373

Testing, development

Check what the UI is using:

- Go toapp.nado.xyz

Go toapp.nado.xyz

[app.nado.xyz](https://app.nado.xyz)
- Look at network indicator (top right)

Look at network indicator (top right)

- Match your API endpoint to that network

Match your API endpoint to that network

## 💡 General Debugging Tips

### Start with SDK Examples

The SDKs are battle-tested. If you're hitting errors:

- Find a similar example in the SDK docs:Python SDKTypeScript SDKRust SDK

Find a similar example in the SDK docs:

- Python SDK

Python SDK

[Python SDK](https://nadohq.github.io/nado-python-sdk/index.html)
- TypeScript SDK

TypeScript SDK

[TypeScript SDK](/developer-resources/typescript-sdk)
- Rust SDK

Rust SDK

[Rust SDK](https://crates.io/crates/nado-sdk)
- Compare your code to the example

Compare your code to the example

- Use the SDK method directly (let it handle the complexity)

Use the SDK method directly (let it handle the complexity)

### Enable Debug Logging

### Verify with Raw API Call

If SDK is failing, try a raw curl to isolate the issue:

If raw API works but SDK fails → SDK configuration issue If raw API also fails → Network/endpoint issue

## 🆘 Still Stuck?

If you've tried everything above and still hitting errors:

### 1. Check What's Different

What works:

- UI? (means your wallet/funds are correct)

UI? (means your wallet/funds are correct)

- SDK examples? (means SDK is configured correctly)

SDK examples? (means SDK is configured correctly)

- Raw curl? (means API is accessible)

Raw curl? (means API is accessible)

What fails:

- Your specific code? (code issue)

Your specific code? (code issue)

- All SDK methods? (configuration issue)

All SDK methods? (configuration issue)

- Everything including curl? (network/endpoint issue)

Everything including curl? (network/endpoint issue)

### 2. Get Help

- Telegram Community:Join our Telegram- Paste your error, we'll help debug

Telegram Community:Join our Telegram- Paste your error, we'll help debug

[Join our Telegram](https://t.me/+whsZJKpiiVwwNjQ0)
- Submit a ticket:Nado Support

Submit a ticket:Nado Support

[Nado Support](https://nado-90114.zendesk.com/hc/en-us/requests/new?ticket_form_id=52275013155481)

When asking for help, include:

- Error message (exact text)

Error message (exact text)

- Network (mainnet/testnet)

Network (mainnet/testnet)

- SDK and version

SDK and version

- What you're trying to do (place order, deposit, etc.)

What you're trying to do (place order, deposit, etc.)

- Code snippet (remove private keys!)

Code snippet (remove private keys!)

Remember:Most integration errors are one of the 6 issues above. Check the list systematically and you'll find the culprit.

## Next Steps

- Back to basics:Core Concepts- Review fundamentals

Back to basics:Core Concepts- Review fundamentals

[Core Concepts](/developer-resources/get-started/core-concepts)
- Deep dive:Linked Signers Guide- Master the most confusing part

Deep dive:Linked Signers Guide- Master the most confusing part

[Linked Signers Guide](/developer-resources/get-started/linked-signers)
- Get trading:First Trade Guide- Place your first order

Get trading:First Trade Guide- Place your first order

[First Trade Guide](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/get-started/first-trade.md)
[PreviousLinked Signers](/developer-resources/get-started/linked-signers)
[NextAPI](/developer-resources/api)

Last updated9 days ago