---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/funding-rate
title: Funding Rate
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Funding Rate

Query perp products 24hr funding rate.

## Rate limits

- 1200 requests/min or 20 requests/sec per IP address. (weight = 2)

1200 requests/min or 20 requests/sec per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Single Product

### Request

Query perp product 24hr funding rate.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "funding_rate": {
    "product_id": 2
  }
}
```

### Request Parameters

product_id

number

Yes

Id of perp product to fetch funding rate for.

### Response

## Multiple Products

### Request

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

### Request Parameters

product_ids

number[]

Yes

Ids of perp products to fetch funding rate for.

### Response

Note: the response is a map ofproduct_id -> funding_ratefor each requested product.

`product_id -> funding_rate`

## Response Fields

product_id

Id of the perp product this funding rate corresponds to.

funding_rate_x18

Latest 24hr funding rate for the specified product, multiplied by 10^18

update_time

Epoch time in seconds this funding rate was last updated at

[PreviousProduct Snapshots](/developer-resources/api/archive-indexer/product-snapshots)
[NextInterest & funding payments](/developer-resources/api/archive-indexer/interest-and-funding-payments)

Last updated1 month ago