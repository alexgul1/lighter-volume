---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/status
title: Status
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Status

Gets status of offchain sequencer.

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
  "type": "status"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=status

`[GATEWAY_REST_ENDPOINT]/query?type=status`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "status"
}
```

## Response

```
{
  "status": "success",
  "data": "active",
  "request_type": "query_status",
}
```

The offchain sequencer could be in any of the following statuses:

- active: accepting incoming executes.

active: accepting incoming executes.

`active`
- failed: sequencer is in a failed state.

failed: sequencer is in a failed state.

`failed`
[PreviousQueries](/developer-resources/api/gateway/queries)
[NextContracts](/developer-resources/api/gateway/queries/contracts)

Last updated1 month ago