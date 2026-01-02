---
url: https://docs.nado.xyz/developer-resources/api/v2/contracts
title: Contracts
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# Contracts

Retrieve summary of perp contracts traded on Nado.

## Request

GET[ARCHIVE_V2_ENDPOINT]/contracts?edge={true|false}

`[ARCHIVE_V2_ENDPOINT]/contracts?edge={true|false}`

## Request Parameters

edge

bool

No

Wether to retrieve volume and OI metrics for all chains. When turned off, it only returns metrics for the current chain. Defaults totrue.

## Response

Note: the response is a map ofticker_id-> contract info object.

`ticker_id`

```
{
    "BTC-PERP_USDT0": {
        "product_id": 1,
        "ticker_id": "BTC-PERP_USDT0",
        "base_currency": "BTC-PERP",
        "quote_currency": "USDT0",
        "last_price": 25744.0,
        "base_volume": 794.154,
        "quote_volume": 20475749.367766097,
        "product_type": "perpetual",
        "contract_price": 25830.738843799172,
        "contract_price_currency": "USD",
        "open_interest": 3059.325,
        "open_interest_usd": 79024625.11330591,
        "index_price": 25878.913320746455,
        "mark_price": 25783.996946729356,
        "funding_rate": -0.003664562348812546,
        "next_funding_rate_timestamp": 1694379600,
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

product_type

string

No

Name of product type.

contract_price

string

No

Describes the price per contract.

contract_price_currency

string

No

Describes the currency which the contract is priced in.

open_interest

decimal

No

The current open interest for the perp contract.

open_interest_usd

decimal

No

The value in USD of the current open interest.

index_price

decimal

No

Last calculated index price for underlying of contract

funding_rate

decimal

No

Current 24hr funding rate. Can compute hourly funding rate dividing by 24.

next_funding_rate_timestamp

integer

No

Timestamp of the next funding rate change

price_change_percent_24h

decimal

No

24-hours % price change of market pair

[PreviousTickers](/developer-resources/api/v2/tickers)
[NextTrades](/developer-resources/api/v2/trades)

Last updated1 month ago