---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/signatures
title: Signatures
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Signatures

Query order signatures by digests

## Rate limits

- Dynamic based ondigestsparam provided (weight = 2 + len(digests) / 10)E.g: Withdigests=100, you can make up to 200 requests per min or 33 requests / 10 secs.

Dynamic based ondigestsparam provided (weight = 2 + len(digests) / 10)

`digests`
- E.g: Withdigests=100, you can make up to 200 requests per min or 33 requests / 10 secs.

E.g: Withdigests=100, you can make up to 200 requests per min or 33 requests / 10 secs.

`digests=100`

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "signatures": {
    "digests": [
      "0xf4f7a8767faf0c7f72251a1f9e5da590f708fd9842bf8fcdeacbaa0237958fff",
      "0x0495a88fb3b1c9bed9b643b8e264a391d04cdd48890d81cd7c4006473f28e361"
    ]
  }
}
```

## Request Parameters

digests

string[]

Yes

A list of order digests to retrieve signatures for.

## Response

## Response Fields

digest

The order's generated digest.

signature

The order's generated signature.

signer

The address that signed the order / generated the signature.

is_linked

Indicates whether this is a signature from a linked signer or the original sender.

[PreviousIsolated Subaccounts](/developer-resources/api/archive-indexer/isolated-subaccounts)
[NextFast Withdrawal Signature](/developer-resources/api/archive-indexer/fast-withdrawal-signature)

Last updated1 month ago