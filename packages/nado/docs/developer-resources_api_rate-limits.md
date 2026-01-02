---
url: https://docs.nado.xyz/developer-resources/api/rate-limits
title: Rate limits
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Rate limits

Nado Websocket and REST API Rate limits.

## Overview

- Nado uses a weight-based rate-limiting system across queries and executes. We limit based onIP address,Wallet address, and a globalmax # of orders per subaccount per market.

Nado uses a weight-based rate-limiting system across queries and executes. We limit based onIP address,Wallet address, and a globalmax # of orders per subaccount per market.

`IP address`
`Wallet address`
`max # of orders per subaccount per market`
- These limits equally apply to bothhttprequests andWebsocketmessages.

These limits equally apply to bothhttprequests andWebsocketmessages.

`http`
`Websocket`
- Limits are applied on a1 minuteand10 secondsbasis.

Limits are applied on a1 minuteand10 secondsbasis.

`1 minute`
`10 seconds`

## Limits

- IP addresses have a max weight limit of2400per minute or400every 10 seconds applied only to queries.

IP addresses have a max weight limit of2400per minute or400every 10 seconds applied only to queries.

`2400`
`400`
- Wallet addresses have a max weight limit of600per minute or100every 10 seconds applied only to executes.

Wallet addresses have a max weight limit of600per minute or100every 10 seconds applied only to executes.

`600`
`100`
- Users can have up to500open orders per subaccount per market.

Users can have up to500open orders per subaccount per market.

`500`
- Orders have the following additional limits:Place orders (with spot leverage): up to600per minute or100every 10 seconds across all markets.Place orders (without spot leverage): up to30per minute or5every 10 seconds across all markets.Note: orders without spot leverage are20xmore expensive to place due to additional health checks needed.Order cancellations: up to600per minute or100every 10 seconds.

Orders have the following additional limits:

- Place orders (with spot leverage): up to600per minute or100every 10 seconds across all markets.

Place orders (with spot leverage): up to600per minute or100every 10 seconds across all markets.

`600`
`100`
- Place orders (without spot leverage): up to30per minute or5every 10 seconds across all markets.Note: orders without spot leverage are20xmore expensive to place due to additional health checks needed.

Place orders (without spot leverage): up to30per minute or5every 10 seconds across all markets.Note: orders without spot leverage are20xmore expensive to place due to additional health checks needed.

`30`
`5`
`20x`
- Order cancellations: up to600per minute or100every 10 seconds.

Order cancellations: up to600per minute or100every 10 seconds.

`600`
`100`

## Query Weights

Queries are rate-limited based on IP. The following weights are applied per query:

- Status:IP weight = 1

Status:IP weight = 1

[Status](/developer-resources/api/gateway/queries/status)
`IP weight = 1`
- Contracts:IP weight = 1

Contracts:IP weight = 1

[Contracts](/developer-resources/api/gateway/queries/contracts)
`IP weight = 1`
- Nonces:IP weight = 2

Nonces:IP weight = 2

[Nonces](/developer-resources/api/gateway/queries/nonces)
`IP weight = 2`
- Order:IP weight = 1

Order:IP weight = 1

[Order](/developer-resources/api/gateway/queries/order)
`IP weight = 1`
- Orders:IP weight = 2 * product_ids.length

Orders:IP weight = 2 * product_ids.length

[Orders](/developer-resources/api/gateway/queries/orders)
`IP weight = 2 * product_ids.length`
- Subaccount Info:IP weight = 2(or10withtxns, or15withtxns+pre_state="true")

Subaccount Info:IP weight = 2(or10withtxns, or15withtxns+pre_state="true")

[Subaccount Info](/developer-resources/api/gateway/queries/subaccount-info)
`IP weight = 2`
`10`
`txns`
`15`
`txns`
`pre_state="true"`
- Isolated Positions:IP weight = 10

Isolated Positions:IP weight = 10

[Isolated Positions](/developer-resources/api/gateway/queries/isolated-positions)
`IP weight = 10`
- Market Liquidity:IP weight = 1

Market Liquidity:IP weight = 1

[Market Liquidity](/developer-resources/api/gateway/queries/market-liquidity)
`IP weight = 1`
- Symbols:IP weight = 2

Symbols:IP weight = 2

