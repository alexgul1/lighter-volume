---
url: https://docs.nado.xyz/developer-resources/api/trigger/executes/place-order
title: Place Order
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Trigger
[Trigger](/developer-resources/api/trigger)
- Executes
[Executes](/developer-resources/api/trigger/executes)

# Place Order

Places an order to be triggered if a provided price or time criteria is met.

## Rate limits

- A max of 25 pending trigger orders per product per subaccount

A max of 25 pending trigger orders per product per subaccount

See more details inTrigger Service Limits.

[Trigger Service Limits](/developer-resources/api/rate-limits#trigger-service-limits)

## Request

POST [TRIGGER_ENDPOINT]/execute

`POST [TRIGGER_ENDPOINT]/execute`

Body

```

{
  "place_order": {
    "product_id": 1,
    "order": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "priceX18": "9900000000000000000000",
      "amount": "1000000000000000000",
      "expiration": "4294967295",
      "nonce": "1757062078359666688"
    },
    "trigger": {
      "price_trigger": {
        "price_requirement": {
          "oracle_price_below": "9900000000000000000000"
        }
      }
    },
    "signature": "0x",
    "id": 100
  }
}
```

POST [TRIGGER_ENDPOINT]/execute

`POST [TRIGGER_ENDPOINT]/execute`

Body

## Request Parameters

product_id

number

Yes

Id of spot / perp product for which to place order. UseAll productsquery to retrieve all valid product ids.

[All products](/developer-resources/api/gateway/queries/all-products)

order

object

Yes

Order object, seeSigningsection for details on each order field.

[Signing](/developer-resources/api/gateway/executes/place-order#signing)

signature

string

Yes

Hex string representing hash of thesignedorder. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/place-order#signing)

trigger

object

Yes

Trigger criteria can be either:Price-based:{"price_trigger": {"price_requirement": {"oracle_price_above": "{PRICE}"}}}Time-based (TWAP):{"time_trigger": {"interval": {SECONDS}, "amounts": ["{AMOUNT1}", "{AMOUNT2}", ...]}}

`{"price_trigger": {"price_requirement": {"oracle_price_above": "{PRICE}"}}}`
`{"time_trigger": {"interval": {SECONDS}, "amounts": ["{AMOUNT1}", "{AMOUNT2}", ...]}}`

digest

string

No

Hex string representing a hash of the order.

spot_leverage

boolean

No

Indicates whether leverage should be used; when set tofalse, placing the order fails if the transaction causes a borrow on the subaccount. Defaults totrue.

`false`
`true`

id

number

No

An optional id that when provided is returned as part ofFillandOrderUpdatestream events when the order is triggered / executed. Seegateway > place orderandsubscriptionsfor more details.

`Fill`
`OrderUpdate`
[gateway > place order](/developer-resources/api/gateway/executes/place-order)
[subscriptions](/developer-resources/api/subscriptions)

Price Trigger Options:

- oracle_price_above: Order is triggered if the oracle price is above or at the indicated price.

oracle_price_above: Order is triggered if the oracle price is above or at the indicated price.

`oracle_price_above`
- oracle_price_below: Order is triggered if the oracle price is below or at the indicated price.

oracle_price_below: Order is triggered if the oracle price is below or at the indicated price.

`oracle_price_below`
- last_price_above: Order is triggered if the last trade price is above or at the indicated price.

last_price_above: Order is triggered if the last trade price is above or at the indicated price.

`last_price_above`
- last_price_below: Order is triggered if the last trade price is below or at the indicated price.

last_price_below: Order is triggered if the last trade price is below or at the indicated price.

`last_price_below`
- mid_price_above: Order is triggered if the mid book price is above or at the indicated price.

mid_price_above: Order is triggered if the mid book price is above or at the indicated price.

`mid_price_above`
- mid_price_below: Order is triggered if the mid book price is below or at the indicated price.

mid_price_below: Order is triggered if the mid book price is below or at the indicated price.

`mid_price_below`

TWAP (Time-Weighted Average Price) Trigger:

- time_trigger: Executes orders at regular intervals over time.interval: Time in seconds between each execution.amounts: Optional array specifying the exact amount for each execution. If not provided, the total order amount is split evenly across executions.

time_trigger: Executes orders at regular intervals over time.

`time_trigger`
- interval: Time in seconds between each execution.

interval: Time in seconds between each execution.

`interval`
- amounts: Optional array specifying the exact amount for each execution. If not provided, the total order amount is split evenly across executions.

amounts: Optional array specifying the exact amount for each execution. If not provided, the total order amount is split evenly across executions.

`amounts`
- TWAP orders must use IOC (Immediate or Cancel) execution type only

TWAP orders must use IOC (Immediate or Cancel) execution type only

- TWAP orders cannot be combined with isolated margin

TWAP orders cannot be combined with isolated margin

- Use thelist_twap_executionsquery to track individual execution statuses.

Use thelist_twap_executionsquery to track individual execution statuses.

`list_twap_executions`

## Trigger Order Dependencies

Price triggerscan optionally depend on other orders being filled first. This allows creating complex order chains where one trigger only activates after another order executes.

Dependency Configuration:

Parameters:

- digest: The order digest (32-byte hex string) that must be filled before this trigger activates

digest: The order digest (32-byte hex string) that must be filled before this trigger activates

`digest`
- on_partial_fill:true: Trigger activates when the dependency order is partially filledfalse: Trigger only activates when the dependency order is completely filled

on_partial_fill:

`on_partial_fill`
- true: Trigger activates when the dependency order is partially filled

true: Trigger activates when the dependency order is partially filled

`true`
- false: Trigger only activates when the dependency order is completely filled

false: Trigger only activates when the dependency order is completely filled

`false`

Important Notes:

- Dependencies areonly supported for price triggers, not TWAP orders

Dependencies areonly supported for price triggers, not TWAP orders

- Dependency orders can be regular orders or other trigger orders

Dependency orders can be regular orders or other trigger orders

- Circular dependencies are not allowed

Circular dependencies are not allowed

- If a dependency order is cancelled, the dependent trigger order is also cancelled

If a dependency order is cancelled, the dependent trigger order is also cancelled

Use Cases:

- Take profit after stop loss: Set a take profit order that only triggers after a stop loss executes

Take profit after stop loss: Set a take profit order that only triggers after a stop loss executes

- Scaling strategies: Execute multiple orders in sequence based on fills

Scaling strategies: Execute multiple orders in sequence based on fills

- Complex exit strategies: Chain multiple conditional exits together

Complex exit strategies: Chain multiple conditional exits together

## Constructing Order Appendix

CRITICAL: The orderappendixfield must be correctly configured for trigger orders. The appendix is a 128-bit integer sent as a string.

`appendix`

### Using Python SDK (Recommended)

### Manual Bit Manipulation

Important constraints:

- TWAP ordersmustuse IOC (order_type=1) execution

TWAP ordersmustuse IOC (order_type=1) execution

- TWAP orderscannotbe combined with isolated margin

TWAP orderscannotbe combined with isolated margin

- For complete appendix encoding specification, seeOrder Appendixdocumentation

For complete appendix encoding specification, seeOrder Appendixdocumentation

[Order Appendix](/developer-resources/api/order-appendix)

## Response

#### Success

#### Failure

[PreviousExecutes](/developer-resources/api/trigger/executes)
[NextPlace Orders](/developer-resources/api/trigger/executes/place-orders)

Last updated1 month ago