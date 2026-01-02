---
url: https://docs.nado.xyz/developer-resources/api/v2/trades
title: Trades
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- V2
[V2](/developer-resources/api/v2)

# Trades

Retrieve historical trades for a given market pair. Most recent trades at the top.

## Request

GET[ARCHIVE_V2_ENDPOINT]/trades?ticker_id=BTC-PERP_USDT0&limit=10&max_trade_id=1000000

`[ARCHIVE_V2_ENDPOINT]/trades?ticker_id=BTC-PERP_USDT0&limit=10&max_trade_id=1000000`

## Request Parameters

ticker_id

string

Yes

Identifier of a ticker with delimiter to separate base/target.

limit

integer

No

Number of historical trades to retrieve. Defaults to 100. Max of 500.

max_trade_id

integer

No

Max trade id to include in the result. Use for pagination.

## Response

```
[
    {
        "product_id": 1,
        "ticker_id": "BTC-PERP_USDT0",
        "trade_id": 6351,
        "price": 112029.5896,
        "base_filled": -0.388,
        "quote_filled": 43467.4807648,
        "timestamp": 1757335618,
        "trade_type": "sell"
    },
    {
        "product_id": 1,
        "ticker_id": "BTC-PERP_USDT0",
        "trade_id": 6350,
        "price": 112032.58899999999,
        "base_filled": -0.179,
        "quote_filled": 20053.833431,
        "timestamp": 1757335618,
        "trade_type": "sell"
    }
]
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

trade_id

integer

No

A unique ID associated with the trade for the currency pair transaction.

price

decimal

No

Trade price of base asset in target currency.

base_filled

decimal

No

Amount of base volume filled in trade.

quote_filled

decimal

No

Amount of quote/target volume filled in trade.

timestamp

integer

No

Unix timestamp in seconds for when the transaction occurred.

trade_type

string

No

Indicates the type of the transaction that was completed ("buy" or "sell").

[PreviousContracts](/developer-resources/api/v2/contracts)
[NextOrder Appendix](/developer-resources/api/order-appendix)

Last updated1 month ago