[Symbols](/developer-resources/api/gateway/queries/symbols)
`IP weight = 2`
- All Products:IP weight = 5

All Products:IP weight = 5

[All Products](/developer-resources/api/gateway/queries/all-products)
`IP weight = 5`
- Edge All Products:IP weight = 5

Edge All Products:IP weight = 5

[Edge All Products](/developer-resources/api/gateway/queries/edge-all-products)
`IP weight = 5`
- Market Prices:IP weight = product_ids.length

Market Prices:IP weight = product_ids.length

[Market Prices](/developer-resources/api/gateway/queries/market-prices)
`IP weight = product_ids.length`
- Max Order Size:IP weight = 5

Max Order Size:IP weight = 5

[Max Order Size](/developer-resources/api/gateway/queries/max-order-size)
`IP weight = 5`
- Max Withdrawable:IP weight = 5

Max Withdrawable:IP weight = 5

[Max Withdrawable](/developer-resources/api/gateway/queries/max-withdrawable)
`IP weight = 5`
- Max NLP Mintable:IP weight = 20

Max NLP Mintable:IP weight = 20

[Max NLP Mintable](/developer-resources/api/gateway/queries/max-nlp-mintable)
`IP weight = 20`
- Max NLP Burnable:IP weight = 20

Max NLP Burnable:IP weight = 20

[Max NLP Burnable](/developer-resources/api/gateway/queries/max-nlp-burnable)
`IP weight = 20`
- NLP Pool Info:IP weight = 20

NLP Pool Info:IP weight = 20

[NLP Pool Info](/developer-resources/api/gateway/queries/nlp-pool-info)
`IP weight = 20`
- NLP Locked Balances:IP weight = 20

NLP Locked Balances:IP weight = 20

[NLP Locked Balances](/developer-resources/api/gateway/queries/nlp-locked-balances)
`IP weight = 20`
- Health Groups:IP weight = 2

Health Groups:IP weight = 2

[Health Groups](/developer-resources/api/gateway/queries/health-groups)
`IP weight = 2`
- Linked Signer:IP weight = 5

Linked Signer:IP weight = 5

[Linked Signer](/developer-resources/api/gateway/queries/linked-signer)
`IP weight = 5`
- Insurance:IP weight = 2

Insurance:IP weight = 2

[Insurance](/developer-resources/api/gateway/queries/insurance)
`IP weight = 2`
- Fee Rates:IP weight = 2

Fee Rates:IP weight = 2

[Fee Rates](/developer-resources/api/gateway/queries/fee-rates)
`IP weight = 2`
- Assets:IP weight = 2

Assets:IP weight = 2

[Assets](/developer-resources/api/v2/assets)
`IP weight = 2`
- Orderbook:IP weight = 1

Orderbook:IP weight = 1

[Orderbook](/developer-resources/api/v2/orderbook)
`IP weight = 1`

## Archive (indexer) Weights

- Archive (indexer) queries are rate-limited based on IP.

Archive (indexer) queries are rate-limited based on IP.

- IP addresses have a max weight limit of2400per minute or400every 10 seconds.

IP addresses have a max weight limit of2400per minute or400every 10 seconds.

`2400`
`400`

The following weights are applied per query:

- Orders:IP Weight = 2 + (limit * subaccounts.length / 20); wherelimitandsubaccountsare query params.

Orders:IP Weight = 2 + (limit * subaccounts.length / 20); wherelimitandsubaccountsare query params.

[Orders](/developer-resources/api/archive-indexer/orders)
`IP Weight = 2 + (limit * subaccounts.length / 20)`
`limit`
`subaccounts`
- Matches:IP Weight = 2 + (limit * subaccounts.length / 10); wherelimitandsubaccountsare query params.

Matches:IP Weight = 2 + (limit * subaccounts.length / 10); wherelimitandsubaccountsare query params.

[Matches](/developer-resources/api/archive-indexer/matches)
`IP Weight = 2 + (limit * subaccounts.length / 10)`
`limit`
`subaccounts`
- Events:IP Weight = 2 + (limit * subaccounts.length / 10); wherelimitandsubaccountsare query params.

Events:IP Weight = 2 + (limit * subaccounts.length / 10); wherelimitandsubaccountsare query params.

