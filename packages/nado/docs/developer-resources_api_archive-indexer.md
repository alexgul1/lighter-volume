---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer
title: Archive (indexer)
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Archive (indexer)

Query Nado's indexed historical data

Using Nado's indexer API you can access historical data in the platform as it is processed by our offchain sequencer. This includes: trading activity, events, candlesticks and more.

You can interact with our indexer by sendingHTTPrequests atPOST [ARCHIVE_ENDPOINT]alongside a json payload of the query. Endpoints:

`HTTP`
`POST [ARCHIVE_ENDPOINT]`

HTTPrequests must set theAccept-Encodingto includegzip,brordeflate

`HTTP`
`Accept-Encoding`
`gzip`
`br`
`deflate`

## Endpoints

### Testnet:

- https://archive.test.nado.xyz/v1

https://archive.test.nado.xyz/v1

`https://archive.test.nado.xyz/v1`

## Available Queries:

[Orders](/developer-resources/api/archive-indexer/orders)
[Matches](/developer-resources/api/archive-indexer/matches)
[Events](/developer-resources/api/archive-indexer/events)
[Candlesticks](/developer-resources/api/archive-indexer/candlesticks)
[Edge Candlesticks](/developer-resources/api/archive-indexer/edge-candlesticks)
[Product Snapshots](/developer-resources/api/archive-indexer/product-snapshots)
[Funding Rate](/developer-resources/api/archive-indexer/funding-rate)
[Interest & funding payments](/developer-resources/api/archive-indexer/interest-and-funding-payments)
[Oracle Price](/developer-resources/api/archive-indexer/oracle-price)
[Oracle Snapshots](/developer-resources/api/archive-indexer/oracle-snapshots)
[Perp Prices](/developer-resources/api/archive-indexer/perp-prices)
[Market Snapshots](/developer-resources/api/archive-indexer/market-snapshots)
[Edge Market Snapshots](/developer-resources/api/archive-indexer/edge-market-snapshots)
[Subaccounts](/developer-resources/api/archive-indexer/subaccounts)
[Subaccount Snapshots](/developer-resources/api/archive-indexer/subaccount-snapshots)
[Linked Signers](/developer-resources/api/archive-indexer/linked-signers)
[Linked Signer Rate Limit](/developer-resources/api/archive-indexer/linked-signer-rate-limit)
[Isolated Subaccounts](/developer-resources/api/archive-indexer/isolated-subaccounts)
[Signatures](/developer-resources/api/archive-indexer/signatures)
[Fast Withdrawal Signature](/developer-resources/api/archive-indexer/fast-withdrawal-signature)
[NLP Funding Payments](/developer-resources/api/archive-indexer/nlp-funding-payments)
[NLP Interest Payments](/developer-resources/api/archive-indexer/nlp-interest-payments)
[NLP Snapshots](/developer-resources/api/archive-indexer/nlp-snapshots)
[Liquidation Feed](/developer-resources/api/archive-indexer/liquidation-feed)
[Sequencer Backlog](/developer-resources/api/archive-indexer/sequencer-backlog)
[Direct Deposit Address](/developer-resources/api/archive-indexer/direct-deposit-address)
[Quote Price](/developer-resources/api/archive-indexer/quote-price)
[Ink Airdrop](/developer-resources/api/archive-indexer/ink-airdrop)
[PreviousRate limits](/developer-resources/api/subscriptions/rate-limits)
[NextOrders](/developer-resources/api/archive-indexer/orders)

Last updated17 days ago