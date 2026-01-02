---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/market-snapshots
title: Market Snapshots
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Market Snapshots

Query historical market snapshots.

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

### Request

Query market snapshots ordered bytimestampdesc.

`timestamp`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
    "market_snapshots": {
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

### Response

Note: Please note that this endpoint is currently in beta stage. This feature might be subject to changes without prior notice.

### Response Fields

#### Snapshots

Note: For product specific fields (i.e. cumulative_volume, open_interests), the value is an object which maps product_ids to their corresponding values.

timestamp

Timestamp of the snapshot. This may not be perfectly rounded to the granularity since it uses the nearest transaction timestamp less than or equal tomax_time

`max_time`

cumulative_users

The cumulative number of subaccounts on Nado. It is updated daily at 9AM ET for historical counts. For current day counts, it is updated every hour.

daily_active_users

Daily active users count, updated daily at 9AM ET for historical counts. For current day counts, it is updated every hour.

cumulative_trades

A map of product_id -> the cumulative number of trades for the given product_id.

cumulative_volumes

A map of product_id -> cumulative volumes in USDT0 units.

cumulative_trade_sizes

A map of product_id -> cumulative trade sizes in base token

cumulative_taker_fees

A map of product_id -> cumulative taker fees. Taker fees include sequencer fees.

cumulative_sequencer_fees

A map of product_id -> cumulative sequencer fees.

cumulative_maker_fees

A map of product_id -> cumulative maker rebates.

cumulative_liquidation_amounts

A map of product_id -> cumulative liquidation amounts in USDT0 units.

open_interests

A map of product_id -> open interests in USDT0 units.

total_deposits

A map of product_id -> total deposits held by Nado for a given product at the given time in the base token units.

total_borrows

A map of product_id -> total borrows lent by Nado for a given product at the given time in the base token units.

funding_rates

A map of product_id ->hourlyhistorical funding rates, value returned asdecimal rates(% = rate * 100), derived from funding payment amounts. Requires a minimum granularity of 3600 to see non-zero funding rates. Use a granularity where granularity % 3600 = 0 for best results.

deposit_rates

A map of product_id ->dailydeposit rates, values returned asdecimal rates(% = rate * 100).

borrow_rates

A map of product_id ->dailyborrow rates, values returned asdecimal rates(% = rate * 100).

cumulative_inflows

A map of product_id -> cumulative inflows a.k.a deposits in base token units.

cumulative_outflows

A map of product_id -> cumulative outflows a.k.a withdraws in base token units.

tvl

The total value locked in USD.

[PreviousPerp Prices](/developer-resources/api/archive-indexer/perp-prices)
[NextEdge Market Snapshots](/developer-resources/api/archive-indexer/edge-market-snapshots)

Last updated1 month ago