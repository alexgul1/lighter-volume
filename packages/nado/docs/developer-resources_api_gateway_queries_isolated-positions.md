---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/isolated-positions
title: Isolated Positions
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Isolated Positions

Get existing open isolated positions for a provided cross subaccount.

## Rate limits

- 240 requests/min or 40 requests every 10 seconds per IP address. (weight = 10)

240 requests/min or 40 requests every 10 seconds per IP address. (weight = 10)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
    "type": "isolated_positions",
    "subaccount": "0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=isolated_positions&subaccount={subaccount}

`[GATEWAY_REST_ENDPOINT]/query?type=isolated_positions&subaccount={subaccount}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
    "type": "isolated_positions",
    "subaccount": "0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000"
}
```

## Request Parameters

subaccount

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier. Seesender field structurefor details.

`bytes32`
[sender field structure](/developer-resources/api/gateway/executes#sender-field-structure)

## Response

Note:

- isolated_positions[i].subaccount: is the isolated subaccount for the base product.

isolated_positions[i].subaccount: is the isolated subaccount for the base product.

`isolated_positions[i].subaccount`
- healths:healths[0]: info about your initial health, which is weighted bylong_weight_initial_x18andshort_weight_initial_x18.healths[1]: info about your maintenance health, which is weighted bylong_weight_maintenance_x18andshort_weight_maintenance_x18.healths[2]: info about your unweighted health.

healths:

`healths`
- healths[0]: info about your initial health, which is weighted bylong_weight_initial_x18andshort_weight_initial_x18.

healths[0]: info about your initial health, which is weighted bylong_weight_initial_x18andshort_weight_initial_x18.

`healths[0]`
`long_weight_initial_x18`
`short_weight_initial_x18.`
- healths[1]: info about your maintenance health, which is weighted bylong_weight_maintenance_x18andshort_weight_maintenance_x18.

healths[1]: info about your maintenance health, which is weighted bylong_weight_maintenance_x18andshort_weight_maintenance_x18.

`healths[1]`
`long_weight_maintenance_x18`
`short_weight_maintenance_x18.`
- healths[2]: info about your unweighted health.

healths[2]: info about your unweighted health.

`healths[2]`
[PreviousSubaccount Info](/developer-resources/api/gateway/queries/subaccount-info)
[NextMarket Liquidity](/developer-resources/api/gateway/queries/market-liquidity)

Last updated1 month ago