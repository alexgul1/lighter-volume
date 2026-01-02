---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/candlesticks
title: Candlesticks
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Candlesticks

Query historical candlesticks by product and granularity / period.

## Rate limits

- Dynamic based onlimitparam provided (weight = 1 + limit / 20)E.g: Withlimit=100, you can make up to 400 requests per min or 66 requests / 10 secs.

Dynamic based onlimitparam provided (weight = 1 + limit / 20)

`limit`
- E.g: Withlimit=100, you can make up to 400 requests per min or 66 requests / 10 secs.

E.g: Withlimit=100, you can make up to 400 requests per min or 66 requests / 10 secs.

`limit=100`

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Available Granularities

The following granularities / periods are supported (in seconds):

1 minute

60

5 minutes

300

15 minutes

900

1 hour

3600

2 hours

7200

4 hours

14400

1 day

86400

1 week

604800

4 weeks

2419200

## Request

Query product candlesticks ordered bytimestampdesc.

`timestamp`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

## Request Parameters

product_id

number

Yes

Id of product to fetch candlesticks for.

granularity

number

Yes

Granularity value in seconds.

max_time

number / string

No

When providingmax_time(unix epoch in seconds), only return candlesticks with timestamp <=max_time

`max_time`
`max_time`

limit

number

No

Max number of candlesticks to return. defaults to100. max possible of500.

`100`
`500`

## Response

## Response Fields

submission_idx

Id of the latest recorded transaction that contributes to the candle.

product_id

Id of product candle is associated to.

granularity

Candle time interval, expressed in seconds, representing the aggregation period for trading volume and price data

open_x18

The first fill price of the candle, multiplied by 10^18

high_x18

The highest recorded fill price during the defined interval of the candle, multiplied by 10^18

low_x18

The lowest recorded fill price during the defined interval of the candle, multiplied by 10^18

close_x18

The last price of the candle, multiplied by 10^18

volume

Asset volume, which represents the absolute cumulative fill amounts during the time interval of the candle, multiplied by 10^18

[PreviousEvents](/developer-resources/api/archive-indexer/events)
[NextEdge Candlesticks](/developer-resources/api/archive-indexer/edge-candlesticks)

Last updated1 month ago