---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/matches
title: Matches
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Matches

Query historical matches for given subaccounts or provided products.

## Rate limits

- IP weight =2 + (limit * subaccounts.length / 10)wherelimitdefaults to 100 (max 500) andsubaccounts.lengthdefaults to 1E.g: Withlimit=100and 1 subaccount, weight = 12, allowing up to 200 requests per min or 33 requests / 10 secs.

IP weight =2 + (limit * subaccounts.length / 10)wherelimitdefaults to 100 (max 500) andsubaccounts.lengthdefaults to 1

`2 + (limit * subaccounts.length / 10)`
`limit`
`subaccounts.length`
- E.g: Withlimit=100and 1 subaccount, weight = 12, allowing up to 200 requests per min or 33 requests / 10 secs.

E.g: Withlimit=100and 1 subaccount, weight = 12, allowing up to 200 requests per min or 33 requests / 10 secs.

`limit=100`

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query subaccounts matches ordered bysubmission indexdesc. Response includes order fill and fee information.

`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "matches": {
    "product_ids": [
      1,
      2
    ],
    "subaccounts": [
      "0x12a0b4888021576eb10a67616dd3dd3d9ce206b664656661756c740000000000"
    ],
    "max_time": 1679728762,
    "limit": 5,
    "isolated": false
  }
}
```

Query matches for provided products ordered bysubmission indexdesc. Response includes order fill and fee information.

`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "matches": {
    "product_ids": [
      1,
      2
    ],
    "max_time": "1679728762",
    "limit": 5
  }
}
```

## Request Parameters

subaccounts

string[]

No

Array ofbytes32sent as hex strings; each includes the address and the subaccount identifier. When provided, only return matches for the specified subaccounts.

`bytes32`

product_ids

number[]

No

When provided, only return matches for the specified product ids; return matches for all products otherwise.

idx

number / string

No

When provided, only return matches withsubmission_idx<=idx

`submission_idx`
`idx`

max_time

number / string

No

Whenidxis not provided,max_time(unix epoch in seconds) can be used to only return matches created <=max_time

`idx`
`max_time`
`max_time`

limit

number

No

Max number of matches to return. defaults to100. max possible of500.

`100`
`500`

isolated

boolean

No

When provided --
-true: only returns matches associated to isolated positions.
-false: only return matches associated to the cross-subaccount.
defaults tonull. In which case it returns everything.

SeeIsolated Marginto learn more.

`true`
`false`
`null`
[Isolated Margin](https://github.com/nadohq/nado-docs/blob/main/docs/basics/isolated-margin.md)

## Response

Note:

- the response includes atxsfield which contains the relevant transactions for the returned matches. There are>=1 match eventsper transaction.

the response includes atxsfield which contains the relevant transactions for the returned matches. There are>=1 match eventsper transaction.

`txs`
`>=1 match events`
- bothmatchesandtxsare in descending order bysubmission_idx.

bothmatchesandtxsare in descending order bysubmission_idx.

`matches`
`txs`
`submission_idx`
`.`
- use thesubmission_idxto associate a match to it's corresponding transaction.

use thesubmission_idxto associate a match to it's corresponding transaction.

`submission_idx`
- thefeeprovided in the response includes taker / maker fees + sequencer fees. Seefeesfor more details.

thefeeprovided in the response includes taker / maker fees + sequencer fees. Seefeesfor more details.

`fee`
[fees](https://github.com/nadohq/nado-docs/blob/main/docs/basics/fees.md)

## Response Fields

### Matches

submission_idx

Wsed to uniquely identify the blockchain transaction that generated the match; you can use it to grab the relevant transaction in thetxssection.

`txs`

isolated

Whether the match is associated with an isolated position.truefor isolated positions,falsefor cross-subaccount positions.

`true`
`false`

is_taker

Whether the order in this match was the taker.trueif the order was the taker,falseif the order was the maker.

`true`
`false`

digest

The unique hash of the order.

order.sender

The sender that placed the order.

order.priceX18

The original order price.

order.amount

The original order amount.

order.expiration

The original order expiration.

order.nonce

The original order nonce.

order.appendix

The original order appendix.

pre_balance

The state of your balance before the match happened.

post_balance

The state of your balance after the match happened.

base_filled

The amount of base (e.g: BTC) filled on this match.

quote_filled

The amount of quote (e.g: USDT0) filled on this match.

fee

The amount of trading fees + sequencer fees paid on this match.

sequencer_fee

The amount of sequencer fees paid on this match.

cumulative_base_filled

The total amount of base (e.g: BTC) filled on this order up this match.

cumulative_quote_filled

The total amount of quote (e.g: USDT0) filled up to this match.

cumulative_fee

The total amount of fee paid up to this match.

closed_amount

Total base amount closed by this order (x18).

realized_pnl

Realized PnL for this order (x18).

### Txs

submission_idx

Unique identifier of the transaction.

product_id

Product associated to the transaction.

taker

The taker order.

maker

The maker order.

timestamp

The unix epoch in seconds of when the transaction took place.

[PreviousOrders](/developer-resources/api/archive-indexer/orders)
[NextEvents](/developer-resources/api/archive-indexer/events)

Last updated13 days ago