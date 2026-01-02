---
url: https://docs.nado.xyz/developer-resources/api/symbols
title: Symbols
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Symbols

Retrieve symbols for all available products.

## Request

GET[GATEWAY_REST_ENDPOINT]/symbols

`[GATEWAY_REST_ENDPOINT]/symbols`

## Response

```
[
    {
        "product_id": 0,
        "symbol": "USDT0",
        "delisted": false
    },
    {
        "product_id": 1,
        "symbol": "KBTC",
        "delisted": false
    },
    {
        "product_id": 2,
        "symbol": "BTC-PERP",
        "delisted": false
    },
    {
        "product_id": 3,
        "symbol": "WETH",
        "delisted": false
    },
    {
        "product_id": 4,
        "symbol": "ETH-PERP",
        "delisted": false
    },
    {
        "product_id": 5,
        "symbol": "USDC",
        "delisted": false
    },
    {
        "product_id": 8,
        "symbol": "SOL-PERP",
        "delisted": false
    },
    {
        "product_id": 10,
        "symbol": "XRP-PERP",
        "delisted": false
    },
    {
        "product_id": 14,
        "symbol": "BNB-PERP",
        "delisted": false
    },
    {
        "product_id": 16,
        "symbol": "HYPE-PERP",
        "delisted": false
    },
    {
        "product_id": 18,
        "symbol": "ZEC-PERP",
        "delisted": false
    },
    {
        "product_id": 20,
        "symbol": "MON-PERP",
        "delisted": false
    },
    {
        "product_id": 22,
        "symbol": "FARTCOIN-PERP",
        "delisted": false
    }
]
```

[PreviousErrors](/developer-resources/api/errors)
[NextDepositing](/developer-resources/api/depositing)

Last updated24 days ago