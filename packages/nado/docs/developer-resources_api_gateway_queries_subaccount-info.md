---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/subaccount-info
title: Subaccount Info
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Subaccount Info

Get balances associated with a specific subaccount and all products.

## Rate limits

The rate limit weight varies based on the request parameters:

- Basic query(notxns):weight = 21200 requests/min or 200 requests every 10 seconds per IP address

Basic query(notxns):weight = 2

`txns`
- 1200 requests/min or 200 requests every 10 seconds per IP address

1200 requests/min or 200 requests every 10 seconds per IP address

- With simulation(txnsprovided):weight = 10240 requests/min or 40 requests every 10 seconds per IP address

With simulation(txnsprovided):weight = 10

`txns`
- 240 requests/min or 40 requests every 10 seconds per IP address

240 requests/min or 40 requests every 10 seconds per IP address

- With simulation + pre_state(txnsandpre_state="true"):weight = 15160 requests/min or ~26 requests every 10 seconds per IP address

With simulation + pre_state(txnsandpre_state="true"):weight = 15

`txns`
`pre_state="true"`
- 160 requests/min or ~26 requests every 10 seconds per IP address

160 requests/min or ~26 requests every 10 seconds per IP address

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
    "type": "subaccount_info",
    "subaccount": "0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000",
    "txns": "[{\"apply_delta\":{\"product_id\":4,\"subaccount\":\"0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000\",\"amount_delta\":\"10790000000000000000\",\"v_quote_delta\":\"-35380410000000000000000\"}}]"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=subaccount_info&subaccount={subaccount}&txns=[{"apply_delta":{"product_id":2,"subaccount":"0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000","amount_delta":"100000000000000000","v_quote_delta":"3033500000000000000000"}}]

`[GATEWAY_REST_ENDPOINT]/query?type=subaccount_info&subaccount={subaccount}&txns=[{"apply_delta":{"product_id":2,"subaccount":"0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000","amount_delta":"100000000000000000","v_quote_delta":"3033500000000000000000"}}]`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
    "type": "subaccount_info",
    "subaccount": "0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000",
    "txns": "[{\"apply_delta\":{\"product_id\":4,\"subaccount\":\"0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000\",\"amount_delta\":\"10790000000000000000\",\"v_quote_delta\":\"-35380410000000000000000\"}}]"
}
```

## Request Parameters

subaccount

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier. Seesender field structurefor details.

`bytes32`
[sender field structure](/developer-resources/api/gateway/executes#sender-field-structure)

txns

string

no

A list of transactions to get an estimated/simulated view. see more info below.

pre_state

string

no

When"true"andtxnsare provided, returns the subaccount state before the transactions were applied in thepre_statefield. Defaults to"false".

`"true"`
`txns`
`pre_state`
`"false"`

### Supported txs for an estimated subaccount info

The following are the supportedtxnsyou can provide to get an estimated view of your subaccount.

`txns`

Note: thesetxnsare only used to simulate what your subaccount would look like if they were executed.

`txns`

#### ApplyDelta

Updates internal balances for theproduct_idand amount deltas provided.

`product_id`

## Response

Note:

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
- health_contributionsis indexed byproduct_idand represents the contribution of the corresponding product to the final health.health_contributions[product_id][0]: contribution to healths[0]health_contributions[product_id][1]: contribution to healths[1]health_contributions[product_id][2]: contribution to healths[2]

health_contributionsis indexed byproduct_idand represents the contribution of the corresponding product to the final health.

`health_contributions`
- health_contributions[product_id][0]: contribution to healths[0]

health_contributions[product_id][0]: contribution to healths[0]

`health_contributions[product_id][0]`
`: contribution to healths[0]`
- health_contributions[product_id][1]: contribution to healths[1]

health_contributions[product_id][1]: contribution to healths[1]

`health_contributions[product_id][1]`
`: contribution to healths[1]`
- health_contributions[product_id][2]: contribution to healths[2]

health_contributions[product_id][2]: contribution to healths[2]

`health_contributions[product_id][2]`
`: contribution to healths[2]`
- pre_state: (Optional) Whenpre_state="true"is provided withtxns, this field contains the subaccount statebeforethe simulated transactions were applied. This allows you to compare the before/after states when simulating transactions.pre_state.healths: Same structure as the mainhealthsfield, but reflecting the state before transactionspre_state.health_contributions: Health contributions before transactionspre_state.spot_balances: Spot balances before transactionspre_state.perp_balances: Perpetual balances before transactions

pre_state: (Optional) Whenpre_state="true"is provided withtxns, this field contains the subaccount statebeforethe simulated transactions were applied. This allows you to compare the before/after states when simulating transactions.

`pre_state`
`pre_state="true"`
`txns`
- pre_state.healths: Same structure as the mainhealthsfield, but reflecting the state before transactions

pre_state.healths: Same structure as the mainhealthsfield, but reflecting the state before transactions

`pre_state.healths`
`healths`
- pre_state.health_contributions: Health contributions before transactions

pre_state.health_contributions: Health contributions before transactions

`pre_state.health_contributions`
- pre_state.spot_balances: Spot balances before transactions

pre_state.spot_balances: Spot balances before transactions

`pre_state.spot_balances`
- pre_state.perp_balances: Perpetual balances before transactions

pre_state.perp_balances: Perpetual balances before transactions

`pre_state.perp_balances`

### Example withpre_state

`pre_state`

When you want to simulate transactions and compare the before/after states, you can use thepre_stateparameter:

`pre_state`

#### Request

GET[GATEWAY_REST_ENDPOINT]/query?type=subaccount_info&subaccount={subaccount}&txns=[{"apply_delta":{"product_id":2,"subaccount":"0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000","amount_delta":"100000000000000000","v_quote_delta":"3033500000000000000000"}}]&pre_state="true"

`[GATEWAY_REST_ENDPOINT]/query?type=subaccount_info&subaccount={subaccount}&txns=[{"apply_delta":{"product_id":2,"subaccount":"0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000","amount_delta":"100000000000000000","v_quote_delta":"3033500000000000000000"}}]&pre_state="true"`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

#### Response

The response will now include apre_statefield showing the state before the simulated transactions:

`pre_state`

Use Case: Thepre_statefeature is particularly useful for:

`pre_state`
- Position Simulation: Preview how a potential trade would affect your health and balances

Position Simulation: Preview how a potential trade would affect your health and balances

- Risk Analysis: Compare health metrics before and after simulated transactions

Risk Analysis: Compare health metrics before and after simulated transactions

- UI/UX: Display "before → after" views to users when they're about to execute trades

UI/UX: Display "before → after" views to users when they're about to execute trades

- Testing: Validate transaction impacts without executing them on-chain

Testing: Validate transaction impacts without executing them on-chain

[PreviousOrders](/developer-resources/api/gateway/queries/orders)
[NextIsolated Positions](/developer-resources/api/gateway/queries/isolated-positions)

Last updated1 month ago