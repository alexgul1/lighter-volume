---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/sequencer-backlog
title: Sequencer Backlog
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Sequencer Backlog

Query off-chain sequencer backlog metrics

## Rate limits

- 2400 requests/min or 400 requests/10secs per IP address. (weight = 1)

2400 requests/min or 400 requests/10secs per IP address. (weight = 1)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "backlog": {}
}
```

## Response

```
{
    "total_txs": "45479039",
    "total_submissions": "45478914",
    "backlog_size": "125",
    "updated_at": "1750365790",
    "backlog_eta_in_seconds": "500",
    "txs_per_second": "0.25"
}
```

### Response Fields

total_txs

Total number of transactions stored in the indexer DB.

total_submissions

Total number of transactions submitted on-chain.

backlog_size

Number of unprocessed transactions (total_txs - total_submissions).

`total_txs - total_submissions`

backlog_eta_in_seconds

Estimated time in seconds (float) to clear the entire backlog (nullif unavailable).

`float`
`null`

txs_per_second

Current submission rate in transactions per second (float) (nullif unavailable).

`null`

updated_at

UNIX timestamp (in seconds) of when the data was last updated.

[PreviousLiquidation Feed](/developer-resources/api/archive-indexer/liquidation-feed)
[NextDirect Deposit Address](/developer-resources/api/archive-indexer/direct-deposit-address)

Last updated1 month ago