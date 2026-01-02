---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/market-liquidity
title: Market Liquidity
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Market Liquidity

Gets the amount of liquidity at each price level.

## Rate limits

- 2400 requests/min or 40 requests/sec per IP address. (weight = 1)

2400 requests/min or 40 requests/sec per IP address. (weight = 1)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "type": "market_liquidity",
  "product_id": 1,
  "depth": 10
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=market_liquidity&product_id={product_id}&depth={depth}

`[GATEWAY_REST_ENDPOINT]/query?type=market_liquidity&product_id={product_id}&depth={depth}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "market_liquidity",
  "product_id": 1,
  "depth": 10
}
```

## Request Parameters

product_id

number

Yes

Id of spot / perp product for which to retrieve market liquidity.

depth

number

Yes

Number of price levels to retrieve. (max: 100)

`max: 100`

## Response

Note:

- Each entry inside bids and asks is an array of price and size respectively.Note: that price is represented using fixed point, so it is1e18times greater than the decimal price.

Each entry inside bids and asks is an array of price and size respectively.Note: that price is represented using fixed point, so it is1e18times greater than the decimal price.

`1e18`
- timestampis in nanoseconds.

timestampis in nanoseconds.

`timestamp`
[PreviousIsolated Positions](/developer-resources/api/gateway/queries/isolated-positions)
[NextSymbols](/developer-resources/api/gateway/queries/symbols)

Last updated1 month ago