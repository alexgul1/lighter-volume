---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/max-nlp-mintable
title: Max NLP Mintable
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Max NLP Mintable

Gets the max amount of NLP mintable possible for a given subaccount.

## Rate limits

- 120 requests/min or 20 requests every 10 seconds per IP address. (weight = 20)

120 requests/min or 20 requests every 10 seconds per IP address. (weight = 20)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "type": "max_nlp_mintable",
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000",
  "spot_leverage": "true"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=max_nlp_mintable&sender={sender}

`[GATEWAY_REST_ENDPOINT]/query?type=max_nlp_mintable&sender={sender}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "max_nlp_mintable",
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

spot_leverage

boolean

No

Boolean sent as a string. indicates whether leverage should be used; when set tofalse, returns the max amount of base LP mintable possible without borrow. Defaults totrue

`false`
`true`

## Response

[PreviousMax Withdrawable](/developer-resources/api/gateway/queries/max-withdrawable)
[NextMax NLP Burnable](/developer-resources/api/gateway/queries/max-nlp-burnable)

Last updated1 month ago