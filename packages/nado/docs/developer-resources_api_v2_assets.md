---
url: https://docs.nado.xyz/developer-resources/api/v2/assets
title: Assets
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# Assets

Retrieve details of all available assets on Nado, including trading fees and asset type.

## Rate limits

- 1200 requests/min or 20 requests/sec per IP address. (weight = 2)

1200 requests/min or 20 requests/sec per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

GET[GATEWAY_V2_ENDPOINT]/assets

`[GATEWAY_V2_ENDPOINT]/assets`

## Response

```
[
  {
    "product_id": 0,
    "ticker_id": null,
    "market_type": null,
    "name": "USDT0",
    "symbol": "USDT0",
    "taker_fee": null,
    "maker_fee": null,
    "can_withdraw": true,
    "can_deposit": true
  },
  {
    "product_id": 2,
    "ticker_id": "BTC-PERP_USDT0",
    "market_type": "perp",
    "name": "Bitcoin Perp",
    "symbol": "BTC-PERP",
    "maker_fee": 0.0002,
    "taker_fee": 0,
    "can_withdraw": false,
    "can_deposit": false
  },
  {
    "product_id": 1,
    "ticker_id": "BTC_USDT0",
    "market_type": "spot",
    "name": "Bitcoin",
    "symbol": "BTC",
    "taker_fee": 0.0003,
    "maker_fee": 0,
    "can_withdraw": true,
    "can_deposit": true
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

maker_fee

decimal

No

Fees charged for placing a market-making order on the book.

taker_fee

decimal

No

Fees applied when liquidity is removed from the book.

can_withdraw

boolean

No

Indicates if asset withdrawal is allowed.

can_deposit

boolean

No

Indicates if asset deposit is allowed.

ticker_id

string

Yes

Identifier of a ticker with delimiter to separate base/quote. This isnullfor assets without market e.g:USDT0

`null`
`USDT0`

market_type

string

Yes

Name of market type (spotorperp) of asset. This isnullfor assets without a market e.g:USDT0

`spot`
`perp`
`null`
`USDT0`
[PreviousV2](/developer-resources/api/v2)
[NextPairs](/developer-resources/api/v2/pairs)

Last updated1 month ago