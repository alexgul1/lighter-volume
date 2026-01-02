---
url: https://docs.nado.xyz/developer-resources/typescript-sdk/how-to/query-markets-and-products
title: Query Markets & Products
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📘TypeScript SDK
[📘TypeScript SDK](/developer-resources/typescript-sdk)
- How To
[How To](/developer-resources/typescript-sdk/how-to)

# Query Markets & Products

In this section, we'll be going over fetching:

- State and config for all markets & products.

State and config for all markets & products.

- Latest market price for one product.

Latest market price for one product.

- Market liquidity for one product (i.e. amount of liquidity at each price tick).

Market liquidity for one product (i.e. amount of liquidity at each price tick).

For all available queries, consult theAPI reference.

[API reference](https://nadohq.github.io/nado-typescript-sdk/)

## All Markets Query

ThegetAllEngineMarketsfunction returns the state of all markets from our backend API, which reflects the state of the off-chain matching engine.

`getAllEngineMarkets`

```
// Fetches state from offchain sequencer 
const allMarkets = await nadoClient.market.getAllMarkets();
```

## Latest market price

ThegetLatestMarketPricefunction returns the market price data of a single product given by its product id.

`getLatestMarketPrice`

```
const latestMarketPrice = await nadoClient.market.getLatestMarketPrice({
  productId: 1,
});
```

### Market liquidity

ThegetMarketLiquidityfunction returns the available liquidity at each price tick. The number of price levels for each side of the book is given bydepth. For example, a depth of2will retrieve 2 levels of bids and 2 levels of asks. Price levels are separated by thepriceIncrementof the market, given by thegetAllMarketsquery.

`getMarketLiquidity`
`depth`
`2`
`priceIncrement`
`getAllMarkets`

## Full example

[PreviousUseful Common Functions](/developer-resources/typescript-sdk/how-to/useful-common-functions)
[NextDeposit Funds](/developer-resources/typescript-sdk/how-to/deposit-funds)

Last updated1 month ago