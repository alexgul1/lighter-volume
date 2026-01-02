---
url: https://docs.nado.xyz/developer-resources/api/gateway/signing
title: Signing
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)

# Signing

Signing Nado executes

All executes are signed usingEIP712. Each execute request contains:

[EIP712](https://eips.ethereum.org/EIPS/eip-712)
- A piece of structured data that includes the sender address i.e: theprimaryTypethat needs to be signed.

A piece of structured data that includes the sender address i.e: theprimaryTypethat needs to be signed.

`primaryType`
- A signature of the hash of that structured data, signed by the sender.

A signature of the hash of that structured data, signed by the sender.

## Domain

The following is the domain required as part of the EIP712 structure:

```
{
    name: 'Nado',
    version: '0.0.1',
    chainId: chainId,
    verifyingContract: contractAddress
}
```

You can retrieve the corresponding chain id and verifying contract via thecontractsquery.

[contracts](/developer-resources/api/gateway/queries/contracts)

Note: make sure to use the correct verifying contract for each execute:

- For place order: should useaddress(producId)i.e: the 20 bytes hex representation of theproductIdfor the order. For example, the verify contract of product18is0x0000000000000000000000000000000000000012.

For place order: should useaddress(producId)i.e: the 20 bytes hex representation of theproductIdfor the order. For example, the verify contract of product18is0x0000000000000000000000000000000000000012.

`address(producId)`
`productId`
`18`
`0x0000000000000000000000000000000000000012`
- For everything else: should use the endpoint address.

For everything else: should use the endpoint address.

See more details in thecontractsquery page.

[contracts](/developer-resources/api/gateway/queries/contracts)

```
def gen_order_verifying_contract(product_id: int) -> str:
    """
    Generates the order verifying contract address based on the product ID.

    Args:
        product_id (int): The product ID for which to generate the verifying contract address.

    Returns:
        str: The generated order verifying contract address in hexadecimal format.
    """
    be_bytes = product_id.to_bytes(20, byteorder="big", signed=False)
    return "0x" + be_bytes.hex()
```

## EIP712 Types

See below the EIP712 type for each execute:

See more details in theSigningsection of each execute's page.

### Place Order

[Place Order](/developer-resources/api/gateway/executes/place-order)

Primary Type:Order

`Order`

Solidity struct that needs to be signed:

JSON representation:

### Cancel Orders

[Cancel Orders](/developer-resources/api/gateway/executes/cancel-orders)

Primary Type:Cancellation

`Cancellation`

Solidity struct that needs to be signed:

JSON representation:

### Cancel Product Orders

[Cancel Product Orders](/developer-resources/api/gateway/executes/cancel-product-orders)

Primary Type:CancellationProducts

`CancellationProducts`

Solidity struct that needs to be signed:

JSON representation:

### Withdraw Collateral

[Withdraw Collateral](/developer-resources/api/gateway/executes/withdraw-collateral)

Primary Type:WithdrawCollateral

`WithdrawCollateral`

Solidity struct that needs to be signed:

JSON representation:

### Liquidate Subaccount

[Liquidate Subaccount](/developer-resources/api/gateway/executes/liquidate-subaccount)

Primary Type:LiquidateSubaccount

`LiquidateSubaccount`

Solidity struct that needs to be signed:

JSON representation:

### Mint NLP

[Mint NLP](/developer-resources/api/gateway/executes/mint-nlp)

Primary Type:MintNlp

`MintNlp`

Solidity struct that needs to be signed:

JSON representation:

## Burn NLP

[Burn NLP](/developer-resources/api/gateway/executes/burn-nlp)

Primary Type:BurnNlp

`BurnNlp`

Solidity struct that needs to be signed:

JSON representation:

## Link Signer

[Link Signer](/developer-resources/api/gateway/executes/link-signer)

Primary Type:LinkSigner

`LinkSigner`

Solidity struct that needs to be signed:

JSON representation:

## List Trigger Orders

[List Trigger Orders](/developer-resources/api/trigger/queries/list-trigger-orders)

Primary Type:ListTriggerOrders

`ListTriggerOrders`

Solidity struct that needs to be signed:

JSON representation:

## Authenticate Subscription Streams

[Authenticate Subscription Streams](/developer-resources/api/subscriptions#authentication)

Primary Type:StreamAuthentication

`StreamAuthentication`

Struct that needs to be signed:

JSON representation:

[PreviousInsurance](/developer-resources/api/gateway/queries/insurance)
[NextExamples](/developer-resources/api/gateway/signing/examples)

Last updated8 days ago