[Events](/developer-resources/api/archive-indexer/events)
`IP Weight = 2 + (limit * subaccounts.length / 10)`
`limit`
`subaccounts`
- Candlesticks:IP Weight = 1 + limit / 20; wherelimitis a query param.

Candlesticks:IP Weight = 1 + limit / 20; wherelimitis a query param.

[Candlesticks](/developer-resources/api/archive-indexer/candlesticks)
`IP Weight = 1 + limit / 20`
`limit`
- Edge Candlesticks:IP Weight = 1 + limit / 20; wherelimitis a query param.

Edge Candlesticks:IP Weight = 1 + limit / 20; wherelimitis a query param.

[Edge Candlesticks](/developer-resources/api/archive-indexer/edge-candlesticks)
`IP Weight = 1 + limit / 20`
`limit`
- Product Snapshots:IP Weight = 10for singleproductsquery, or10 * timestamps.lengthfor multipleproduct_snapshotsquery with max_time parameter

Product Snapshots:IP Weight = 10for singleproductsquery, or10 * timestamps.lengthfor multipleproduct_snapshotsquery with max_time parameter

[Product Snapshots](/developer-resources/api/archive-indexer/product-snapshots)
`IP Weight = 10`
`products`
`10 * timestamps.length`
`product_snapshots`
- Funding Rate:IP Weight = 2

Funding Rate:IP Weight = 2

[Funding Rate](/developer-resources/api/archive-indexer/funding-rate)
`IP Weight = 2`
- Interest & funding payments:IP Weight = 5

Interest & funding payments:IP Weight = 5

[Interest & funding payments](/developer-resources/api/archive-indexer/interest-and-funding-payments)
`IP Weight = 5`
- Oracle Price:IP Weight = 2

Oracle Price:IP Weight = 2

[Oracle Price](/developer-resources/api/archive-indexer/oracle-price)
`IP Weight = 2`
- Oracle Snapshots:IP Weight = max((snapshot_count * product_ids.length / 100), 2); where snapshot_count isinterval.count.min(500)

Oracle Snapshots:IP Weight = max((snapshot_count * product_ids.length / 100), 2); where snapshot_count isinterval.count.min(500)

[Oracle Snapshots](/developer-resources/api/archive-indexer/oracle-snapshots)
`IP Weight = max((snapshot_count * product_ids.length / 100), 2)`
`interval.count.min(500)`
- Perp Prices:IP Weight = 2(includes both singlepriceand multipleperp_pricesqueries)

Perp Prices:IP Weight = 2(includes both singlepriceand multipleperp_pricesqueries)

[Perp Prices](/developer-resources/api/archive-indexer/perp-prices)
`IP Weight = 2`
`price`
`perp_prices`
- Market Snapshots:IP Weight = max((snapshot_count * product_ids.length / 100), 2); where snapshot_count isinterval.count.min(500)

Market Snapshots:IP Weight = max((snapshot_count * product_ids.length / 100), 2); where snapshot_count isinterval.count.min(500)

[Market Snapshots](/developer-resources/api/archive-indexer/market-snapshots)
`IP Weight = max((snapshot_count * product_ids.length / 100), 2)`
`interval.count.min(500)`
- Edge Market Snapshots:IP weight = (interval.count.min(500) / 20) + (interval.count.clamp(2, 20) * 2)

Edge Market Snapshots:IP weight = (interval.count.min(500) / 20) + (interval.count.clamp(2, 20) * 2)

[Edge Market Snapshots](/developer-resources/api/archive-indexer/edge-market-snapshots)
`IP weight = (interval.count.min(500) / 20) + (interval.count.clamp(2, 20) * 2)`
- Subaccounts:IP Weight = 2

Subaccounts:IP Weight = 2

[Subaccounts](/developer-resources/api/archive-indexer/subaccounts)
`IP Weight = 2`
- Subaccount Snapshots:IP Weight = 2 + (limit * subaccounts.length / 10); wherelimitandsubaccountsare query params.

Subaccount Snapshots:IP Weight = 2 + (limit * subaccounts.length / 10); wherelimitandsubaccountsare query params.

[Subaccount Snapshots](/developer-resources/api/archive-indexer/subaccount-snapshots)
`IP Weight = 2 + (limit * subaccounts.length / 10)`
`limit`
`subaccounts`
- Linked Signers:IP Weight = 2

