---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/liquidation-feed
title: Liquidation Feed
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Liquidation Feed

Query subaccounts that can be liquidated.

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Queries liquidatable accounts.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "liquidation_feed": {}
}
```

## Response

```
[
  {
    "subaccount": "0xf2b7cec33cac30582b94979bf03a3cbc73954b2c64656661756c740000000000",
    "update_time": 1680118943
  },
  {
    "subaccount": "0xcb6f1e2ece124a150dcc681c180df2a890432d6a64656661756c740000000000",
    "update_time": 1680118943
  },
  {
    "subaccount": "0x9e6e13be7ea2866c2c7c6e4a118a6c05eee6b44e64656661756c740000000000",
    "update_time": 1680118943
  },
  {
    "subaccount": "0x75008754ffae2889c055961c1b0c5c3ab743c59664656661756c740000000000",
    "update_time": 1680118943
  }
]
```

## Response Fields

subaccount

Subaccount eligible for liquidation.

update_time

Last time feed was updated.

[PreviousNLP Snapshots](/developer-resources/api/archive-indexer/nlp-snapshots)
[NextSequencer Backlog](/developer-resources/api/archive-indexer/sequencer-backlog)

Last updated1 month ago