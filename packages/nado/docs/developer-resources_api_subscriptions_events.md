---
url: https://docs.nado.xyz/developer-resources/api/subscriptions/events
title: Events
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Subscriptions
[Subscriptions](/developer-resources/api/subscriptions)

# Events

Each subscription stream has a corresponding event that will be broadcasted over websocket.

## Order Update

Update speed: real-time

```
{
  "type": "order_update",
  // timestamp of the event in nanoseconds
  "timestamp": "1695081920633151000", 
  "product_id": 1,
  // order digest
  "digest": "0xf7712b63ccf70358db8f201e9bf33977423e7a63f6a16f6dab180bdd580f7c6c",
  // remaining amount to be filled.
  // will be `0` if the order is either fully filled or cancelled.
  "amount": "82000000000000000",
  // any of: "filled", "cancelled", "placed"
  "reason": "filled",
  // an optional `order id` that can be provided when placing an order
  "id": 100
}
```

### Example Scenarios:

Let's assume your initial order amount is 100 units and each match occurs for an amount of 10 units.

Note: The following events only includeamountandreasonfor simplicity.

`amount`
`reason`

#### Scenario 1: Limit Order Partially Fills and Gets Placed

Your limit order matches against existing orders in the book.

You will receive the following events over websocket, each with the same timestamp but in sequential order:

- Event 1:(90, "filled")— 10 units of your order are filled.

Event 1:(90, "filled")— 10 units of your order are filled.

`(90, "filled")`
- Event 2:(80, "filled")— Another 10 units are filled.

Event 2:(80, "filled")— Another 10 units are filled.

`(80, "filled")`
- Event 3:(80, "placed")— The remaining 80 units are placed on the book.

Event 3:(80, "placed")— The remaining 80 units are placed on the book.

`(80, "placed")`

#### Scenario 2: Immediate-Or-Cancel (IOC) Order Partially Fills

Your IOC order matches against existing orders but is not completely filled.

The events you will receive are as follows:

- Event 1:(90, "filled")— 10 units are filled.

Event 1:(90, "filled")— 10 units are filled.

`(90, "filled")`
- Event 2:(80, "filled")— Another 10 units are filled.

Event 2:(80, "filled")— Another 10 units are filled.

`(80, "filled")`
- Event 3:(0, "cancelled")— The remaining order is cancelled.Note: If your IOC order is fully filled, the last event you will receive is(0, "filled").

Event 3:(0, "cancelled")— The remaining order is cancelled.Note: If your IOC order is fully filled, the last event you will receive is(0, "filled").

`(0, "cancelled")`
`(0, "filled")`

#### Scenario 3: Resting Limit Order Gets Matched

Your existing, or "resting," limit order matches against an incoming order.

You will receive the following event:(90, "filled")— 10 units of your resting limit order are filled.

`(90, "filled")`

#### Scenario 4: Resting Limit Order Gets Cancelled

Your resting limit order could be cancelled for various reasons, such as manual cancellation, expiration, failing health checks, or self-trade prevention.

In any of these cases, you will receive:(0, "cancelled")

`(0, "cancelled")`

#### Scenario 5: IOC order doesn't cross the book or FOK order fails to be entirely filled

In any of these cases, you will receive:(0, "cancelled")

`(0, "cancelled")`

## Trade

Update speed: real-time

## Best Bid Offer

Update speed: real-time

## Fill

Update speed: real-time

## Position Change

Update speed: real-time

Note:that it is possible that back to backposition_changeevents have the same fields except fortimestamp. Additionally,position_changeevents are not sent on interest and funding payments, and also are not sent on actions done through slow mode (except deposits). The full list of actions that will trigger aPositionChangeevent are:

`position_change`
`timestamp`
`position_change`
`PositionChange`
- Minting or burning NLP tokens

Minting or burning NLP tokens

- Liquidating a subaccount

Liquidating a subaccount

- Matching orders

Matching orders

- Depositing or withdrawing spot

Depositing or withdrawing spot

- Settling PNL

Settling PNL

## Book Depth

Update speed: once every 50ms

Note: To keep an updated local orderbook, do the following:

- Subscribe to thebook_depthstream and queue up events.

Subscribe to thebook_depthstream and queue up events.

`book_depth`
- Get a market data snapshot by callingMarketLiquidity. The snapshot contains atimestampin the response.

Get a market data snapshot by callingMarketLiquidity. The snapshot contains atimestampin the response.

[MarketLiquidity](https://docs.vertexprotocol.com/developer-resources/api/gateway/queries/market-liquidity)
`timestamp`
- Apply events withmax_timestamp> snapshottimestamp.

Apply events withmax_timestamp> snapshottimestamp.

`max_timestamp`
`timestamp`
- When you receive an event where itslast_max_timestampis not equal to themax_timestampof the last event you've received, it means some events were lost and you should repeat 1-3 again.

When you receive an event where itslast_max_timestampis not equal to themax_timestampof the last event you've received, it means some events were lost and you should repeat 1-3 again.

`last_max_timestamp`
`max_timestamp`

## Liquidation

Update speed: real-time

## Latest Candlestick

Update speed: real-time

## Funding Payment

Update speed: real-time at the time of payment (payments happen hourly).

## Funding Rate

Update speed: real-time (updates occur every 20 seconds).

Note: Thefunding_rate_x18andupdate_timevalues are identical to those returned by theFunding Rateindexer endpoint.

`funding_rate_x18`
`update_time`
[Funding Rate](/developer-resources/api/archive-indexer/funding-rate)
[PreviousStreams](/developer-resources/api/subscriptions/streams)
[NextRate limits](/developer-resources/api/subscriptions/rate-limits)

Last updated1 month ago