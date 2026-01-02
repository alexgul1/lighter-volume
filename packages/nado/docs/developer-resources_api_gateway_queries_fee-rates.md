---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/fee-rates
title: Fee Rates
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# Fee Rates

Gets all fee rates associated to a subaccount.

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
  "type": "fee_rates",
  "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=fee_rates&sender={sender}

`[GATEWAY_REST_ENDPOINT]/query?type=fee_rates&sender={sender}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Message

```
{
  "type": "fee_rates",
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

- taker_fee_rates_x18: taker fee associated with a given product indexed byproduct_id.Note: this fee represents the basis point (BPS) on a taker order inx18.

taker_fee_rates_x18: taker fee associated with a given product indexed byproduct_id.Note: this fee represents the basis point (BPS) on a taker order inx18.

`taker_fee_rates_x18`
`product_id`
`x18`
- maker_fee_rates_x18: maker fee associated with a given produced indexed byproduct_id.

maker_fee_rates_x18: maker fee associated with a given produced indexed byproduct_id.

`maker_fee_rates_x18`
`product_id`
`.`
- withdraw_sequencer_fees: withdraw fees associated with a given product indexed byproduct_id.Note: this fee represents a fixed amount of product to be deducted as fee inx18.

withdraw_sequencer_fees: withdraw fees associated with a given product indexed byproduct_id.Note: this fee represents a fixed amount of product to be deducted as fee inx18.

`withdraw_sequencer_fees`
`product_id`
`x18`

See ourfeespage for details about current fee rates.

[fees](https://github.com/nadohq/nado-docs/blob/main/docs/basics/fees.md)
[PreviousNLP Locked Balances](/developer-resources/api/gateway/queries/nlp-locked-balances)
[NextHealth Groups](/developer-resources/api/gateway/queries/health-groups)

Last updated1 month ago