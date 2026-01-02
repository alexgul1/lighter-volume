---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/subaccounts
title: Subaccounts
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Subaccounts

Query Nado subaccounts.

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query subaccounts ordered bysubaccount idASC.

`subaccount id`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "subaccounts": {
    "start": 100,
    "limit": 10,
  }
}
```

Query all subaccounts associated to an address ordered bysubaccount idASC.

`subaccount id`

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "subaccounts": {
    "address": "0x79CC76364b5Fb263A25bD52930E3d9788fCfEEA8"
  }
}
```

## Request Parameters

start

string/number

No

Subaccount id to start from (used for pagination). Defaults to 0.

limit

string/number

No

Max number of subaccounts to return. Defaults to 100, max of 500.

address

string

No

An optional wallet address to find all subaccounts associated to it.

## Response

## Response Fields

### Subaccounts

id

Internal subaccount id

subaccount

Hex string of the subaccount (wallet + subaccount name)

address

Hex string of wallet address

subaccount_name

Subaccount identifier

created_at

When subaccount was created

isolated

Whether it's a subaccount for an isolated position

[PreviousEdge Market Snapshots](/developer-resources/api/archive-indexer/edge-market-snapshots)
[NextSubaccount Snapshots](/developer-resources/api/archive-indexer/subaccount-snapshots)

Last updated1 month ago