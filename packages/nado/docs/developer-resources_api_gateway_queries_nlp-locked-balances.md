---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/nlp-locked-balances
title: NLP Locked Balances
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# NLP Locked Balances

Gets the locked and unlocked NLP (Nado Liquidity Provider) balances for a given subaccount.

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
  "type": "nlp_locked_balances",
  "subaccount": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=nlp_locked_balances&subaccount={subaccount}

`[GATEWAY_REST_ENDPOINT]/query?type=nlp_locked_balances&subaccount={subaccount}`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
  "type": "nlp_locked_balances",
  "subaccount": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000"
}
```

## Request Parameters

subaccount

string

Yes

Abytes32sent as a hex string; includes the address and the subaccount identifier.

`bytes32`

## Response

## Response Fields

### NLP Locked Balances Response

balance_locked

Total balance that is currently locked (SpotBalance object)

balance_unlocked

Total balance that is currently unlocked and available (SpotBalance object)

locked_balances

Array of individual locked balance entries with their unlock times

### Locked Balance Entry

balance

SpotBalance object containing the locked amount

unlocked_at

Unix epoch timestamp (in seconds) when this balance will unlock

### SpotBalance Object

product_id

The product ID (typically 0 for USDT0/quote asset)

balance

Balance details object

balance.amount

The balance amount in x18 format (string)

balance.last_cumulative_funding_x18

Last cumulative funding value in x18 format (string)

## Notes

- NLP positions have a 4-day lock period after minting before they can be burned (withdrawn)

NLP positions have a 4-day lock period after minting before they can be burned (withdrawn)

- Thelocked_balancesarray shows individual lock entries, each with their own unlock timestamp

Thelocked_balancesarray shows individual lock entries, each with their own unlock timestamp

`locked_balances`
- balance_lockedis the sum of all locked balances

balance_lockedis the sum of all locked balances

`balance_locked`
- balance_unlockedrepresents balances that have passed their lock period and can be withdrawn

balance_unlockedrepresents balances that have passed their lock period and can be withdrawn

`balance_unlocked`
[PreviousNLP Pool Info](/developer-resources/api/gateway/queries/nlp-pool-info)
[NextFee Rates](/developer-resources/api/gateway/queries/fee-rates)

Last updated1 month ago