---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/place-order
title: Place Order
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Place Order

Places an order on Nado's orderbook.

## Rate limits

- With spot leverage: 600 orders/minute or 10 orders/sec per wallet. (weight=1)

With spot leverage: 600 orders/minute or 10 orders/sec per wallet. (weight=1)

- Without spot leverage: 30 orders/min or 5 orders every 10 seconds per wallet. (weight = 20)

Without spot leverage: 30 orders/min or 5 orders every 10 seconds per wallet. (weight = 20)

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```

{
  "place_order": {
    "product_id": 1,
    "order": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "priceX18": "1000000000000000000",
      "amount": "1000000000000000000",
      "expiration": "4294967295",
      "nonce": "1757062078359666688",
      "appendix": "1"
    },
    "signature": "0x",
    "id": 100
  }
}
```

POST [GATEWAY_REST_ENDPOINT]/execute

`POST [GATEWAY_REST_ENDPOINT]/execute`

Body

```

{
  "place_order": {
    "product_id": 1,
    "order": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "priceX18": "1000000000000000000",
      "amount": "1000000000000000000",
      "expiration": "4294967295",
      "nonce": "1757062078359666688"
    },
    "signature": "0x",
    "id": 100
  }
}
```

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

order.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

order.priceX18

string

Yes

Price of the order multiplied by 1e18.

order.amount

string

Yes

Quantity of the order multiplied by 1e18.

order.expiration

string

Yes

A time after which the order should automatically be cancelled, as a timestamp in seconds after the unix epoch.

order.nonce

string

Yes

Used to differentiate between the same order multiple times. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/place-order#signing)

order.appendix

string

Yes

Encodes various order properties including execution types, isolated positions, TWAP parameters, and trigger types. See order appendix section for more details.

signature

string

Yes

Hex string representing hash of thesignedorder. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/place-order#signing)

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

An optional id that when provided is returned as part ofFillandOrderUpdatestream events. Seesubscriptionsfor more details.NOTE: The clientidshould not be used to differentiate orders, as it is not included in the order hash (i.e., the orderdigest). Instead, use the last 20 bits of the order nonce to distinguish between similar orders. For more details, refer toOrder Nonce.

`Fill`
`OrderUpdate`
[subscriptions](/developer-resources/api/subscriptions)
`id`
`digest`
[Order Nonce](/developer-resources/api/gateway/executes/place-order#order-nonce)

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier

`sender`
`bytes32`

priceX18: anint128representing the price of the order multiplied by 1e18, sent as a string. For example, a price of 1 USDT0 would be sent as"1000000000000000000"

`priceX18`
`int128`
`"1000000000000000000"`

amount: anint128representing the quantity of the order multiplied by 1e18, sent as a string. A positive amount means that this is a buy order, and a negative amount means this is a sell order.

`amount`
`int128`

expiration: a time after which the order should automatically be cancelled, as a timestamp in seconds after the unix epoch, sent as a string.

`expiration`

### Order Nonce

nonce: used to differentiate between the same order multiple times, and a user trying to place an order with the same parameters twice. Sent as a string. Encodes two bit of information:

`nonce`
- Most significant44bits encoding the time in milliseconds (arecv_time) after which the order should be ignored by the matching engine

Most significant44bits encoding the time in milliseconds (arecv_time) after which the order should be ignored by the matching engine

`44`
`recv_time`
- Least significant20bits are a random integer used to avoid hash collisionsFor example, to place an order with a random integer of1000, and a discard time 50 ms from now, we would send a nonce of((timestamp_ms() + 50) << 20) + 1000)

Least significant20bits are a random integer used to avoid hash collisions

`20`

For example, to place an order with a random integer of1000, and a discard time 50 ms from now, we would send a nonce of((timestamp_ms() + 50) << 20) + 1000)

`1000`
`((timestamp_ms() + 50) << 20) + 1000)`

Note: for signing you should always use the data type specified in the solidity struct which might be different from the type sent in the request e.g:nonceshould be anuint64forSigningbut should be sent as astringin the final payload.

`nonce`
`uint64`
`string`

## Order Appendix

See more details and examples in ourOrder Appendixpage.

[Order Appendix](/developer-resources/api/order-appendix)

