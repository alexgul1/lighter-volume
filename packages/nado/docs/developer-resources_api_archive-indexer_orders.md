---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/orders
title: Orders
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Orders

Query historical orders by subaccounts or order digests.

## Rate limits

- IP weight =2 + (limit * subaccounts.length / 20)wherelimitdefaults to 100 (max 500) andsubaccounts.lengthdefaults to 1

IP weight =2 + (limit * subaccounts.length / 20)wherelimitdefaults to 100 (max 500) andsubaccounts.lengthdefaults to 1

`2 + (limit * subaccounts.length / 20)`
`limit`
`subaccounts.length`

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query subaccountsmatchedorders, ordered bysubmission indexdesc.

`matched`
`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "orders": {
    "product_ids": [
      1,
      2
    ],
    "subaccounts": [
      "0x12a0b4888021576eb10a67616dd3dd3d9ce206b664656661756c740000000000"
    ],
    "max_time": 1679728762,
    "trigger_types": [
      "price_trigger",
      "time_trigger"
    ],
    "isolated": false,
    "limit": 5
  }
}
```

Query orders by digests.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

## Request Parameters

subaccounts

string[]

conditional

Array ofbytes32sent as hex strings; each includes the address and the subaccount identifier. Must be provided when querying bysubaccounts.

`bytes32`
`subaccounts`

product_ids

number[]

No

When provided, only return orders for the specified product ids; return orders for all products otherwise.

idx

number / string

No

When provided, only return orders withsubmission_idx<=idx

`submission_idx`
`idx`

max_time

number / string

No

Whenidxis not provided,max_time(unix epoch in seconds) can be used to only return orders created <=max_time

`idx`
`max_time`
`max_time`

digests

string[]

conditional

Must be provided when querying bydigests. only return orders matching the specified digests.note: cannot specify digests alongside withsubaccounts,product_idsormax_time

`digests`
`subaccounts`
`product_ids`
`max_time`

trigger_types

string[]

No

When provided, only return orders matching the specified trigger types. Possible values:price_trigger,time_trigger,none. If not provided, returns orders of all trigger types.

`price_trigger`
`time_trigger`
`none`

limit

number

No

Max number of orders to return. defaults to100. max possible of500.note: when querying bydigestslimit must be <= total digests provided

`100`
`500`
`digests`

isolated

bool

No

When provided --

- true: only returns orders associated to isolated positions.

true: only returns orders associated to isolated positions.

`true`
- false: only return matches associated to the cross-subaccount.

false: only return matches associated to the cross-subaccount.

`false`

defaults tonull. In which case it returns everything.

`null`

SeeIsolated Marginto learn more.

[Isolated Margin](https://github.com/nadohq/nado-docs/blob/main/docs/basics/isolated-margin.md)

## Response

## Response Fields

digest

The unique hash of the order.

subaccount

The subaccount that placed the order.

product_id

The id of of the product the order was executed for.

submission_idx

Used to uniquely identify the blockchain transaction that generated the order. For multi-fills orders, this is the submission_idx of the first fill.

last_fill_submission_idx

For multi-fills orders, this is the submission_idx of the last fill. For single fill orders, it has the same value assubmission_idx.

`submission_idx`

amount

The original amount of base to buy or sell.

price_x18

The original order price.

base_filled

The total amount of base (e.g: BTC) filled on this order.

quote_filled

The total amount of quote (e.g: USDT0) filled on this order.

fee

The total amount of fee paid on this order.

closed_amount

Total base amount closed by this order (x18).

realized_pnl

Realized PnL from this order (x18).

expiration

The original order expiration.

nonce

The original order nonce.

appendix

The original order appendix.

[PreviousArchive (indexer)](/developer-resources/api/archive-indexer)
[NextMatches](/developer-resources/api/archive-indexer/matches)

Last updated13 days ago