---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/direct-deposit-address
title: Direct Deposit Address
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Direct Deposit Address

Query direct deposit address for a subaccount

## Rate limits

- 240 requests/min or 40 requests/10secs per IP address. (weight = 10)

240 requests/min or 40 requests/10secs per IP address. (weight = 10)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Query the unique direct deposit address for a subaccount.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "direct_deposit_address": {
    "subaccount": "0x79cc76364b5fb263a25bd52930e3d9788fcfeea864656661756c740000000000"
  }
}
```

## Request Parameters

subaccount

string

Yes

Hex string of the subaccount to fetch the direct deposit address for.

## Response

## Response Fields

### Direct Deposit Address

subaccount

Hex string of the subaccount

deposit_address

Unique deposit address for this subaccount

created_at

Unix epoch time in seconds when the deposit address was created

Direct deposit addresses allow users to deposit funds directly to their subaccount without needing to interact with the smart contract. Funds sent to this address will automatically be credited to the associated subaccount.

[PreviousSequencer Backlog](/developer-resources/api/archive-indexer/sequencer-backlog)
[NextQuote Price](/developer-resources/api/archive-indexer/quote-price)

Last updated1 month ago