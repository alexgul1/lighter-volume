---
url: https://docs.nado.xyz/developer-resources/api/v2/pairs
title: Pairs
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# Pairs

Retrieve details of all available trading pairs on Nado, including corresponding base and quote.

## Request

GET[GATEWAY_V2_ENDPOINT]/pairs?market={spot|perp}

`[GATEWAY_V2_ENDPOINT]/pairs?market={spot|perp}`

## Request Parameters

market

string

No

Indicates the corresponding market to fetch trading pairs for. Allowed values are:spotandperp. When nomarketparam is provided, it returns all available pairs.

`spot`
`perp`
`market`

## Response

```
[
    {
        "product_id": 1,
        "ticker_id": "BTC-PERP_USDT0",
        "base": "BTC-PERP",
        "quote": "USDT0"
    },
    {
        "product_id": 2,
        "ticker_id": "ETH-PERP_USDT0",
        "base": "ETH-PERP",
        "quote": "USDT0"
    },
    {
        "product_id": 3,
        "ticker_id": "BTC_USDT0",
        "base": "BTC",
        "quote": "USDT0"
    },
    {
        "product_id": 4,
        "ticker_id": "ETH_USDT0",
        "base": "ETH",
        "quote": "USDT0"
    }
]
```

## Response Fields

product_id

u32

No

Unique identifier for the product.

ticker_id

string

No

Identifier of a ticker with delimiter to separate base/target.

base

string

No

Symbol of the base asset.

quote

string

No

Symbol of the target asset.

[PreviousAssets](/developer-resources/api/v2/assets)
[NextAPR](/developer-resources/api/v2/apr)

Last updated1 month ago