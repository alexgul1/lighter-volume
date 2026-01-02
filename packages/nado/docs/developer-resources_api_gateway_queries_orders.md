---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/orders
title: Orders
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Orders

Get all open orders associated with a subaccount.

## Rate limits

- 1200 requests/min or 20 requests/sec per IP address. (weight = 2) or 2 * length ofproduct_idsformulti-product ordersquery.

1200 requests/min or 20 requests/sec per IP address. (weight = 2) or 2 * length ofproduct_idsformulti-product ordersquery.

`product_ids`
[multi-product orders](/developer-resources/api/gateway/queries/orders#multiple-products)

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
  "type": "subaccount_orders",
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "product_id": 1
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=subaccount_orders&sender={sender}&product_id={product_id}

`[GATEWAY_REST_ENDPOINT]/query?type=subaccount_orders&sender={sender}&product_id={product_id}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "subaccount_orders",
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "product_id": 1
}
```

### Request Parameters

sender

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier.

`bytes32`

product_id

number

Yes

Id of spot / perp product for which to retrieve subaccount orders.

### Response

Note: that side of the order (buy/sell) is included in the sign ofamountandunfilled_amount. They are positive if the order is a buy order, otherwise negative.

`amount`
`unfilled_amount`

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

sender

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier.

`bytes32`

product_ids

number[]

Yes

List of spot / perp products for which to retrieve open orders.

### Response

[PreviousOrder](/developer-resources/api/gateway/queries/order)
[NextSubaccount Info](/developer-resources/api/gateway/queries/subaccount-info)

Last updated1 month ago