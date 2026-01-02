---
url: https://docs.nado.xyz/developer-resources/typescript-sdk/how-to/useful-common-functions
title: Useful Common Functions
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📘TypeScript SDK
[📘TypeScript SDK](/developer-resources/typescript-sdk)
- How To
[How To](/developer-resources/typescript-sdk/how-to)

# Useful Common Functions

These are some utility functions used throughout the guide. You may want to include them in your project.

- AgetNadoClientfunction that returns a ready-made client object connected to Ink Sepolia.

AgetNadoClientfunction that returns a ready-made client object connected to Ink Sepolia.

`getNadoClient`
- AprettyPrintJsonfunction that logs readable JSON.

AprettyPrintJsonfunction that logs readable JSON.

`prettyPrintJson`

Note

- Make sure your account has funds for gas on the relevant network.

Make sure your account has funds for gas on the relevant network.

- Make sure to replace your private key of choice in the functiongetNadoClientbelow

Make sure to replace your private key of choice in the functiongetNadoClientbelow

`getNadoClient`

```
import { createNadoClient } from '@nado-protocol/client';
import { toPrintableObject } from '@nado-protocol/shared';
import { createPublicClient, createWalletClient, http } from 'viem';
import { privateKeyToAccount } from 'viem/accounts';
import { inkSepolia } from 'viem/chains';

/**
 * Creates a Nado client for example scripts
 */
export function getNadoClient() {
  const walletClient = createWalletClient({
    account: privateKeyToAccount('0x...'),
    chain: inkSepolia,
    transport: http(),
  });

  const publicClient = createPublicClient({
    chain: inkSepolia,
    transport: http(),
  });

  return createNadoClient('inkTestnet', {
    walletClient,
    publicClient,
  });
}

/**
 * Util for pretty printing JSON
 */
export function prettyPrintJson(label: string, json: unknown) {
  console.log(label);
  console.log(JSON.stringify(toPrintableObject(json), null, 2));
}
```

[PreviousCreate a Nado client](/developer-resources/typescript-sdk/how-to/create-a-nado-client)
[NextQuery Markets & Products](/developer-resources/typescript-sdk/how-to/query-markets-and-products)

Last updated1 month ago