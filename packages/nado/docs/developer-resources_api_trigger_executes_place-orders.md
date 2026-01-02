---
url: https://docs.nado.xyz/developer-resources/api/trigger/executes/place-orders
title: Place Orders
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Trigger
[Trigger](/developer-resources/api/trigger)
- Executes
[Executes](/developer-resources/api/trigger/executes)

# Place Orders

Places multiple trigger orders in a single request.

Place multiple trigger orders in a single request. This is more efficient than placing orders individually and allows for better control over batch trigger order placement.

## Rate limits

- A max of 25 pending trigger orders per product per subaccount

A max of 25 pending trigger orders per product per subaccount

See more details inTrigger Service Limits.

[Trigger Service Limits](/developer-resources/api/rate-limits#trigger-service-limits)

Important: All orders in a batch must belong to the same subaccount. Orders with different senders will be rejected.

## Request

POST [TRIGGER_ENDPOINT]/execute

`POST [TRIGGER_ENDPOINT]/execute`

### Body

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
          "appendix": "4096"
        },
        "trigger": {
          "price_trigger": {
            "price_requirement": {
              "oracle_price_below": "100000000000000000000000"
            }
          }
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
          "appendix": "4096"
        },
        "trigger": {
          "price_trigger": {
            "price_requirement": {
              "oracle_price_above": "3800000000000000000000"
            }
          }
        },
        "signature": "0x...",
        "id": 101
      }
    ],
    "stop_on_failure": false
  }
}
```

## Request Parameters

orders

array

Yes

Array of trigger order objects to place. Each order follows the same structure asPlace Order.All orders must have the same sender.

[Place Order](/developer-resources/api/trigger/executes/place-order)

orders[].product_id

number

Yes

Id of spot / perp product for which to place order.

orders[].order

object

Yes

Order object (same structure as single order placement).

orders[].trigger

object

Yes

Trigger criteria - either price_trigger or time_trigger. SeePlace Orderfor details.

[Place Order](/developer-resources/api/trigger/executes/place-order)

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

- Stop on Failure: Setstop_on_failure: trueto stop processing remaining orders when the first order fails. Already successfully placed orders remain active.

Stop on Failure: Setstop_on_failure: trueto stop processing remaining orders when the first order fails. Already successfully placed orders remain active.

`stop_on_failure: true`
- Same Sender Required: All orders in a batch must have the same sender. Mixed sender batches will be rejected withBatchSenderMismatcherror.

Same Sender Required: All orders in a batch must have the same sender. Mixed sender batches will be rejected withBatchSenderMismatcherror.

`BatchSenderMismatch`
- Order Signing: Each order must be individually signed using EIP712 (seeSigningfor details).

Order Signing: Each order must be individually signed using EIP712 (seeSigningfor details).

[Signing](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/api/gateway/executes/signing/README.md)
- Per-Order Limits: The 25 pending trigger orders per product per subaccount limit applies to each order individually.

Per-Order Limits: The 25 pending trigger orders per product per subaccount limit applies to each order individually.

## Use Cases

- Multi-Market Stop Losses: Set stop loss triggers across multiple products simultaneously

Multi-Market Stop Losses: Set stop loss triggers across multiple products simultaneously

- Bracket Orders: Place both take profit and stop loss triggers together

Bracket Orders: Place both take profit and stop loss triggers together

- Conditional Exits: Create multiple exit strategies across different products

Conditional Exits: Create multiple exit strategies across different products

## Example

Placing stop loss triggers for BTC and ETH perps:

## See Also

- Place Order- Single trigger order placement

Place Order- Single trigger order placement

[Place Order](/developer-resources/api/trigger/executes/place-order)
- Cancel Orders- Cancel multiple trigger orders

Cancel Orders- Cancel multiple trigger orders

[Cancel Orders](/developer-resources/api/trigger/executes/cancel-orders)
- List Trigger Orders- Query active trigger orders

List Trigger Orders- Query active trigger orders

[List Trigger Orders](/developer-resources/api/trigger/queries/list-trigger-orders)
[PreviousPlace Order](/developer-resources/api/trigger/executes/place-order)
[NextCancel Orders](/developer-resources/api/trigger/executes/cancel-orders)

Last updated1 month ago