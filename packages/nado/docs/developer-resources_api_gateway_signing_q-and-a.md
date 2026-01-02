---
url: https://docs.nado.xyz/developer-resources/api/gateway/signing/q-and-a
title: Q&A
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Signing
[Signing](/developer-resources/api/gateway/signing)

# Q&A

Common signing issues & questions

### Q:What is Nado's EIP712 domain?

```
{
    name: 'Nado',
    version: '0.0.1',
    chainId: chainId,
    verifyingContract: contractAddress
}
```

Seesigningfor more details.

[signing](/developer-resources/api/gateway/signing#domain)

### Q: How can i retrieve the verifying contracts to use?

- Via thecontractsquery for all executes except place orders.

Via thecontractsquery for all executes except place orders.

[contracts](/developer-resources/api/gateway/queries/contracts)

### Q: Which contract should I use for each execute?

- For place orders: must be computed asaddress(productId). For example, the verify contract of product18is0x0000000000000000000000000000000000000012.

For place orders: must be computed asaddress(productId). For example, the verify contract of product18is0x0000000000000000000000000000000000000012.

`address(productId)`
`18`
`0x0000000000000000000000000000000000000012`
- For everything else: use the endpoint contract from the contracts query.

For everything else: use the endpoint contract from the contracts query.

See thecontractsquery for more details.

[contracts](/developer-resources/api/gateway/queries/contracts#response)

### Q: I am running into signature errors, how to fix?

Signature errors can arise for several reasons:

- An invalid struct: confirm you are signing the correct struct. See theSigningpage to verify the struct of each execute request.

An invalid struct: confirm you are signing the correct struct. See theSigningpage to verify the struct of each execute request.

[Signing](/developer-resources/api/gateway/signing)
- An invalid chain id: confirm you have the correct chain id for the network you are on.

An invalid chain id: confirm you have the correct chain id for the network you are on.

- An invalid verifying contract: confirm you have the correct verifying contract address for the network and execute you are signing. i.e: confirm you are using the correct orderbook address for place orders and endpoint address for everything else.

An invalid verifying contract: confirm you have the correct verifying contract address for the network and execute you are signing. i.e: confirm you are using the correct orderbook address for place orders and endpoint address for everything else.

### Q: Is any other signing standard supported?

No, onlyEIP712.

[EIP712](https://eips.ethereum.org/EIPS/eip-712)

### Q: Are there any examples you can provide?

Seeexamples.

[examples](/developer-resources/api/gateway/signing/examples)

### Q: What is the PrimaryType of execute X?

All primary types are listed in oursigningpage.

[signing](/developer-resources/api/gateway/signing)
[PreviousExamples](/developer-resources/api/gateway/signing/examples)
[NextSubscriptions](/developer-resources/api/subscriptions)

Last updated1 month ago