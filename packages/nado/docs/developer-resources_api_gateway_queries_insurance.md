---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/insurance
title: Insurance
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Insurance

Retrieve current value of Nado's Insurance fund

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
  "type": "insurance"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=insurance

`[GATEWAY_REST_ENDPOINT]/query?type=insurance`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
  "type": "insurance"
}
```

## Response

```
{
    "status": "success",
    "data": {
        "insurance": "552843342443351553629462"
    },
    "request_type": "query_insurance"
}
```

[PreviousLinked Signer](/developer-resources/api/gateway/queries/linked-signer)
[NextSigning](/developer-resources/api/gateway/signing)

Last updated1 month ago