---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/contracts
title: Contracts
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Contracts

Get information about core Nado contracts.

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
  "type": "contracts"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=contracts

`[GATEWAY_REST_ENDPOINT]/query?type=contracts`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "contracts"
}
```

## Response

```
{
    "status": "success",
    "data": {
        "chain_id": "763373",
        "endpoint_addr": "0xf8963f7860af7de9b94893edb9a3b5c155e1fc0c"
    },
    "request_type": "query_contracts"
}
```

Note:

- endpoint_addris the address of the Nado endpoint contracts. Deposits are sent to the endpoint address;this to used sign every request exceptPlaceOrder

endpoint_addris the address of the Nado endpoint contracts. Deposits are sent to the endpoint address;this to used sign every request exceptPlaceOrder

`endpoint_addr`
`PlaceOrder`
[PreviousStatus](/developer-resources/api/gateway/queries/status)
[NextNonces](/developer-resources/api/gateway/queries/nonces)

Last updated1 month ago