---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/liquidate-subaccount
title: Liquidate Subaccount
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Liquidate Subaccount

Submits a transaction to liquidate a subaccount's balance for a specified liquidation amount.

## Rate limits

- 30 liquidations/min or 5 liquidations every 10 seconds per wallet. (weight=20)

30 liquidations/min or 5 liquidations every 10 seconds per wallet. (weight=20)

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```

{
  "liquidate_subaccount": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "liquidatee": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "productId": 1,
      "isEncodedSpread": false,
      "amount": "1000000000000000000",
      "nonce": "1"
    },
    "signature": "0x"
  }
}
```

POST [GATEWAY_REST_ENDPOINT]/execute

`POST [GATEWAY_REST_ENDPOINT]/execute`

Body

```

{
  "liquidate_subaccount": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "liquidatee": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "mode": 0,
      "healthGroup": 1,
      "amount": "1000000000000000000",
      "nonce": "1"
    },
    "signature": "0x"
  }
}
```

## Request Parameters

tx

object

Yes

Liquidate subaccount transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/gateway/executes/liquidate-subaccount#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.liquidatee

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the subaccount being liquidated.

tx.productId

number

Yes

Perp Liquidation:

- A valid perp product Id.

A valid perp product Id.

Spot Liquidation:

- A valid spot product Id.

A valid spot product Id.

Spread Liquidation:

- An encoded perp / spot product Ids, where the lower 16 bits represent the spot product and the higher 16 bits represent the perp product.isEncodedSpreadmust be set totruefor spread liquidation. SeeSigningsection for more details.

An encoded perp / spot product Ids, where the lower 16 bits represent the spot product and the higher 16 bits represent the perp product.isEncodedSpreadmust be set totruefor spread liquidation. SeeSigningsection for more details.

`isEncodedSpread`
`true`
[Signing](/developer-resources/api/gateway/executes/liquidate-subaccount#signing)

tx.isEncodedSpread

bool

Yes

When set totrue, theproductIdis expected to encode a perp and spot product Ids as follows:(perp_id << 16) | spot_id

`true`
`productId`
`(perp_id << 16) | spot_id`

tx.amount

string

Yes

The amount to liquidate multiplied by 1e18, sent as a string.

tx.nonce

string

Yes

This is an incrementing nonce, can be obtained using theNoncesquery.

[Nonces](/developer-resources/api/gateway/queries/nonces)

signature

string

Yes

Signed transaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/liquidate-subaccount#signing)

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier.

`sender`
`bytes32`

liquidatee: abytes32sent as a hex string; includes the address and the subaccount identifier.

`liquidatee`
`bytes32`

productId: The product to liquidate as well as the liquidation mode.

`productId`
- Perp liquidation⇒ A validperpproduct id is provided andisEncodedSpreadis set tofalse.

Perp liquidation⇒ A validperpproduct id is provided andisEncodedSpreadis set tofalse.

`perp`
`isEncodedSpread`
`false`
- Spot liquidation⇒ A validspotproduct id is provided andisEncodedSpreadis set tofalse

Spot liquidation⇒ A validspotproduct id is provided andisEncodedSpreadis set tofalse

`spot`
`isEncodedSpread`
`false`
- Spread Liquidation=> If there are perp and spot positions in different directions, liquidate both at the same time. Must be set to a 32 bits integer where the lower 16 bits represent thespotproduct and the higher 16 bits represent theperpproduct.isEncodedSpreadmust be set totrue.

Spread Liquidation=> If there are perp and spot positions in different directions, liquidate both at the same time. Must be set to a 32 bits integer where the lower 16 bits represent thespotproduct and the higher 16 bits represent theperpproduct.isEncodedSpreadmust be set totrue.

`spot`
`perp`
`isEncodedSpread`
`true`

Computing****************productId****************for Spread Liquidation

isEncodedSpread: indicates whetherproductIdencodes both aspotand aperpproduct Id for spread liquidation.

`isEncodedSpread`
`productId`
`spot`
`perp`

amount: the amount to liquidate multiplied by 1e18, sent as a string. Can be positive or negative, depending on if the user’s balance is positive or negative.

`amount`

nonce: thetx_nonce. This is an incrementing nonce, can be obtained using theNoncesquery.

`nonce`
`tx_nonce`
[Nonces](/developer-resources/api/gateway/queries/nonces)

Note: for signing you should always use the data type specified in the solidity struct which might be different from the type sent in the request e.g:nonceshould be anuint64forSigningbut should be sent as astringin the final payload.

`nonce`
`uint64`
`string`

## Response

#### Success

#### Failure

[PreviousTransfer Quote](/developer-resources/api/gateway/executes/transfer-quote)
[NextMint NLP](/developer-resources/api/gateway/executes/mint-nlp)

Last updated1 month ago