---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/ink-airdrop
title: Ink Airdrop
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Ink Airdrop

Query the Ink airdrop amount for a given address.

Query the Ink token airdrop allocation for a specific wallet address.

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "ink_airdrop": {
    "address": "0x1234567890123456789012345678901234567890"
  }
}
```

## Request Parameters

address

string

Yes

Wallet address (20-byte address) sent as a hex string.

## Response

Note: The amount is returned as a string to preserve precision.

## Response Fields

amount

The Ink token airdrop amount allocated to the address.

[PreviousQuote Price](/developer-resources/api/archive-indexer/quote-price)
[NextTrigger](/developer-resources/api/trigger)

Last updated1 month ago