---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/symbols
title: Symbols
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Symbols

Get info about available symbols and product configuration

## Rate limits

- 1200 requests/min or 20 requests/sec per IP address. (weight = 2)

1200 requests/min or 20 requests/sec per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "type": "symbols",
  "product_ids": [1, 2]
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=symbols&product_type=spot

`[GATEWAY_REST_ENDPOINT]/query?type=symbols&product_type=spot`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
  "type": "symbols",
  "product_ids": [1, 2, 3, 4],
  "product_type": "spot"
}
```

## Request Parameters

product_ids

number[]

No

An array of product ids. Only available for POST and WS requests.

product_type

string

No

Type of products to return, must be:
"spot" | "perp".

## Response

Note:

- All products have are quoted against USDT0, except for product 0.

All products have are quoted against USDT0, except for product 0.

## Response fields

### Symbols

All numerical values are returned as strings and scaled by 1e18.

type

Product type, "spot" or "perp"

product_id

Product id

symbol

Product symbol

price_increment_x18

Price increment, a.k.a tick size

size_increment

Size increment, in base units

min_size

Minimum order size, in base units

maker_fee_rate_x18

Maker fee rate, given as decimal rate

taker_fee_rate_x18

Taker fee rate, given as decimal rate

long_weight_initial_x18

Long initial margin weight, given as decimal

long_weight_maintenance_x18

Long maintenance margin weight, given as decimal

max_open_interest_x18

Maximum open interest, null if no limit

[PreviousMarket Liquidity](/developer-resources/api/gateway/queries/market-liquidity)
[NextAll Products](/developer-resources/api/gateway/queries/all-products)

Last updated1 month ago