---
url: https://docs.nado.xyz/developer-resources/api/subscriptions/streams
title: Streams
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Subscriptions
[Subscriptions](/developer-resources/api/subscriptions)

# Streams

API to manage subscriptions to available streams via websocket.

## Available Streams

See below the available streams you can subscribe to:

```
pub enum StreamSubscription {
    // pass `null` product_id to subscribe to all products
    OrderUpdate { product_id: Option<u32>, subaccount: H256 },
    Trade { product_id: u32 },
    BestBidOffer { product_id: u32 },
    // pass `null` product_id to subscribe to all products
    Fill { product_id: Option<u32>, subaccount: H256 },
    // pass `null` product_id to subscribe to all products
    PositionChange { product_id: Option<u32>, subaccount: H256},
    BookDepth { product_id: u32 },
    // pass `null` product_id to subscribe to all products
    Liquidation { product_id: Option<u32> },
    LatestCandlestick {
        product_id: u32,
        // time interval in seconds (e.g., 60, 300, 900, 3600)
        granularity: i32
    },
    FundingPayment { product_id: u32 },
    // pass `null` product_id to subscribe to all products
    FundingRate { product_id: Option<u32> }
}
```

## Subscribing to a stream

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: Yes.

Note: Setproduct_idtonullto subscribe to order updates across all products for the subaccount.

`product_id`
`null`

Subscribe to all products:

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Note: Setproduct_idtonullto subscribe to fills across all products for the subaccount.

`product_id`
`null`

Subscribe to all products:

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Note: Setproduct_idtonullto subscribe to position changes across all products for the subaccount.

`product_id`
`null`

Subscribe to all products:

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Note: Setproduct_idtonullto subscribe to liquidations across all products.

`product_id`
`null`

Subscribe to all products:

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

See all supportesgranularityvalues inAvailable Granularities

`granularity`
[Available Granularities](/developer-resources/api/archive-indexer/candlesticks#available-granularities)

Requires Authentication: No.

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Requires Authentication: No.

Note: Setproduct_idtonullto subscribe to funding rate updates across all products.

`product_id`
`null`

Subscribe to all products:

### Response

## Unsubscribing

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Unsubscribe from all products:

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

### Response

## Listing subscribed streams

### Response

[PreviousAuthentication](/developer-resources/api/subscriptions/authentication)
[NextEvents](/developer-resources/api/subscriptions/events)

Last updated1 month ago