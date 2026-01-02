---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/mint-nlp
title: Mint NLP
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Mint NLP

Mints specified amount of NLP tokens.

## Rate limits

- Wallet weight =10- allows 60 mints/min or 10 mints every 10 seconds per wallet.

Wallet weight =10- allows 60 mints/min or 10 mints every 10 seconds per wallet.

`10`

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "mint_nlp": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "quoteAmount": "1000000000000000000",
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
  "mint_nlp": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "productId": 1,
      "amountBase": "1000000000000000000",
      "quoteAmountLow": "10000000000000000000000",
      "quoteAmountHigh": "20000000000000000000000",
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

Mint NLP transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/gateway/executes/mint-nlp#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.quoteAmount

string

Yes

This amount of quote to be consumed by minting NLPs multiplied by 1e18, sent as a string.

tx.nonce

string

Yes

This is an incrementing nonce, can be obtained using theNoncesquery.

[Nonces](/developer-resources/api/gateway/queries/nonces)

signature

string

Yes

Hex string representing hash of thesignedtransaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/mint-nlp#signing)

spot_leverage

boolean

No

Indicates whether leverage should be used; when set tofalse, the mint fails if the transaction causes a borrow on the subaccount. Defaults totrue.

`false`
`true`

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier.

`sender`
`bytes32`

quoteAmount: this is the amount of quote to be consumed by minting NLPs, sent as a string. This must be positive and must be specified with 18 decimals.

`quoteAmount`

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

[PreviousLiquidate Subaccount](/developer-resources/api/gateway/executes/liquidate-subaccount)
[NextBurn NLP](/developer-resources/api/gateway/executes/burn-nlp)

Last updated8 days ago