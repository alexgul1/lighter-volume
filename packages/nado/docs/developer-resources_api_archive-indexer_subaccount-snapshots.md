---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/subaccount-snapshots
title: Subaccount Snapshots
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Subaccount Snapshots

Query latest subaccount snapshots.

Use this query to get a summary of the latest actions per product on Nado for provided subaccounts. Tracked variables (ex. net interest) are extrapolated to the timestamp or set of timestamps provided.

## Rate limits

- 480 requests/min or 80 requests/10secs per IP address. (weight = 5)

480 requests/min or 80 requests/10secs per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query latest subaccount events/actions ordered bysubmission indexdesc.

`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
    "account_snapshots": {
        "subaccounts": [
            "0xec132d41e542c7129268d9d4431f105e0830a81164656661756c745f31000000"
        ],
        "timestamps": [
            1738703761
        ],
        "isolated": false,
        "active": true
    }
}
```

## Request Parameters

subaccounts

array

Yes

A list ofbytes32sent as a hex string; includes the address and the subaccount identifier.

`bytes32`

timestamp

array

Yes

A list of timestamps to retrieve multiple subaccount snapshots (one per timestamp).

isolated

boolean

No

A filter to include only isolated or cross margin events.

- Iftrue: returns onlyisolatedmargin events.

Iftrue: returns onlyisolatedmargin events.

`true`
- Iffalse: returns onlycrossmargin events.

Iffalse: returns onlycrossmargin events.

`false`
- If omitted: returnsbothisolated and cross events.

If omitted: returnsbothisolated and cross events.

active

boolean

No

Filters which products to include in the snapshot:

- true: returns only products withnon-zero balanceat the timestamp (currently active positions)

true: returns only products withnon-zero balanceat the timestamp (currently active positions)

`true`
- false: returns products withevent historybefore the timestamp (any historical activity)

false: returns products withevent historybefore the timestamp (any historical activity)

`false`
- If omitted: defaults tofalse

If omitted: defaults tofalse

`false`

## Response

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

[PreviousSubaccounts](/developer-resources/api/archive-indexer/subaccounts)
[NextLinked Signers](/developer-resources/api/archive-indexer/linked-signers)

Last updated1 month ago