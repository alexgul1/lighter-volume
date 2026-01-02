---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries/all-products
title: All Products
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Queries
[Queries](/developer-resources/api/gateway/queries)

# All Products

Gets info about all available products including: product id, oracle price, configuration, state, etc.

## Rate limits

- 480 requests/min or 8 requests/sec per IP address. (weight = 5)

480 requests/min or 8 requests/sec per IP address. (weight = 5)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
 "type": "all_products"
}
```

GET[GATEWAY_REST_ENDPOINT]/query?type=all_products

`[GATEWAY_REST_ENDPOINT]/query?type=all_products`

POST [GATEWAY_REST_ENDPOINT]/query

`POST [GATEWAY_REST_ENDPOINT]/query`

Body

```
{
 "type": "all_products"
}
```

## Response

Note:

- A product is some asset / position an account can take on.

A product is some asset / position an account can take on.

- A market is a venue for a product against USDT0.

A market is a venue for a product against USDT0.

- All products have a market quoted against USDT0, except for product 0.

All products have a market quoted against USDT0, except for product 0.

- Product 0 is the USDT0 asset itself.

Product 0 is the USDT0 asset itself.

- You can retrieve product symbols viaSymbolsquery.Body

You can retrieve product symbols viaSymbolsquery.Body

[Symbols](/developer-resources/api/symbols)
[PreviousSymbols](/developer-resources/api/gateway/queries/symbols)
[NextEdge All Products](/developer-resources/api/gateway/queries/edge-all-products)

Last updated1 month ago