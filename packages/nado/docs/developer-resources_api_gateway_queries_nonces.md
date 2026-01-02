---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/nonces
title: Nonces
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Nonces

Get execute nonces for a particular address.

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
  "type": "nonces",
  "address": "0x0000000000000000000000000000000000000000"
}
```

GGET[GATEWAY_REST_ENDPOINT]/query?type=nonces&address={address}

`[GATEWAY_REST_ENDPOINT]/query?type=nonces&address={address}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "nonces",
  "address": "0x0000000000000000000000000000000000000000"
}
```

## Request Parameters

address

string

Yes

Abytes20sent as a hex string representing the wallet address.

`bytes20`

## Response

Note: when doing any execute that is notplace_orders, i.e.withdraw_collateral,liquidate_subaccount, you want to usetx_nonceas the nonce.tx_nonceincrements by one each time a successful execute goes through.order_nonceis a historical artifact for the frontend, and simply returns the current timestamp in milliseconds plus 100000 multiplied by 2**20.

`place_orders`
`withdraw_collateral`
`liquidate_subaccount`
`tx_nonce`
`tx_nonce`
`order_nonce`
[PreviousContracts](/developer-resources/api/gateway/queries/contracts)
[NextOrder](/developer-resources/api/gateway/queries/order)

Last updated1 month ago