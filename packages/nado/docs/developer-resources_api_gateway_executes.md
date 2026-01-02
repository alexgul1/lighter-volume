---
url: https://docs.nado.xyz/developer-resources/api/gateway/executes
title: Executes
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)

# Executes

Nado Executes - Websocket and REST API

## Overview

All executes go through the following endpoint; the exact details of the execution are specified by the JSON payload.

- Websocket:WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

Websocket:WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`
- REST:POST [GATEWAY_REST_ENDPOINT]/execute

REST:POST [GATEWAY_REST_ENDPOINT]/execute

`POST [GATEWAY_REST_ENDPOINT]/execute`

### Signing

All executes are signed usingEIP712. Each execute request contains:

[EIP712](https://eips.ethereum.org/EIPS/eip-712)
- A piece of structured data that includes the sender address

A piece of structured data that includes the sender address

- A signature of the hash of that structured data, signed by the sender

A signature of the hash of that structured data, signed by the sender

You can check the SDK for some examples of how to generate these signatures.

See more info in thesigningpage.

[signing](/developer-resources/api/gateway/signing)

### Sender Field Structure

The sender field is a soliditybytes32. There are two components:

`bytes32`
- anaddressthat is abytes20

anaddressthat is abytes20

`address`
`bytes20`
- a subaccount identifier that is abytes12

a subaccount identifier that is abytes12

`bytes12`

For example, if your address was0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43, and you wanted to use the default subaccount identifier (i.e: the worddefault) you can setsenderto0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c4364656661756c740000000000, which sets the subaccount identifier to64656661756c740000000000.

`0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43`
`default`
`sender`
`0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c4364656661756c740000000000`
`64656661756c740000000000`

### Amounts

ForDepositCollateralandWithdrawCollateral, the amount specifies the physical token amount that you want to receive.i.e.if USDT0 has 6 decimals, and you want to deposit or withdraw 1 USDT0, you specifyamount = 1e6.

`DepositCollateral`
`WithdrawCollateral`
`i.e.`
`amount = 1e6`

For all other transactions, amount is normalized to 18 decimals, so1e18== one unit of the underlying asset. For example, if you want to buy 1 wETH, regardless of the amount of decimals the wETH contract has on chain, you specify1e18in the amount field of the order.

`1e18`
`1e18`

## API Response

AllExecutemessages return the following information:

`Execute`

#### Success

#### Failure

[PreviousGateway](/developer-resources/api/gateway)
[NextPlace Order](/developer-resources/api/gateway/executes/place-order)

Last updated1 month ago