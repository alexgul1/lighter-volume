---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/fast-withdrawal-signature
title: Fast Withdrawal Signature
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Fast Withdrawal Signature

Query signature for fast withdrawal

## Rate limits

- 240 requests/min or 40 requests/10secs per IP address. (weight = 10)

240 requests/min or 40 requests/10secs per IP address. (weight = 10)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query the signature required for a fast withdrawal at a specific submission index.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "fast_withdrawal_signature": {
    "idx": "12345"
  }
}
```

## Request Parameters

idx

number / string

Yes

Submission index to fetch the fast withdrawal signature for.

## Response

## Response Fields

### Fast Withdrawal Signature

signature

Hex string of the signature for fast withdrawal

submission_idx

Transaction submission index

subaccount

Hex string of the subaccount

product_id

Product ID (0 for quote asset)

amount

Withdrawal amount (x18 format)

nonce

Nonce for the withdrawal transaction

[PreviousSignatures](/developer-resources/api/archive-indexer/signatures)
[NextNLP Funding Payments](/developer-resources/api/archive-indexer/nlp-funding-payments)

Last updated1 month ago