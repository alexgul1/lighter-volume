---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/interest-and-funding-payments
title: Interest & funding payments
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Interest & funding payments

Query historical interest and funding payments for a subaccount.

## Rate limits

- 480 requests/min or 80 requests/10secs per IP address. (weight = 5)

480 requests/min or 80 requests/10secs per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query subaccount historical interest and funding payments.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "interest_and_funding": {
    "subaccount": "0xD028878bF5c96218E53DA859e587cb8398B17b3f64656661756c740000000000",
    "product_ids": [1, 2],
    "limit": 10,
    "max_idx": 1315836
  }
}
```

## Request Parameters

subaccount

string

Yes

A bytes32 sent as a hex string; includes the address and the subaccount identifier.

product_ids

number[]

Yes

Ids of products to historical interest/funding payments for.

max_idx

string/number

No

When provided, only return records withidx<=max_idx.

`idx`
`max_idx`

limit

number

Yes

Max number of records to return. Max possible of100.

`100`

## Response

## Response Fields

interest_payments.product_id

Id of spot product the interest payment is associated to.

interest_payments.idx

Id of transaction that triggered the interest payment.

interest_payments.timestamp

Timestamp of the transaction that triggered the interest payment.

interest_payments.amount

Amount of interest paid multiplied by 10**18.

interest_payments.balance_amount

Previous spot balance at the moment of payment (exclusive of payment amount)

interest_payments.rate_x18

Spot interest rate at the moment of payment, multiplied by 10**18.

interest_payments.oracle_price_x18

Oracle price for the spot product at the moment of payment, multiplied by 10**18.

funding_payments.product_id

Id of perp product the funding payment is associated to.

funding_payments.idx

Id of transaction that triggered the funding payment.

funding_payments.timestamp

Timestamp of the transaction that triggered the funding payment.

funding_payments.amount

Amount of funding paid multiplied by 10**18.

funding_payments.balance_amount

Previous perp balance at the moment of payment +amount of perps locked in LPs (exclusive of payment amount).

funding_payments.rate_x18

Perp funding rate at the moment of payment, multiplied by 10**18.

funding_payments.oracle_price_x18

Oracle price for the perp product at the moment of payment, multiplied by 10**18.

next_idx

Id of the next payment snapshot. Use this asmax_idxon a subsequent call to get the next page. This will benullwhen there are no more records.

`max_idx`
`null`
[PreviousFunding Rate](/developer-resources/api/archive-indexer/funding-rate)
[NextOracle Price](/developer-resources/api/archive-indexer/oracle-price)

Last updated1 month ago