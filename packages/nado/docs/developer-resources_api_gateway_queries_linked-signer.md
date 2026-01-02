---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/linked-signer
title: Linked Signer
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Linked Signer

Retrieves current linked signer of a provided subaccount

## Rate limits

- 480 requests/min or 8 requests/sec per IP address. (weight = 5)

480 requests/min or 8 requests/sec per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "type": "linked_signer",
  "subaccount": "0x9b9989a4E0b260B84a5f367d636298a8bfFb7a9b42544353504f540000000000"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=linked_signer&subaccount=0x9b9989a4E0b260B84a5f367d636298a8bfFb7a9b42544353504f540000000000

`[GATEWAY_REST_ENDPOINT]/query?type=linked_signer&subaccount=0x9b9989a4E0b260B84a5f367d636298a8bfFb7a9b42544353504f540000000000`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
  "type": "linked_signer",
  "subaccount": "0x9b9989a4E0b260B84a5f367d636298a8bfFb7a9b42544353504f540000000000"
}
```

## Response

```
{
  "status": "success",
  "data": {
    "linked_signer": "0x0000000000000000000000000000000000000000"
  },
  "request_type": "query_linked_signer",
}
```

Notes:

- linked_signer: the current linked signer address (20 bytes) associated to the providedsubaccount. It returns the zero address when no signer is linked.

linked_signer: the current linked signer address (20 bytes) associated to the providedsubaccount. It returns the zero address when no signer is linked.

`linked_signer`
`subaccount`
[PreviousHealth Groups](/developer-resources/api/gateway/queries/health-groups)
[NextInsurance](/developer-resources/api/gateway/queries/insurance)

Last updated1 month ago