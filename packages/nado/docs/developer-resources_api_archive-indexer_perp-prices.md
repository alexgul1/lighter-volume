---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/perp-prices
title: Perp Prices
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Perp Prices

Query latest index and mark prices for provided perp products.

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Single Product

### Request

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "price": {
    "product_id": 2
  }
}
```

### Request Parameters

product_id

number

Yes

Id of perp product to fetch prices for.

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

Ids of perp products to fetch prices for.

### Response

Note: the response is a map ofproduct_id -> perp_pricesfor each requested product.

`product_id -> perp_prices`

## Response Fields

product_id

Id of the perp product.

index_price_x18

Latest index price of the perp product, multiplied by 10^18.

mark_price_x18

Latest mark price of the perp product, multiplied by 10^18.

update_time

Epoch time in seconds the perp prices were last updated at.

[PreviousOracle Snapshots](/developer-resources/api/archive-indexer/oracle-snapshots)
[NextMarket Snapshots](/developer-resources/api/archive-indexer/market-snapshots)

Last updated1 month ago