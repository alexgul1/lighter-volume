---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/oracle-price
title: Oracle Price
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Oracle Price

Query latest oracle price for provided product ids

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "oracle_price": {
    "product_ids": [1, 2, 3, 4]
  }
}
```

## Request Parameters

product_ids

number[]

Yes

Ids of products to fetch oracles price for.

## Response

## Response Fields

### Prices

product_id

Id of product oracle price corresponds to.

oracle_price_x18

Latest oracle price multiplied by 10^18.

update_time

Epoch in seconds the oracle price was last updated at.

[PreviousInterest & funding payments](/developer-resources/api/archive-indexer/interest-and-funding-payments)
[NextOracle Snapshots](/developer-resources/api/archive-indexer/oracle-snapshots)

Last updated1 month ago