Linked Signers:IP Weight = 2

[Linked Signers](/developer-resources/api/archive-indexer/linked-signers)
`IP Weight = 2`
- Linked Signer Rate Limit:IP Weight = 2

Linked Signer Rate Limit:IP Weight = 2

[Linked Signer Rate Limit](/developer-resources/api/archive-indexer/linked-signer-rate-limit)
`IP Weight = 2`
- Isolated Subaccounts:IP Weight = 2

Isolated Subaccounts:IP Weight = 2

[Isolated Subaccounts](/developer-resources/api/archive-indexer/isolated-subaccounts)
`IP Weight = 2`
- Signatures:IP Weight = 2 + len(digests) / 10; wheredigestsis a query param.

Signatures:IP Weight = 2 + len(digests) / 10; wheredigestsis a query param.

[Signatures](/developer-resources/api/archive-indexer/signatures)
`IP Weight = 2 + len(digests) / 10`
`digests`
- Fast Withdrawal Signature:IP Weight = 10

Fast Withdrawal Signature:IP Weight = 10

[Fast Withdrawal Signature](/developer-resources/api/archive-indexer/fast-withdrawal-signature)
`IP Weight = 10`
- NLP Funding Payments:IP Weight = 5

NLP Funding Payments:IP Weight = 5

[NLP Funding Payments](/developer-resources/api/archive-indexer/nlp-funding-payments)
`IP Weight = 5`
- NLP Interest Payments:IP Weight = 5

NLP Interest Payments:IP Weight = 5

[NLP Interest Payments](/developer-resources/api/archive-indexer/nlp-interest-payments)
`IP Weight = 5`
- NLP Snapshots:IP Weight = limit.min(500) / 100; wherelimitis a query param.

NLP Snapshots:IP Weight = limit.min(500) / 100; wherelimitis a query param.

[NLP Snapshots](/developer-resources/api/archive-indexer/nlp-snapshots)
`IP Weight = limit.min(500) / 100`
`limit`
- Tx Hashes:IP Weight = idxs.length * 2; whereidxsis an array of submission indices (max 100).

Tx Hashes:IP Weight = idxs.length * 2; whereidxsis an array of submission indices (max 100).

[Tx Hashes](/developer-resources/api/archive-indexer/tx-hashes)
`IP Weight = idxs.length * 2`
`idxs`
- Liquidation Feed:IP Weight = 2

Liquidation Feed:IP Weight = 2

[Liquidation Feed](/developer-resources/api/archive-indexer/liquidation-feed)
`IP Weight = 2`
- Sequencer Backlog:IP Weight = 1

Sequencer Backlog:IP Weight = 1

[Sequencer Backlog](/developer-resources/api/archive-indexer/sequencer-backlog)
`IP Weight = 1`
- Direct Deposit Address:IP Weight = 10

Direct Deposit Address:IP Weight = 10

[Direct Deposit Address](/developer-resources/api/archive-indexer/direct-deposit-address)
`IP Weight = 10`
- Quote Price:IP Weight = 2

Quote Price:IP Weight = 2

[Quote Price](/developer-resources/api/archive-indexer/quote-price)
`IP Weight = 2`
- Ink Airdrop:IP Weight = 2

Ink Airdrop:IP Weight = 2

[Ink Airdrop](/developer-resources/api/archive-indexer/ink-airdrop)
`IP Weight = 2`

## Execute Weights

Executes are rate-limited based on Wallet address. The following weights are applied per execute:

- Place order:With spot leverage:Wallet weight = 1Without spot leverage:Wallet weight = 20

Place order:

[Place order](/developer-resources/api/gateway/executes/place-order)
- With spot leverage:Wallet weight = 1

With spot leverage:Wallet weight = 1

`Wallet weight = 1`
- Without spot leverage:Wallet weight = 20

Without spot leverage:Wallet weight = 20

`Wallet weight = 20`
- Place orders:With spot leverage:Wallet weight = 1 per orderWithout spot leverage:Wallet weight = 20 per orderNote: 50ms processing penalty per request

Place orders:

[Place orders](/developer-resources/api/gateway/executes/place-orders)
- With spot leverage:Wallet weight = 1 per order

