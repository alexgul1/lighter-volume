---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/isolated-subaccounts
title: Isolated Subaccounts
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Isolated Subaccounts

Query isolated margin subaccounts

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query all isolated subaccounts.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "isolated_subaccounts": {
    "start_idx": 0,
    "limit": 100
  }
}
```

Query isolated subaccounts associated with a specific subaccount.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "isolated_subaccounts": {
    "subaccount": "0x79cc76364b5fb263a25bd52930e3d9788fcfeea864656661756c740000000000",
    "limit": 100
  }
}
```

## Request Parameters

subaccount

string

No

Hex string of the parent subaccount to filter by.

start_idx

number / string

No

Starting index for pagination. Defaults to 0.

limit

number

No

Max number of isolated subaccounts to return. Defaults to100. Max of500.

`100`
`500`

## Response

## Response Fields

### Isolated Subaccounts

subaccount

Hex string of the parent subaccount

isolated_subaccount

Hex string of the isolated margin subaccount

product_id

Product ID for which this isolated subaccount was created

created_at

Unix epoch time in seconds when the isolated subaccount was created

[PreviousLinked Signer Rate Limit](/developer-resources/api/archive-indexer/linked-signer-rate-limit)
[NextSignatures](/developer-resources/api/archive-indexer/signatures)

Last updated1 month ago