---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/oracle-snapshots
title: Oracle Snapshots
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Oracle Snapshots

Query historical oracle prices.

## Rate limits

- IP weight =max((snapshot_count * product_ids.length / 100), 2)wheresnapshot_count = interval.count.min(500). If noproduct_idsare specified,product_ids.length = 100.E.g: Withproduct_ids=[1, 2, 3, 4]andinterval.count=60, weight = max((60 * 4 / 100), 2) = 2, allowing up to 1200 requests per min or 200 requests/10 secs.

IP weight =max((snapshot_count * product_ids.length / 100), 2)wheresnapshot_count = interval.count.min(500). If noproduct_idsare specified,product_ids.length = 100.

`max((snapshot_count * product_ids.length / 100), 2)`
`snapshot_count = interval.count.min(500)`
`product_ids`
`product_ids.length = 100`
- E.g: Withproduct_ids=[1, 2, 3, 4]andinterval.count=60, weight = max((60 * 4 / 100), 2) = 2, allowing up to 1200 requests per min or 200 requests/10 secs.

E.g: Withproduct_ids=[1, 2, 3, 4]andinterval.count=60, weight = max((60 * 4 / 100), 2) = 2, allowing up to 1200 requests per min or 200 requests/10 secs.

`product_ids=[1, 2, 3, 4]`
`interval.count=60`

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query oracle snapshots ordered bytimestampdesc.

`timestamp`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
    "oracle_snapshots": {
        "interval": {
          "count": 2,
          "granularity": 3600,
          "max_time": 1691083697,
        },
        "product_ids": [1, 2]
    }
}
```

### Request Parameters

interval

object

Yes

Object to specify desired time period for data

interval.count

number

Yes

Number of snapshots to return, limit 100. Also limited tointerval.count * # product_ids < 2000

`interval.count * # product_ids < 2000`

interval.granularity

number

Yes

Granularity value in seconds

interval.max_time

number / string

No

When providingmax_time(unix epoch in seconds), only return snapshots with timestamp <=max_time. If no value is entered,max_timedefaults to the current time.

`max_time`
`max_time`
`max_time`

product_ids

number[]

No

list of product ids to fetch snapshots for, defaults to all products

## Response

Note: Returns a map ofproduct_id -> oracle_price

`product_id -> oracle_price`
[PreviousOracle Price](/developer-resources/api/archive-indexer/oracle-price)
[NextPerp Prices](/developer-resources/api/archive-indexer/perp-prices)

Last updated1 month ago