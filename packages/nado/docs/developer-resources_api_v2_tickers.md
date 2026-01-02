---
url: https://docs.nado.xyz/developer-resources/api/v2/tickers
title: Tickers
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# Tickers

Retrieve 24-hour pricing and volume information on each market pair available on Nado.

## Request

GET[ARCHIVE_V2_ENDPOINT]/tickers?market={spot|perp}&edge={true|false}

`[ARCHIVE_V2_ENDPOINT]/tickers?market={spot|perp}&edge={true|false}`

## Request Parameters

market

string

No

Indicates the corresponding market to fetch trading tickers info for. Allowed values are:spotandperp. When nomarketparam is provided, it returns all available tickers.

`spot`
`perp`
`market`

edge

bool

No

Whether to retrieve volume metrics for all chains. When turned off, it only returns metrics for the current chain. Defaults totrue.

## Response

Note: the response is a map ofticker_id-> ticker info object.

`ticker_id`

```
{
    "BTC-PERP_USDT0": {
        "product_id": 1,
        "ticker_id": "BTC-PERP_USDT0",
        "base_currency": "BTC",
        "quote_currency": "USDT0",
        "last_price": 25728.0,
        "base_volume": 552.048,
        "quote_volume": 14238632.207250029,
        "price_change_percent_24h": -0.6348599635253989
    }
}
```

## Response Fields

product_id

u32

No

Unique identifier for the product.

ticker_id

string

No

Identifier of a ticker with delimiter to separate base/target.

base_currency

string

No

Symbol of the base asset.

quote_currency

string

No

Symbol of the target asset.

last_price

decimal

No

Last transacted price of base currency based on given quote currency.

base_volume

decimal

No

24-hours trading volume for the pair (unit in base)

quote_volume

decimal

No

24-hours trading volume for the pair (unit in quote/target)

price_change_percent_24h

decimal

No

24-hours % price change of market pair

[PreviousOrderbook](/developer-resources/api/v2/orderbook)
[NextContracts](/developer-resources/api/v2/contracts)

Last updated1 month ago