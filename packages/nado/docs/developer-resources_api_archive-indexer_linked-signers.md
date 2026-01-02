---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/linked-signers
title: Linked Signers
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Linked Signers

Query linked signers

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query linked signers ordered by creation time.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "linked_signers": {
    "start_idx": 0,
    "limit": 100
  }
}
```

## Request Parameters

start_idx

number / string

No

Starting index for pagination. Defaults to 0.

limit

number

No

Max number of linked signers to return. Defaults to100. Max of500.

`100`
`500`

## Response

## Response Fields

### Linked Signers

subaccount

Hex string of the subaccount

signer

Hex string of the linked signer address

created_at

Unix epoch time in seconds when the signer was linked

[PreviousSubaccount Snapshots](/developer-resources/api/archive-indexer/subaccount-snapshots)
[NextLinked Signer Rate Limit](/developer-resources/api/archive-indexer/linked-signer-rate-limit)

Last updated1 month ago