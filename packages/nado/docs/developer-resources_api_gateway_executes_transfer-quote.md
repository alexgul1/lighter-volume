---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes/transfer-quote
title: Transfer Quote
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Executes
[Executes](/developer-resources/api/gateway/executes)

# Transfer Quote

Transfer USDT0 between subaccounts under the same wallet.

## Fees

Transfers between subaccounts incur a network fee:

- Standard transfers: 1 USDT0

Standard transfers: 1 USDT0

- Isolated subaccount transfers: 0.1 USDT0 (when either sender or recipient is an isolated subaccount)

Isolated subaccount transfers: 0.1 USDT0 (when either sender or recipient is an isolated subaccount)

The fee is automatically deducted from the sender's balance.

## Rate limits

- 60 transfer quotes/min or 10 every 10 seconds per wallet. (weight=10)

60 transfer quotes/min or 10 every 10 seconds per wallet. (weight=10)

- A max of 5 transfer quotes to new recipients (subaccounts) every 24hrs.Note: Transferring quote to a subaccount that doesn't exist, creates the subaccount.

A max of 5 transfer quotes to new recipients (subaccounts) every 24hrs.

- Note: Transferring quote to a subaccount that doesn't exist, creates the subaccount.

Note: Transferring quote to a subaccount that doesn't exist, creates the subaccount.

See more details inAPI Rate limits.

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Connect

WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Message

```

{
  "transfer_quote": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "recipient": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743100000000000000",
      "amount": "10000000000000000000",
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
  "transfer_quote": {
    "tx": {
      "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
      "recipient": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743100000000000000",
      "amount": "10000000000000000000",
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

Transfer Quote transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/gateway/executes/transfer-quote#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.recipient

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the quote recipient.

tx.amount

string

Yes

The amount of USDT0 to transfer, denominated inx18. Transfr amount must be>= 5 USDT0. SeeSigningsection for more details.

`x18`
`>= 5 USDT0`
[Signing](/developer-resources/api/gateway/executes/transfer-quote#signing)

tx.nonce

string

Yes

This is an incrementing nonce, can be obtained using theNoncesquery.

[Nonces](/developer-resources/api/gateway/queries/nonces)

signature

string

Yes

Hex string representing hash of thesignedtransaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/gateway/executes/transfer-quote#signing)

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier.

`sender`
`bytes32`

recipient: abytes32sent as a hex string; includes the address and the subaccount identifier.

`recipient`
`bytes32`

amount: the amount of quote to transfer, sent as anx18string.

`amount`
`x18`

Notes:

- If you are transferring5 USDT0, must specify5000000000000000000i.e 5 USDT0 * 1e18.

If you are transferring5 USDT0, must specify5000000000000000000i.e 5 USDT0 * 1e18.

`5 USDT0`
`5000000000000000000`
- Transfer amount should be>= 5 USDT0.

Transfer amount should be>= 5 USDT0.

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

[PreviousWithdraw Collateral](/developer-resources/api/gateway/executes/withdraw-collateral)
[NextLiquidate Subaccount](/developer-resources/api/gateway/executes/liquidate-subaccount)

Last updated23 days ago