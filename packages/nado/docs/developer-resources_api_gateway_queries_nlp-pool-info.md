---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/nlp-pool-info
title: NLP Pool Info
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# NLP Pool Info

Gets information about all NLP (Nado Liquidity Provider) pools.

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
  "type": "nlp_pool_info"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=nlp_pool_info

`[GATEWAY_REST_ENDPOINT]/query?type=nlp_pool_info`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "nlp_pool_info"
}
```

## Request Parameters

This query does not require any parameters.

## Response

```
{
  "status": "success",
  "data": {
    "nlp_pools": [
      {
        "pool_id": 1,
        "subaccount": "0x0000000000000000000000000000000000000000000000000000000000000002",
        "owner": "0x1234567890123456789012345678901234567890",
        "balance_weight_x18": "500000000000000000",
        "subaccount_info": {
          "subaccount": "0x0000000000000000000000000000000000000000000000000000000000000002",
          "exists": true,
          "health": {
            "assets": "1000000000000000000000",
            "liabilities": "500000000000000000000",
            "initial_health": "250000000000000000000",
            "maintenance_health": "100000000000000000000"
          },
          "spot_balances": [],
          "perp_balances": []
        },
        "open_orders": []
      }
    ]
  },
  "request_type": "query_nlp_pool_info"
}
```

## Response Fields

### NLP Pool Info

nlp_pools

Array of NLP pool objects

### NLP Pool Object

pool_id

Unique identifier for the pool

subaccount

The subaccount address associated with this pool (bytes32 hex string)

owner

The owner address of the pool (bytes20 hex string)

balance_weight_x18

Weight of this pool's balance in x18 format (string representation of u128)

subaccount_info

Complete subaccount information including health, balances, and positions

open_orders

Array of currently open orders for this pool

[PreviousMax NLP Burnable](/developer-resources/api/gateway/queries/max-nlp-burnable)
[NextNLP Locked Balances](/developer-resources/api/gateway/queries/nlp-locked-balances)

Last updated1 month ago