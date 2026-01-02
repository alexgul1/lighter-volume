---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/events
title: Events
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Events

Query Nado events by subaccounts, products, event types, etc.

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

## Available Events

Each event corresponds to a transaction type in Nado. See below available events and theirevent_typemapping:

`event_type`

LiquidateSubaccount

`LiquidateSubaccount`

liquidate_subaccount

DepositCollateral

`DepositCollateral`

deposit_collateral

WithdrawCollateral

`WithdrawCollateral`

withdraw_collateral

SettlePnl

`SettlePnl`

settle_pnl

MatchOrders

`MatchOrders`

match_orders

MintLp

`MintLp`

mint_lp

BurnLp

`BurnLp`

burn_lp

## Event Limits

You can specify 2 types oflimiton the query:

`limit`
- raw: the max number of events to return.

raw: the max number of events to return.

`raw`
- txs: the max number of transactions to return.note: one transaction can emit multiple events, by specifying this limit, you will get all the events associated to the transactions in the response.

txs: the max number of transactions to return.note: one transaction can emit multiple events, by specifying this limit, you will get all the events associated to the transactions in the response.

`txs`

## Request

Query events corresponding to specific subaccounts, ordered bysubmission indexdesc. E.g: allMatchOrderevents for subaccountsxxxspecific to spot wBTC.

`submission index`
`MatchOrder`
`xxx`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

Query events corresponding to specific products, ordered bysubmission indexdesc. Usestxslimit, will only return a singletxand one or more events associated with thetx.

`submission index`
`txs`
`tx`
`tx`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

Query events corresponding to specific types, ordered bysubmission indexdesc.

`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

Query all events ordered bysubmission indexdesc.

`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

## Request Parameters

subaccounts

string[]

No

Array ofbytes32sent as hex strings; each includes the address and the subaccount identifier. When provided, only return events for the specified subaccounts.

`bytes32`

product_ids

number[]

No

when provided, only return events for the specified product ids; return events for all products otherwise.

event_types

string[]

No

when provided, only return events for the specified event types; return all events otherwise.

idx

number / string

No

when provided, only return events withsubmission_idx<=idx

`submission_idx`
`idx`

max_time

number / string

No

whenidxis not provided,max_time(unix epoch in seconds) can be used to only return events created <=max_time

`idx`
`max_time`
`max_time`

limit

object
{"raw": number } or

{"txs": number }

No

- specifyingrawlimit: max number of events to return. defaults to100. max possible of500.

specifyingrawlimit: max number of events to return. defaults to100. max possible of500.

`raw`
`100`
`500`
- specifyingtxslimit: max number of txs to return.

specifyingtxslimit: max number of txs to return.

`txs`

isolated

bool

No

When provided --
-true: only returns evens associated to isolated positions.
-false: only return events associated to the cross-subaccount.
defaults tonull. In which case it returns everything.

SeeIsolated Marginto learn more.

`true`
`false`
`null`
[Isolated Margin](https://github.com/nadohq/nado-docs/blob/main/docs/basics/isolated-margin.md)

## Response

Note:

- the response includes atxsfield which contains the relevant transactions to the events. There are>=1 eventsper transaction.

the response includes atxsfield which contains the relevant transactions to the events. There are>=1 eventsper transaction.

`txs`
`>=1 events`
- botheventsandtxsare in descending order bysubmission_idx.

botheventsandtxsare in descending order bysubmission_idx.

`events`
`txs`
`submission_idx`
`.`
- use thesubmission_idxto associate aneventto it's corresponding transaction.

use thesubmission_idxto associate aneventto it's corresponding transaction.

`submission_idx`
`event`

## Response Fields

### Events

- Net cumulative: the net difference in that quantity since the beginning of time. For example, if I want to compute total amount paid out in funding between two events, you can subtract thenet_funding_cumulativeof the larger event by thenet_funding_cumulativeof the smaller event.

Net cumulative: the net difference in that quantity since the beginning of time. For example, if I want to compute total amount paid out in funding between two events, you can subtract thenet_funding_cumulativeof the larger event by thenet_funding_cumulativeof the smaller event.

`net_funding_cumulative`
`net_funding_cumulative`
- Net unrealized: similar tonet_cumulative, but fornet_unrealized, we have the caveat that when the magnitude of your position decreases, the magnitude of net_unrealizeddecreasesby the same amount.

Net unrealized: similar tonet_cumulative, but fornet_unrealized, we have the caveat that when the magnitude of your position decreases, the magnitude of net_unrealizeddecreasesby the same amount.

`net_cumulative`
`net_unrealized`
`decreases`

submission_idx

Used to uniquely identify the blockchain transaction that generated the event; you can use it to grab the relevant transaction in thetxssection.

`txs`

product_id

The id of of the product the event is associated with.

event_type

Name of the transaction type this event corresponds to.

subaccount

The subaccount associated to the event.

pre_balance

The state of your balance before the event happened.

post_balance

The state of your balance after the event happened.

product

The state of the product throughout the event.

### Txs

submission_idx

Unique identifier of the transaction.

product_id

Product associated to the transaction.

tx

Raw data of the corresponding transaction e.g:match_orderswith all associated data.

`match_orders`

timestamp

The unix epoch in seconds of when the transaction took place.

[PreviousMatches](/developer-resources/api/archive-indexer/matches)
[NextCandlesticks](/developer-resources/api/archive-indexer/candlesticks)

Last updated1 month ago