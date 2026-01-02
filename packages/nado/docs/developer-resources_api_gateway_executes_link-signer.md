---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/link-signer
title: Link Signer
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Link Signer

Designates an address to be able to sign executes on behalf of a subaccount.

Each subaccount can have at most one linked signer at a time. A linked signer can perform any execute on behalf of the subaccount it is linked to. Use theLinked Signerquery to view your current linked signer.

[Linked Signer](/developer-resources/api/gateway/queries/linked-signer)

Please note:

- To enable a linked signer, your subaccount must have a minimum of5 USDT0worth in account value.

To enable a linked signer, your subaccount must have a minimum of5 USDT0worth in account value.

## Rate limits

- A max of 50 link signer requests every 7 days per subaccount. (weight=30). Use theLinked Signer Rate Limitquery to check a subaccount's linked signer usage and remaining wait time.

A max of 50 link signer requests every 7 days per subaccount. (weight=30). Use theLinked Signer Rate Limitquery to check a subaccount's linked signer usage and remaining wait time.

[Linked Signer Rate Limit](/developer-resources/api/archive-indexer/linked-signer-rate-limit)

See more general details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```
{
  "link_signer": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "signer": "0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000",
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
  "link_signer": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "signer": "0xeae27ae6412147ed6d5692fd91709dad6dbfc34264656661756c740000000000",
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

A link signer transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/gateway/executes/link-signer#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.signer

string

Yes

Abytes32sent as a hex string; includes the address (first 20 bytes) that'll be used as thesender'ssigner. the last 12 bytes can be set to anything.

`bytes32`
`sender's`

tx.nonce

string

Yes

This is an incrementing nonce, can be obtained using theNoncesquery.

[Nonces](/developer-resources/api/gateway/queries/nonces)

signature

string

Yes

Signed transaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/link-signer#signing)

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier of the primary subaccount to add a signer to.

`sender`
`bytes32`

signer: abytes32sent as a hex string; includes the address (first 20 bytes) that'll be used as thesender'ssigner.

`signer`
`bytes32`
`sender's`

Notes:

- the last 12 bytes of thesignerfield do not matter and can be set to anything.

the last 12 bytes of thesignerfield do not matter and can be set to anything.

`signer`
- setsignerto the zero address to revoke current signer on the providedsender.

setsignerto the zero address to revoke current signer on the providedsender.

`signer`
`sender`

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

[PreviousBurn NLP](/developer-resources/api/gateway/executes/burn-nlp)
[NextQueries](/developer-resources/api/gateway/queries)

Last updated23 days ago