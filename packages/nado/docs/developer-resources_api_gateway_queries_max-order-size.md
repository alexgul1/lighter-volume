---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/max-order-size
title: Max Order Size
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Max Order Size

Gets the max order size possible of a given product for a given subaccount.

## Rate limits

- 480 requests/min or 80 requests every 10 seconds per IP address. (weight = 5)

480 requests/min or 80 requests every 10 seconds per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "type": "max_order_size",
  "product_id": 1,
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "price_x18": "23000000000000000000000",
  "direction": "short",
  "spot_leverage": "true",
  "reduce_only": "false",
  "isolated": "false"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=max_order_size&product_id={product_id}&sender={sender}&price_x18={price_x18}&direction={direction}

`[GATEWAY_REST_ENDPOINT]/query?type=max_order_size&product_id={product_id}&sender={sender}&price_x18={price_x18}&direction={direction}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "max_order_size",
  "product_id": 1,
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "price_x18": "23000000000000000000000",
  "direction": "short",
  "spot_leverage": "true",
  "reduce_only": "false",
  "isolated": "false"
}
```

## Request Parameters

sender

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier.

`bytes32`

product_id

number

Yes

Id of spot / perp product for which to retrieve max order size.

price_x18

string

Yes

Anint128representing the price of the order multiplied by 1e18, sent as a string. For example, a price of 1 USDT0 would be sent as"1000000000000000000"

`int128`
`"1000000000000000000"`

direction

string

Yes

longfor max bid orshortfor max ask.

`long`
`short`

spot_leverage

string

No

Boolean sent as a string. Indicates whether leverage should be used; when set tofalse, returns the max order possible without borrow. Defaults totrue

`false`
`true`

reduce_only

string

No

Boolean sent as a string. Indicates wether to retrieve the max order size to close / reduce a position. Defaults tofalse

`false`

isolated

string

No

Boolean sent as a string. When set totrue, calculates max order size for an isolated margin position. Defaults tofalse. SeeIsolated Marginto learn more.

`true`
`false`
[Isolated Margin](https://github.com/nadohq/nado-docs/blob/main/docs/basics/isolated-margin.md)

## Response

[PreviousMarket Prices](/developer-resources/api/gateway/queries/market-prices)
[NextMax Withdrawable](/developer-resources/api/gateway/queries/max-withdrawable)

Last updated1 month ago