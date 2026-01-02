---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/nlp-snapshots
title: NLP Snapshots
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# NLP Snapshots

Query NLP (Nado Liquidity Provider) pool snapshots

## Rate limits

- Dynamic based on snapshot count (weight = (limit.min(500) / 100))E.g: Withlimit=100, weight = 1E.g: Withlimit=500, weight = 5

Dynamic based on snapshot count (weight = (limit.min(500) / 100))

- E.g: Withlimit=100, weight = 1

E.g: Withlimit=100, weight = 1

`limit=100`
- E.g: Withlimit=500, weight = 5

E.g: Withlimit=500, weight = 5

`limit=500`

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query NLP snapshots at specific time intervals.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "nlp_snapshots": {
    "interval": {
      "count": 10,
      "max_time": "1683315718",
      "granularity": 3600
    }
  }
}
```

Query NLP snapshots with pagination.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "nlp_snapshots": {
    "idx": "12345",
    "max_time": "1683315718",
    "limit": 100
  }
}
```

## Request Parameters

interval

object

No

Object specifying time interval parameters:count,max_time,granularity

`count`
`max_time`
`granularity`

idx

number / string

No

Submission index for pagination.

max_time

number / string

No

Unix epoch time in seconds. Only return snapshots with timestamp <=max_time

`max_time`

limit

number

No

Max number of snapshots to return. Defaults to100. Max of500.

`100`
`500`

## Response

## Response Fields

### NLP Snapshots

submission_idx

Transaction submission index

timestamp

Unix epoch time in seconds when snapshot was taken

total_deposits

Total deposits in the NLP pool (x18 format)

total_borrows

Total borrows from the NLP pool (x18 format)

base_interest_rate

Interest rate for base assets (x18 format)

quote_interest_rate

Interest rate for quote assets (x18 format)

[PreviousNLP Interest Payments](/developer-resources/api/archive-indexer/nlp-interest-payments)
[NextLiquidation Feed](/developer-resources/api/archive-indexer/liquidation-feed)

Last updated1 month ago