With spot leverage:Wallet weight = 1 per order

`Wallet weight = 1 per order`
- Without spot leverage:Wallet weight = 20 per order

Without spot leverage:Wallet weight = 20 per order

`Wallet weight = 20 per order`
- Note: 50ms processing penalty per request

Note: 50ms processing penalty per request

- Cancel orders:When nodigestsare provided:Wallet weight = 1Whendigestsare provided:Wallet weight = total digests

Cancel orders:

[Cancel orders](/developer-resources/api/gateway/executes/cancel-orders)
- When nodigestsare provided:Wallet weight = 1

When nodigestsare provided:Wallet weight = 1

`Wallet weight = 1`
- Whendigestsare provided:Wallet weight = total digests

Whendigestsare provided:Wallet weight = total digests

`Wallet weight = total digests`
- Cancel Product Orders:When noproductIdsare provided:Wallet weight = 50WhenproductIdsare provided:Wallet weight = 5 * total productIds

Cancel Product Orders:

[Cancel Product Orders](/developer-resources/api/gateway/executes/cancel-product-orders)
- When noproductIdsare provided:Wallet weight = 50

When noproductIdsare provided:Wallet weight = 50

`Wallet weight = 50`
- WhenproductIdsare provided:Wallet weight = 5 * total productIds

WhenproductIdsare provided:Wallet weight = 5 * total productIds

`Wallet weight = 5 * total productIds`
- Cancel And Place:The sum ofCancel orders+Place orderlimits

Cancel And Place:

[Cancel And Place](/developer-resources/api/gateway/executes/cancel-and-place)
- The sum ofCancel orders+Place orderlimits

The sum ofCancel orders+Place orderlimits

[Cancel orders](/developer-resources/api/gateway/executes/cancel-orders)
[Place order](/developer-resources/api/gateway/executes/place-order)
- Withdraw Collateral:With spot leverage:Wallet weight = 10Without spot leverage:Wallet weight = 20

Withdraw Collateral:

[Withdraw Collateral](/developer-resources/api/gateway/executes/withdraw-collateral)
- With spot leverage:Wallet weight = 10

With spot leverage:Wallet weight = 10

`Wallet weight = 10`
- Without spot leverage:Wallet weight = 20

Without spot leverage:Wallet weight = 20

`Wallet weight = 20`
- Liquidate Subaccount:Wallet weight = 20

Liquidate Subaccount:Wallet weight = 20

[Liquidate Subaccount](/developer-resources/api/gateway/executes/liquidate-subaccount)
`Wallet weight = 20`
- Mint NLP:Wallet weight = 10

Mint NLP:Wallet weight = 10

[Mint NLP](/developer-resources/api/gateway/executes/mint-nlp)
`Wallet weight = 10`
- Burn NLP:Wallet weight = 10

Burn NLP:Wallet weight = 10

[Burn NLP](/developer-resources/api/gateway/executes/burn-nlp)
`Wallet weight = 10`
- Link Signer:Wallet weight = 30Can only perform a max of 50 link signer requests every 7 days per subaccount.

Link Signer:Wallet weight = 30

[Link Signer](/developer-resources/api/gateway/executes/link-signer)
`Wallet weight = 30`
- Can only perform a max of 50 link signer requests every 7 days per subaccount.

Can only perform a max of 50 link signer requests every 7 days per subaccount.

- Transfer Quote:Wallet weight = 10Can only transfer to a max of 5 new recipients within 24hrs.

Transfer Quote:Wallet weight = 10

[Transfer Quote:](/developer-resources/api/gateway/executes/transfer-quote)
`Wallet weight = 10`
- Can only transfer to a max of 5 new recipients within 24hrs.

Can only transfer to a max of 5 new recipients within 24hrs.

## Trigger Service Limits

The trigger service has additional limits specific to conditional orders:

- Pending trigger orders: Max of25pending trigger orders per product per subaccount

Pending trigger orders: Max of25pending trigger orders per product per subaccount

`25`
- TWAP orders: Must use IOC execution type and cannot be combined with isolated margin

TWAP orders: Must use IOC execution type and cannot be combined with isolated margin

[PreviousOrder Appendix](/developer-resources/api/order-appendix)
[NextErrors](/developer-resources/api/errors)

Last updated23 days ago