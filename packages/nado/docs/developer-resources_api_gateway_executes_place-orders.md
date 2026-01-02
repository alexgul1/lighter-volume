---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/place-orders
title: Place Orders
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Place Orders

Places multiple orders on Nado's orderbook in a single request.

Place multiple orders in a single request. This is more efficient than placing orders individually and allows for better control over batch order placement.

## Rate limits

- With spot leverage: 600 orders/minute or 10 orders/sec per wallet. (weight=1 per order)

With spot leverage: 600 orders/minute or 10 orders/sec per wallet. (weight=1 per order)

- Without spot leverage: 30 orders/min or 5 orders every 10 seconds per wallet. (weight = 20 per order)

Without spot leverage: 30 orders/min or 5 orders every 10 seconds per wallet. (weight = 20 per order)

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

Note: There is a 50ms processing penalty for eachplace_ordersrequest to ensure fair sequencing and prevent gaming of the matching engine.

`place_orders`

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "place_orders": {
    "orders": [
      {
        "product_id": 2,
        "order": {
          "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
          "priceX18": "100000000000000000000000",
          "amount": "1000000000000000000",
          "expiration": "4294967295",
          "nonce": "1757062078359666688",
          "appendix": "1"
        },
        "signature": "0x...",
        "id": 100
      },
      {
        "product_id": 3,
        "order": {
          "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
          "priceX18": "3800000000000000000000",
          "amount": "2000000000000000000",
          "expiration": "4294967295",
          "nonce": "1757062078359666689",
          "appendix": "1"
        },
        "signature": "0x...",
        "id": 101
      }
    ],
    "stop_on_failure": false
  }
}
```

POST [GATEWAY_REST_ENDPOINT]/execute

`POST [GATEWAY_REST_ENDPOINT]/execute`

Body

## Request Parameters

orders

array

Yes

Array of order objects to place. Each order follows the same structure asPlace Order.

[Place Order](/developer-resources/api/gateway/executes/place-order)

orders[].product_id

number

Yes

Id of spot / perp product for which to place order.

orders[].order

object

Yes

Order object (same structure as single order placement).

orders[].signature

string

Yes

Hex string representing hash of thesignedorder.

orders[].digest

string

No

Hex string representing a hash of the order.

orders[].spot_leverage

boolean

No

Indicates whether leverage should be used for this order. Defaults totrue.

`true`

orders[].id

number

No

An optional id returned inFillandOrderUpdateevents.

`Fill`
`OrderUpdate`

stop_on_failure

boolean

No

Iftrue, stops processing remaining orders when the first order fails. Already successfully placed orders are NOT cancelled. Defaults tofalse.

`true`
`false`

## Response

### Response Fields

digest

Order digest (32-byte hash) if successfully placed,nullif failed.

`null`

error

Error message if order failed,nullif successful.

`null`

## Behavior

- Partial Success: By default, orders are processed independently. Some orders may succeed while others fail.

Partial Success: By default, orders are processed independently. Some orders may succeed while others fail.

- Stop on Failure: Setstop_on_failure: trueto stop processing remaining orders when the first order fails. Already successfully placed orders remain on the book.

Stop on Failure: Setstop_on_failure: trueto stop processing remaining orders when the first order fails. Already successfully placed orders remain on the book.

`stop_on_failure: true`
- Order Signing: Each order must be individually signed using EIP712 (seeSigningfor details).

Order Signing: Each order must be individually signed using EIP712 (seeSigningfor details).

[Signing](/developer-resources/api/gateway/signing)
- Rate Limits: Rate limit weight is calculated per order (1 per order with leverage, 20 per order without).

Rate Limits: Rate limit weight is calculated per order (1 per order with leverage, 20 per order without).

## Use Cases

- Spread Trading: Place both legs of a spread trade in one request

Spread Trading: Place both legs of a spread trade in one request

- Multiple Markets: Open positions across multiple products in one request

Multiple Markets: Open positions across multiple products in one request

## Example

Placing BTC and ETH perp orders simultaneously:

## See Also

- Place Order- Single order placement

Place Order- Single order placement

[Place Order](/developer-resources/api/gateway/executes/place-order)
- Cancel And Place- Atomic cancel and place

Cancel And Place- Atomic cancel and place

[Cancel And Place](/developer-resources/api/gateway/executes/cancel-and-place)
- Signing- EIP712 order signing

Signing- EIP712 order signing

[Signing](/developer-resources/api/gateway/signing)
[PreviousPlace Order](/developer-resources/api/gateway/executes/place-order)
[NextCancel Orders](/developer-resources/api/gateway/executes/cancel-orders)

Last updated1 month ago