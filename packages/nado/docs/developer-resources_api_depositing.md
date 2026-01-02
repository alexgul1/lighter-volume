---
url: https://docs.nado.xyz/developer-resources/api/depositing
title: Depositing
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Depositing

There are two ways to deposit funds into Nado programmatically:

- On-Chain Contract Call- Direct interaction with the Endpoint contract (recommended)

On-Chain Contract Call- Direct interaction with the Endpoint contract (recommended)

- Direct Deposit- Simple transfer to your unique deposit address (alternative, requires caution)

Direct Deposit- Simple transfer to your unique deposit address (alternative, requires caution)

## Method 1: On-Chain Contract Call (Recommended)

Deposit by calling the Endpoint contract directly. This is the recommended method for programmatic deposits.

### Contract Address

Find the Endpoint contract address at:

`GET <nado-url>/query?type=contracts`

### Function Interface

#### Basic Deposit

```
function depositCollateral(
    bytes12 subaccountName,  // last 12 bytes of the subaccount bytes32
    uint32 productId,        // product ID for the token
    uint128 amount          // raw token amount (see decimals below)
) external
```

Parameters:

- subaccountName: The last 12 bytes of your subaccount identifier (e.g.,0x64656661756c740000000000for "default")

subaccountName: The last 12 bytes of your subaccount identifier (e.g.,0x64656661756c740000000000for "default")

`subaccountName`
`0x64656661756c740000000000`
- productId: The product ID for the token you're depositing

productId: The product ID for the token you're depositing

`productId`
- amount: The raw amount in the token's smallest unitFor USDT0 (6 decimals): 1 USDT0 =1e6=1000000For wETH (18 decimals): 1 wETH =1e18For wBTC (8 decimals): 1 wBTC =1e8

amount: The raw amount in the token's smallest unit

`amount`
- For USDT0 (6 decimals): 1 USDT0 =1e6=1000000

For USDT0 (6 decimals): 1 USDT0 =1e6=1000000

`1e6`
`1000000`
- For wETH (18 decimals): 1 wETH =1e18

For wETH (18 decimals): 1 wETH =1e18

`1e18`
- For wBTC (8 decimals): 1 wBTC =1e8

For wBTC (8 decimals): 1 wBTC =1e8

`1e8`

#### Deposit with Referral Code

### Prerequisites

Before depositing via contract call, you must:

- Approve Token Allowance

Approve Token Allowance

- Get Product InformationUseAll Productsquery to find:Product ID for your tokenToken contract addressToken decimals

Get Product Information

- UseAll Productsquery to find:Product ID for your tokenToken contract addressToken decimals

UseAll Productsquery to find:

[All Products](/developer-resources/api/gateway/queries/all-products)
- Product ID for your token

Product ID for your token

- Token contract address

Token contract address

- Token decimals

Token decimals

### Example: Depositing 100 USDT0

Assuming USDT0 has product ID0and 6 decimals:

`0`

#### Using Python SDK (Recommended)

#### Using Raw Contract (Low-level)

Advantages:

- Type-safe: Product ID ensures correct token

Type-safe: Product ID ensures correct token

- Explicit: Clear which token and amount you're depositing

Explicit: Clear which token and amount you're depositing

- Fails early: Transaction reverts if parameters are incorrect

Fails early: Transaction reverts if parameters are incorrect

### Processing Time

Deposits may take a few seconds to process after transaction confirmation. You can monitor your balance via:

- Subaccount Infoquery

Subaccount Infoquery

[Subaccount Info](/developer-resources/api/gateway/queries/subaccount-info)
- WebSocket subscriptions for real-time updates

WebSocket subscriptions for real-time updates

## Method 2: Direct Deposit (Alternative)

Each subaccount has a unique deposit address. You can send funds directly to this address and they will automatically be credited to your subaccount.

Caution: Only use this method if you're certain you're sending a supported token. Sending unsupported tokens to this address will result in permanent loss of funds. We recommend using the On-Chain Contract Call method instead.

### Getting Your Deposit Address

Query your unique deposit address using theDirect Deposit Addressendpoint:

[Direct Deposit Address](/developer-resources/api/archive-indexer/direct-deposit-address)

Request:

Response:

### Depositing Funds

- Get your deposit address using the API call above

Get your deposit address using the API call above

- Verify the token is supportedviaAll Productsquery

Verify the token is supportedviaAll Productsquery

[All Products](/developer-resources/api/gateway/queries/all-products)
- Send the supported token directly to this address from any wallet (MetaMask, CEX, etc.)

Send the supported token directly to this address from any wallet (MetaMask, CEX, etc.)

- Funds will be automatically credited to your subaccount within a few seconds

Funds will be automatically credited to your subaccount within a few seconds

Advantages:

- No need to interact with smart contracts

No need to interact with smart contracts

- No need to approve allowances

No need to approve allowances

- Works with any wallet (including CEX withdrawals)

Works with any wallet (including CEX withdrawals)

- Simpler for end users

Simpler for end users

Critical Warnings:

- ⚠️ONLY send supported tokens- Find supported tokens viaAll Products

⚠️ONLY send supported tokens- Find supported tokens viaAll Products

[All Products](/developer-resources/api/gateway/queries/all-products)
- ⚠️Sending unsupported tokens will result in permanent loss

⚠️Sending unsupported tokens will result in permanent loss

- ⚠️Use the correct network- Ink (mainnet) or Ink Sepolia (testnet)

⚠️Use the correct network- Ink (mainnet) or Ink Sepolia (testnet)

- ⚠️No refunds for incorrect deposits- Double-check before sending

⚠️No refunds for incorrect deposits- Double-check before sending

## Important Notes

- Use Correct Product ID: Each token has a specific product ID. Using the wrong ID will cause the transaction to fail.

Use Correct Product ID: Each token has a specific product ID. Using the wrong ID will cause the transaction to fail.

- Check Token Decimals: Always multiply by the correct decimal factor (6 for USDT0, 18 for wETH, etc.)

Check Token Decimals: Always multiply by the correct decimal factor (6 for USDT0, 18 for wETH, etc.)

- Minimum Deposit: Some products may have minimum deposit amounts

Minimum Deposit: Some products may have minimum deposit amounts

- Only Supported Tokens: Only deposit tokens that are listed via the All Products query

Only Supported Tokens: Only deposit tokens that are listed via the All Products query

## Getting Token Information

Use theAll Productsquery to get:

[All Products](/developer-resources/api/gateway/queries/all-products)

This information is essential for:

- Finding the correctproductId

Finding the correctproductId

`productId`
- Getting the token contract for approvals (Method 1 only)

Getting the token contract for approvals (Method 1 only)

- Calculating the correctamountwith proper decimals

Calculating the correctamountwith proper decimals

`amount`
- Verifying a token is supported before using direct deposit

Verifying a token is supported before using direct deposit

[PreviousSymbols](/developer-resources/api/symbols)
[NextWithdrawing (on-chain)](/developer-resources/api/withdrawing-on-chain)

Last updated9 days ago