appendix: is a 128-bit integer that encodes extra order parameters like execution type, isolated margin, and trigger type.

`appendix`

### Bit Layout

Fields (from LSB to MSB):

- Version (8 bits, 0–7)– protocol version (currently1)

Version (8 bits, 0–7)– protocol version (currently1)

`1`
- Isolated (1 bit, 8)– whether the order uses isolated margin

Isolated (1 bit, 8)– whether the order uses isolated margin

- Order Type (2 bits, 9–10)– 0 = DEFAULT, 1 = IOC, 2 = FOK, 3 = POST_ONLY0-DEFAULT: Standard limit order behavior1-IOC (Immediate or Cancel): Execute immediately, cancel unfilled portion2-FOK (Fill or Kill): Execute completely or cancel entire order3-POST_ONLY: Only add liquidity, reject if would take liquidity

Order Type (2 bits, 9–10)– 0 = DEFAULT, 1 = IOC, 2 = FOK, 3 = POST_ONLY

- 0-DEFAULT: Standard limit order behavior

0-DEFAULT: Standard limit order behavior

`0`
`DEFAULT`
- 1-IOC (Immediate or Cancel): Execute immediately, cancel unfilled portion

1-IOC (Immediate or Cancel): Execute immediately, cancel unfilled portion

`1`
`IOC (Immediate or Cancel)`
- 2-FOK (Fill or Kill): Execute completely or cancel entire order

2-FOK (Fill or Kill): Execute completely or cancel entire order

`2`
`FOK (Fill or Kill)`
- 3-POST_ONLY: Only add liquidity, reject if would take liquidity

3-POST_ONLY: Only add liquidity, reject if would take liquidity

`3`
`POST_ONLY`
- Reduce Only (1 bit, 11)– only decreases an existing position.

Reduce Only (1 bit, 11)– only decreases an existing position.

- Trigger Type (2 bits, 12–13)– 0 = NONE, 1 = PRICE, 2 = TWAP, 3 = TWAP_CUSTOM_AMOUNTS

Trigger Type (2 bits, 12–13)– 0 = NONE, 1 = PRICE, 2 = TWAP, 3 = TWAP_CUSTOM_AMOUNTS

- Reserved (50 bits, 14–63)– future use

Reserved (50 bits, 14–63)– future use

- Value (64 bits, 64–127)– extra data (isolated margin or TWAP parameters)iftriggeris2or3⇒valuerepresents how many times the TWAP order will execute and the maximum acceptable slippage. Encoded as:times: Number of TWAP executions.slippage_x6: Maximum slippage × 1,000,000 (6 decimal precision).ifisolatedis1⇒valuerepresentsmargin_x6(in x6 precision, 6 decimals) to be transferred to the isolated subaccount when the order gets its first match.otherwise,valueis0.

Value (64 bits, 64–127)– extra data (isolated margin or TWAP parameters)

- iftriggeris2or3⇒valuerepresents how many times the TWAP order will execute and the maximum acceptable slippage. Encoded as:times: Number of TWAP executions.slippage_x6: Maximum slippage × 1,000,000 (6 decimal precision).

iftriggeris2or3⇒valuerepresents how many times the TWAP order will execute and the maximum acceptable slippage. Encoded as:

`trigger`
`2`
`3`
`value`
- times: Number of TWAP executions.

times: Number of TWAP executions.

`times`
- slippage_x6: Maximum slippage × 1,000,000 (6 decimal precision).

slippage_x6: Maximum slippage × 1,000,000 (6 decimal precision).

`slippage_x6`
- ifisolatedis1⇒valuerepresentsmargin_x6(in x6 precision, 6 decimals) to be transferred to the isolated subaccount when the order gets its first match.

ifisolatedis1⇒valuerepresentsmargin_x6(in x6 precision, 6 decimals) to be transferred to the isolated subaccount when the order gets its first match.

`isolated`
`1`
`value`
`margin_x6`
- otherwise,valueis0.

otherwise,valueis0.

`value`
`0`

## Response

#### Success

#### Failure

[PreviousExecutes](/developer-resources/api/gateway/executes)
[NextPlace Orders](/developer-resources/api/gateway/executes/place-orders)

Last updated1 month ago