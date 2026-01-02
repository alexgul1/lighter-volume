# Nado API Overview

> Scraped from web search results - may need verification

## What is Nado?

Nado is a **non-custodial central limit order book (CLOB) exchange** built on **Ink L2** (EVM-compatible, Chain ID: 57073).

- Built by the team behind Kraken
- 5-15ms latency for order matching
- Batched on-chain settlement
- Up to 20x leverage on perpetuals
- Taker fees as low as 1.5 bps, maker rebates up to -0.8 bps

## API Endpoints

### Mainnet
- Gateway: `https://gateway.prod.nado.xyz/v1`
- Query: `https://gateway.prod.nado.xyz/v1/query`
- Execute: `https://gateway.prod.nado.xyz/v1/execute`

### Testnet
- Gateway: `https://gateway.test.nado.xyz/v2`
- Archive: `https://archive.test.nado.xyz/v2`
- Chain ID: 763373

## Authentication

All executes are signed using **EIP-712**.

### EIP-712 Domain
```javascript
{
  name: 'Nado',
  version: '0.0.1',
  chainId: 57073,  // mainnet
  verifyingContract: // see below
}
```

### Verifying Contract
- For `place_order`: use `address(productId)` (e.g., product 2 → `0x0000000000000000000000000000000000000002`)
- For other executes: query `/v1/query?type=contracts` to get endpoint address

### Sender Field Format
32 bytes = address (20 bytes) + subaccount identifier (12 bytes)

Example for address `0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43` with default subaccount:
```
0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000
```

## Place Order

### Endpoint
```
POST /v1/execute
```

### Request
```json
{
  "place_order": {
    "product_id": 1,
    "order": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
      "priceX18": "1000000000000000000",
      "amount": "1000000000000000000",
      "expiration": "4294967295",
      "nonce": "1757062078359666688",
      "appendix": "1"
    },
    "signature": "0x...",
    "id": 100
  }
}
```

### Fields
- **product_id**: Spot/perp product ID (query "All products" to get list)
- **priceX18**: Price with 18 decimals (1e18 = 1.0)
- **amount**: Amount with 18 decimals (1e18 = 1 unit of asset)
- **expiration**: Unix timestamp when order expires
- **nonce**: Unique nonce for the order
- **appendix**: 128-bit integer encoding order parameters (execution type, isolated margin, trigger type)
- **signature**: EIP-712 signature

### EIP-712 Order Type
```javascript
{
  Order: [
    { name: 'sender', type: 'bytes32' },
    { name: 'priceX18', type: 'int128' },
    { name: 'amount', type: 'int128' },
    { name: 'expiration', type: 'uint64' },
    { name: 'nonce', type: 'uint64' },
    { name: 'appendix', type: 'uint128' }
  ]
}
```

### Response
```json
{
  "status": "success",
  "signature": "{signature}",
  "data": {},
  "request_type": "place_order"
}
```

## Rate Limits

| Condition | Limit |
|-----------|-------|
| With spot leverage | 600 orders/min (10/sec) |
| Without spot leverage | 30 orders/min (5 per 10 sec) |

## Cancel Order

### Endpoints
- `cancel_orders` - Cancel specific orders
- `cancel_product_orders` - Cancel all orders for a product
- `cancel_and_place` - Atomic cancel + place

Orders can be cancelled for:
- Manual cancellation
- Expiration
- Failing health checks
- Self-trade prevention

## Query Endpoints

### Available Queries
- All Products
- Edge All Products
- Market Prices
- Subaccount Info
- Orders (with `trigger_types` filter)
- Subaccount Snapshots (`active` filter for non-zero balances)

### Amount Format
All amounts normalized to 18 decimals:
- Balance of 1 USDT = `1e18`
- Price of 1 BTC at $20,000 = `20000e18`

Negative balance = borrowing that asset (leveraged position).

## Common Errors

- **Signature Verification Failed**: Usually wrong chainId or verifyingContract in EIP-712 domain

## Documentation Links

- Overview: https://docs.nado.xyz/
- API: https://docs.nado.xyz/developer-resources/api
- V2 API: https://docs.nado.xyz/developer-resources/api/v2
- Place Order: https://docs.nado.xyz/developer-resources/api/gateway/executes/place-order
- Signing Examples: https://docs.nado.xyz/developer-resources/api/gateway/signing/examples
- Common Errors: https://docs.nado.xyz/developer-resources/get-started/common-errors
