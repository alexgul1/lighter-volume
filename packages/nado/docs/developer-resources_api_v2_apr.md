---
url: https://docs.nado.xyz/developer-resources/api/v2/apr
title: APR
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# APR

Retrieve current deposit / borrow APRs of available spots on Nado.

## Request

GET[GATEWAY_V2_ENDPOINT]/apr

`[GATEWAY_V2_ENDPOINT]/apr`

## Response

```
[
    {
        "name": "USDT0",
        "symbol": "USDT0",
        "product_id": 0,
        "deposit_apr": 6.32465621e-10,
        "borrow_apr": 0.010050173557473174,
        "tvl": 20001010125092.633
    },
    {
        "name": "Wrapped BTC",
        "symbol": "WBTC",
        "product_id": 1,
        "deposit_apr": 8.561123e-12,
        "borrow_apr": 0.010050166480005895,
        "tvl": 1045563178297771.2
    }
]
```

## Response Fields

product_id

number

No

Internal unique ID of spot / perp product

name

string

No

Asset name (as represented internally in the exchange).

symbol

string

No

Asset symbol (as represented internally in the exchange).

deposit_apr

float

No

The current estimated APR for depositing or holding this asset.Note: This value should be multiplied by 100 to represent the percentage (%) form.

borrow_apr

float

No

The current estimated APR for borrowing this asset.Note: This value should be multiplied by 100 to represent the percentage (%) form.

tvl

tvl

No

Total Value Locked (TVL) represents the current USDT0 value of this asset, calculated as the difference between deposits and borrows.

[PreviousPairs](/developer-resources/api/v2/pairs)
[NextOrderbook](/developer-resources/api/v2/orderbook)

Last updated1 month ago