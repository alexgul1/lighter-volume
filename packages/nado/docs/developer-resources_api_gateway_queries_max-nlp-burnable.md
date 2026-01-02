---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/max-nlp-burnable
title: Max NLP Burnable
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Max NLP Burnable

Gets the max amount of NLP  burnable possible for a given subaccount.

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
  "type": "max_nlp_burnable",
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=max_nlp_burnable&sender={sender}

`[GATEWAY_REST_ENDPOINT]/query?type=max_nlp_burnable&sender={sender}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "max_nlp_burnable",
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000"
}
```

## Request Parameters

sender

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier.

`bytes32`

## Response

[PreviousMax NLP Mintable](/developer-resources/api/gateway/queries/max-nlp-mintable)
[NextNLP Pool Info](/developer-resources/api/gateway/queries/nlp-pool-info)

Last updated1 month ago