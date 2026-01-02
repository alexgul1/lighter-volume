---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/quote-price
title: Quote Price
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Quote Price

Query quote token (USDT0) price in USD.

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
  "quote_price": {}
}
```

## Response

```
{
    "price_x18": "999944870000000000"
}
```

[PreviousDirect Deposit Address](/developer-resources/api/archive-indexer/direct-deposit-address)
[NextInk Airdrop](/developer-resources/api/archive-indexer/ink-airdrop)

Last updated1 month ago