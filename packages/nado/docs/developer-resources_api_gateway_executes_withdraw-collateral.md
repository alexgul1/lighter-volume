---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/withdraw-collateral
title: Withdraw Collateral
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Withdraw Collateral

Withdraws specified amount of collateral from Nado.

Note: use themax withdrawablequery to determine the max amount you can withdraw for a given spot product.

[max withdrawable](/developer-resources/api/gateway/queries/max-withdrawable)

## Rate limits

- With spot leverage: 60 withdrawals/min or 10 withdrawals every 10 seconds per wallet. (weight = 10)

With spot leverage: 60 withdrawals/min or 10 withdrawals every 10 seconds per wallet. (weight = 10)

- Without spot leverage: 30 withdrawals/min or 5 withdrawals every 10 seconds per wallet. (weight=20)

Without spot leverage: 30 withdrawals/min or 5 withdrawals every 10 seconds per wallet. (weight=20)

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```

{
  "withdraw_collateral": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "productId": 1,
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
  "withdraw_collateral": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "productId": 1,
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

Withdraw collateral transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/gateway/executes/withdraw-collateral#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.productId

number

Yes

A spot product ID to withdraw from.

tx.amount

string

Yes

The amount of the asset to withdraw, denominated in the base ERC20 token of the specified product e.g: USDT0 (product=0) has 6 decimals whereas wETH (product=3) has 18. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/withdraw-collateral#signing)

tx.nonce

string

Yes

This is an incrementing nonce, can be obtained using theNoncesquery.

[Nonces](/developer-resources/api/gateway/queries/nonces)

signature

string

Yes

Hex string representing hash of thesignedtransaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/withdraw-collateral#signing)

spot_leverage

boolean

No

Indicates whether leverage should be used; when set tofalse, the withdrawal fails if the transaction causes a borrow on the subaccount. Defaults totrue.

`false`
`true`

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier.

`sender`
`bytes32`

productId: auint32that specifies the product you’d like to withdraw collateral from; must be for a spot product.

`productId`
`uint32`

amount: the amount of asset to withdraw, sent as a string. Note that this is different from the amounts provided in transactions that aren’tdepositCollateral. This is the raw amount of the ERC20 token you want to receive, i.e. if USDT0 has 6 decimals and you want to withdraw 1 USDT0, specify 1e6; if wETH has 18 decimals and you want to withdraw 1 wETH, specify 1e18. Useall productsquery to view the token address of the corresponding product which can be used to determine the correct decimals to use.

`amount`
`depositCollateral`
[all products](/developer-resources/api/gateway/queries/all-products)

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

[PreviousCancel And Place](/developer-resources/api/gateway/executes/cancel-and-place)
[NextTransfer Quote](/developer-resources/api/gateway/executes/transfer-quote)

Last updated1 month ago