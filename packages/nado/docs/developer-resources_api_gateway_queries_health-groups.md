---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/health-groups
title: Health Groups
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Health Groups

Gets all available health groups.

Note: a health group is a perp and spot product whose health is calculated together (e.g. BTC and BTC-PERP).

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
  "type": "health_groups"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=health_groups

`[GATEWAY_REST_ENDPOINT]/query?type=health_groups`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
  "type": "health_groups"
}
```

## Response

```
{
    "status": "success",
    "data": {
        "health_groups": [
            [
                1,
                2
            ]
        ]
    },
    "request_type": "query_health_groups"
}
```

- health_groups: list of all available health groups.Note:health_groups[i]is the spot / perp product pair of health groupiwherehealth_groups[i][0]is the spotproduct_idandhealth_groups[i][1]is the perpproduct_id. Additionally, it is possible for a health group to only have either a spot or perp product, in which case, the product that doesn’t exist is set to0.

health_groups: list of all available health groups.Note:health_groups[i]is the spot / perp product pair of health groupiwherehealth_groups[i][0]is the spotproduct_idandhealth_groups[i][1]is the perpproduct_id. Additionally, it is possible for a health group to only have either a spot or perp product, in which case, the product that doesn’t exist is set to0.

`health_groups`
`health_groups[i]`
`i`
`health_groups[i][0]`
`product_id`
`health_groups[i][1]`
`product_id`
`0`
[PreviousFee Rates](/developer-resources/api/gateway/queries/fee-rates)
[NextLinked Signer](/developer-resources/api/gateway/queries/linked-signer)

Last updated1 month ago