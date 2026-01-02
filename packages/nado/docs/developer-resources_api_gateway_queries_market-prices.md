---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/market-prices
title: Market Prices
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Market Prices

Gets the highest bid and lowest ask price levels from the orderbook for provided products.

## Rate limits

- 2400 requests/min or 40 requests/sec per IP address. (weight = 1) or length ofproduct_idsformulti-product marketsquery.

2400 requests/min or 40 requests/sec per IP address. (weight = 1) or length ofproduct_idsformulti-product marketsquery.

`product_ids`
[multi-product markets](/developer-resources/api/gateway/queries/market-prices#multiple-products)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Single Product

### Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "type": "market_price",
  "product_id": 1
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=market_price&product_id={product_id}

`[GATEWAY_REST_ENDPOINT]/query?type=market_price&product_id={product_id}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "market_price",
  "product_id": 1
}
```

### Request Parameters

product_id

number

Yes

Id of spot / perp product for which to retrieve market price data.

### Response

Note: that price is represented using fixed point, so it is1e18times greater than the decimal price.

`1e18`

## Multiple Products

### Request

Connect

WEBSOCKET [CORE_WEBSOCKET_ENDPOINT]

`WEBSOCKET [CORE_WEBSOCKET_ENDPOINT]`

Message

POST /query

`POST /query`

Body

### Request Parameters

product_ids

number[]

Yes

List of spot / perp products for which to retrieve market price data.

### Response

[PreviousEdge All Products](/developer-resources/api/gateway/queries/edge-all-products)
[NextMax Order Size](/developer-resources/api/gateway/queries/max-order-size)

Last updated1 month ago