---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/nlp-interest-payments
title: NLP Interest Payments
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# NLP Interest Payments

Query NLP (Nado Liquidity Provider) interest payments

## Rate limits

- 480 requests/min or 80 requests/10secs per IP address. (weight = 5)

480 requests/min or 80 requests/10secs per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query historical NLP interest payments.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "nlp_interest_payments": {
    "max_idx": "1315836",
    "max_time": "1683315718",
    "limit": 100
  }
}
```

## Request Parameters

max_idx

number / string

No

When provided, only return payments withidx<=max_idx.

`idx`
`max_idx`

max_time

number / string

No

When provided, only return payments withtimestamp<=max_time(unix epoch in seconds).

`timestamp`
`max_time`

limit

number

No

Max number of payments to return. Defaults to100. Max of500.

`100`
`500`

## Response

## Response Fields

### Interest Payments

product_id

Id of the spot product (typically quote/collateral products)

idx

Submission index of the transaction that triggered the payment

timestamp

Unix epoch time in seconds when the payment occurred

amount

Interest payment amount (x18 format)

balance_amount

Balance amount at the time of payment (x18 format)

[PreviousNLP Funding Payments](/developer-resources/api/archive-indexer/nlp-funding-payments)
[NextNLP Snapshots](/developer-resources/api/archive-indexer/nlp-snapshots)

Last updated23 days ago