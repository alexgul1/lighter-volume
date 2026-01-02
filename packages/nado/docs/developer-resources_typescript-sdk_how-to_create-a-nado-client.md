---
url: https://docs.nado.xyz/developer-resources/typescript-sdk/how-to/create-a-nado-client
title: Create a Nado client
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📘TypeScript SDK
[📘TypeScript SDK](/developer-resources/typescript-sdk)
- How To
[How To](/developer-resources/typescript-sdk/how-to)

# Create a Nado client

## TheNadoClientObject

`NadoClient`

To start using the SDK, you need an initializedNadoClientfrom theclientpackage. TheNadoClientis the main entrypoint to common APIs.

`NadoClient`
`client`
`NadoClient`

## Create aNadoClientobject

`NadoClient`

TheNadoClientclass is rarely instantiated directly. Instead, call thecreateNadoClientfunction from theclientpackage and provide the relevant parameters.

`NadoClient`
`createNadoClient`
`client`

### Import the dependencies

```
import { createNadoClient } from '@nado-protocol/client';
import { createPublicClient, createWalletClient, http } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { inkSepolia } from 'viem/chains';
```

### Create aWalletClientandPublicClient

`WalletClient`
`PublicClient`

TheWalletClientis optional and required only for write operations

`WalletClient`

```
const walletClient = createWalletClient({
  account: privateKeyToAccount('0x...'),
  chain: inkSepolia,
  transport: http(),
});

const publicClient = createPublicClient({
  chain: inkSepolia,
  transport: http(),
});

```

### CallcreateNadoClient

`createNadoClient`

The first argument is theChainEnvassociated with the client. Each client can talk to one chain that Nado is deployed on. For example, useinkTestnetto connect to Nado's instance on Ink Sepolia.

`ChainEnv`
`inkTestnet`

## Full example

Run the script, this example usests-node:

`ts-node`

If no errors are thrown, you're good to go!

[PreviousHow To](/developer-resources/typescript-sdk/how-to)
[NextUseful Common Functions](/developer-resources/typescript-sdk/how-to/useful-common-functions)

Last updated1 month ago