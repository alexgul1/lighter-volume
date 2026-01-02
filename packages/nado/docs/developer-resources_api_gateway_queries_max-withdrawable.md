---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/max-withdrawable
title: Max Withdrawable
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Max Withdrawable

Gets the max amount withdrawable possible of a given spot product for a subaccount.

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
  "type": "max_withdrawable",
  "product_id": 1,
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "spot_leverage": "true"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=max_withdrawable&product_id={product_id}&sender={sender}

`[GATEWAY_REST_ENDPOINT]/query?type=max_withdrawable&product_id={product_id}&sender={sender}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
  "type": "max_withdrawable",
  "product_id": 1,
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "spot_leverage": "true"
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

Id of spot / perp product for which to retrieve max withdrawable amount.

spot_leverage

string

No

Boolean sent as a string. Indicates whether leverage should be used; when set tofalse, returns the max withdrawable amount possible without borrow. Defaults totrue

`false`
`true`

## Response

[PreviousMax Order Size](/developer-resources/api/gateway/queries/max-order-size)
[NextMax NLP Mintable](/developer-resources/api/gateway/queries/max-nlp-mintable)

Last updated1 month ago