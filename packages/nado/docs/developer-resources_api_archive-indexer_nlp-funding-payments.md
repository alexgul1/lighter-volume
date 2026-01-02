---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/nlp-funding-payments
title: NLP Funding Payments
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# NLP Funding Payments

Query NLP (Nado Liquidity Provider) funding payments

## Rate limits

- 480 requests/min or 80 requests/10secs per IP address. (weight = 5)

480 requests/min or 80 requests/10secs per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query historical NLP funding payments.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "nlp_funding_payments": {
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

### Funding Payments

product_id

Id of the perp product

idx

Submission index of the transaction that triggered the payment

timestamp

Unix epoch time in seconds when the payment occurred

total_payment

Total funding payment amount (x18 format)

rate_x18

Funding rate used for calculation (x18 format)

oracle_price_x18

Oracle price at the time of payment (x18 format)

[PreviousFast Withdrawal Signature](/developer-resources/api/archive-indexer/fast-withdrawal-signature)
[NextNLP Interest Payments](/developer-resources/api/archive-indexer/nlp-interest-payments)

Last updated1 month ago