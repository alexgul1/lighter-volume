---
url: https://docs.nado.xyz/developer-resources/api/v2/orderbook
title: Orderbook
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# Orderbook

Retrieve amount of liquidity at each price level for a provided ticker.

## Rate limits

- 2400 requests/min or 40 requests/sec per IP address. (weight = 1)

2400 requests/min or 40 requests/sec per IP address. (weight = 1)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

GET[GATEWAY_V2_ENDPOINT]/orderbook?ticker_id={ticker_id}&depth={depth}

`[GATEWAY_V2_ENDPOINT]/orderbook?ticker_id={ticker_id}&depth={depth}`

## Request Parameters

ticker_id

string

Yes

Identifier of a ticker with delimiter to separate base/target.

depth

number

Yes

Number of price levels to retrieve.

## Response

```
{
    "product_id": 1,
    "ticker_id": "BTC-PERP_USDT0",
    "bids": [
        [
            116215.0,
            0.128
        ],
        [
            116214.0,
            0.172
        ]
    ],
    "asks": [
        [
            116225.0,
            0.043
        ],
        [
            116226.0,
            0.172
        ]
    ],
    "timestamp": 1757913317944
}
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

bids

decimal[]

No

An array containing 2 elements. The offer price (first element) and quantity for each bid order (second element).

asks

decimal[]

No

An array containing 2 elements. The ask price (first element) and quantity for each ask order (second element).

timestamp

integer

No

Unix timestamp in milliseconds for when the last updated time occurred.

[PreviousAPR](/developer-resources/api/v2/apr)
[NextTickers](/developer-resources/api/v2/tickers)

Last updated1 month ago