---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/product-snapshots
title: Product Snapshots
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Product Snapshots

Query historical product snapshots.

## Rate limits

- 240 requests/min or 40 requests/10secs per IP address. (weight = 10)

240 requests/min or 40 requests/10secs per IP address. (weight = 10)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Single Product

### Request

Query snapshots for a given product ordered bysubmission indexdesc.

`submission index`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
    "products": {
        "product_id": 2,
        "max_time": 1679728762,
        "limit": 1
    }
}
```

### Request Parameters

product_id

number

Yes

id of product to fetch snapshots for.

idx

number / string

No

when provided, only return product snapshots withsubmission_idx<=idx

`submission_idx`
`idx`

max_time

number / string

No

whenidxis not provided,max_time(unix epoch in seconds) can be used to only return snapshots created <=max_time

`idx`
`max_time`
`max_time`

limit

number

No

max number of snapshots to return. defaults to100. max possible of500.

`100`
`500`

### Response

Note:

- the response includes atxsfield which contains the relevant transactions to the product snapshots. There are>=1 product snapshotsper transaction.

the response includes atxsfield which contains the relevant transactions to the product snapshots. There are>=1 product snapshotsper transaction.

`txs`
`>=1 product snapshots`
- bothproductsandtxsare in descending order bysubmission_idx.

bothproductsandtxsare in descending order bysubmission_idx.

`products`
`txs`
`submission_idx`
- use thesubmission_idxto associate aproduct snapshotto it's corresponding transaction.

use thesubmission_idxto associate aproduct snapshotto it's corresponding transaction.

`submission_idx`
`product snapshot`

### Response Fields

#### Products

submission_idx

Used to uniquely identify the blockchain transaction that generated the product snapshot; you can use it to grab the relevant transaction in thetxssection.

`txs`

product_id

The id of of the product the event is associated with.

product

The state of the product at the time of the transaction.

#### Txs

submission_idx

Unique identifier of the transaction.

tx

Raw data of the corresponding transaction

timestamp

The unix epoch in seconds of when the transaction took place.

## Multiple Products

### Request

Query the latest snapshot for the provided products.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

### Request Parameters

product_ids

number[]

Yes

Ids of products to fetch snapshots for.

max_time

number / string

No

When provided, returns the last snapshot created <=max_timefor each product. Otherwise, the latest snapshot is returned.

`max_time`

### Response

Note: the response is a map ofproduct_id -> snapshotfor each requested product.

`product_id -> snapshot`

### Response Fields

submission_idx

Used to uniquely identify the blockchain transaction that generated the product snapshot.

product_id

The id of of the product the event is associated with.

product

The state of the product at the time of the transaction.

[PreviousEdge Candlesticks](/developer-resources/api/archive-indexer/edge-candlesticks)
[NextFunding Rate](/developer-resources/api/archive-indexer/funding-rate)

Last updated1 month ago