---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/order
title: Order
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Order

Gets an order from the orderbook by digest.

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
  "type": "order",
  "product_id": 1,
  "digest": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=order&product_id={product_id}&digest={digest}

`[GATEWAY_REST_ENDPOINT]/query?type=order&product_id={product_id}&digest={digest}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "order",
  "product_id": 1,
  "digest": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
```

## Request Parameters

product_id

number

Yes

Id of spot / perp product for which to retrieve order.

digest

string

Yes

Order digest to retrieve.

## Response

Note: that side of the order (buy/sell) is included in the sign ofamountandunfilled_amount. They are positive if the order is a buy order, otherwise negative.

`amount`
`unfilled_amount`
[PreviousNonces](/developer-resources/api/gateway/queries/nonces)
[NextOrders](/developer-resources/api/gateway/queries/orders)

Last updated1 month ago