---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/tx-hashes
title: Tx Hashes
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Tx Hashes

Query transaction hashes by submission indices

## Rate limits

- Dynamic based on number of indices (weight = idxs.length * 2)E.g: With10 indices, weight = 20Max of 100 indices per request

Dynamic based on number of indices (weight = idxs.length * 2)

- E.g: With10 indices, weight = 20

E.g: With10 indices, weight = 20

`10 indices`
- Max of 100 indices per request

Max of 100 indices per request

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query transaction hashes for specific submission indices.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "tx_hashes": {
    "idxs": ["12345", "12346", "12347"]
  }
}
```

## Request Parameters

idxs

array

Yes

Array of submission indices to fetch transaction hashes for. Max 100 indices.

## Response

## Response Fields

### Tx Hashes

submission_idx

Starting submission index for this transaction batch

tx_hash

Hex string of the transaction hash

length

Number of submissions included in this transaction batch

If a submission index doesn't have an associated transaction hash,nullis returned for that index.

`null`

Last updated17 days ago