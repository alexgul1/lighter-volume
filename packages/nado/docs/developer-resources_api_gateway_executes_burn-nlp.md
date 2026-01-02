---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/burn-nlp
title: Burn NLP
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Burn NLP

Burns specified amount of NLP tokens.

## Rate limits

- 60 burns/min or 10 burns every 10 seconds per wallet. (weight = 10)

60 burns/min or 10 burns every 10 seconds per wallet. (weight = 10)

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "burn_nlp": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "nlpAmount": "10001000000000000000000"
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
  "burn_lp": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "productId": 1,
      "amount": "10001000000000000000000"
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

Burn NLP transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/gateway/executes/burn-nlp#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.nlpAmount

string

Yes

Amount of NLP tokens to burn multiplied by 1e18, sent as a string.

tx.nonce

string

Yes

This is an incrementing nonce, can be obtained using theNoncesquery.

[Nonces](/developer-resources/api/gateway/queries/nonces)

signature

string

Yes

Signed transaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/burn-nlp#signing)

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier.

`sender`
`bytes32`

nlpAmount: amount of NLP tokens to burn, sent as a string. This must be positive and must be specified with 18 decimals.

`nlpAmount`

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

[PreviousMint NLP](/developer-resources/api/gateway/executes/mint-nlp)
[NextLink Signer](/developer-resources/api/gateway/executes/link-signer)

Last updated1 month ago