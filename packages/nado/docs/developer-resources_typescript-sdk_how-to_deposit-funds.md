---
url: https://docs.nado.xyz/developer-resources/typescript-sdk/how-to/deposit-funds
title: Deposit Funds
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📘TypeScript SDK
[📘TypeScript SDK](/developer-resources/typescript-sdk)
- How To
[How To](/developer-resources/typescript-sdk/how-to)

# Deposit Funds

## Import the functions

We'll use a few of thecommon functions, assuming that they are in acommon.tsfile. The withdraw step requires a nonce as the transaction is executed against the off-chain engine.

[common functions](/developer-resources/typescript-sdk/how-to/useful-common-functions)
`common.ts`

```
import { toFixedPoint } from '@nado-protocol/shared';
// Change the import source as needed
import { getNadoClient, prettyPrintJson } from './common';
```

## Mint a mock ERC20 token for testing

Grab a client object and mint mock tokens for the relevant product. This isonlyavailable on testnets for obvious reasons.

Minting is on-chain, so we wait for the transaction confirmation for chain state to propagate.

```
const nadoClient = await getNadoClient();
const { walletClient, publicClient } = nadoClient.context

// If you have access to `walletClient`, you can call `walletClient.account.address`
// directly instead of reaching into `nadoClient.context`
const address = walletClient!.account.address;
const subaccountName = 'default';
// 10 USDT0 (6 decimals)
const depositAmount = toFixedPoint(10, 6);

const mintTxHash = await nadoClient.spot._mintMockERC20({
  amount: depositAmount,
  productId: 0,
});

await publicClient.waitForTransactionReceipt({
  hash: mintTxHash,
});

```

## Make a deposit

First, callapproveAllowanceto approve the deposit amount.

`approveAllowance`

This is also an on-chain transaction with a confirmation hash.

Now we can deposit the tokens. This transaction is on-chain.

Subaccounts

- A subaccount is anindependenttrading account within Nado, allowing traders to manage risk across independent subaccounts

A subaccount is anindependenttrading account within Nado, allowing traders to manage risk across independent subaccounts

- Subaccounts are associated by a stringname(max 12 char.) and the owner wallet address

Subaccounts are associated by a stringname(max 12 char.) and the owner wallet address

`name`

After this, we inject a short delay while the offchain sequencer picks up the transaction and credits the account.

## Query Subaccount balance

Now, call thegetSubaccountEngineSummaryfunction to retrieve an overview of your subaccount, including balances.

`getSubaccountEngineSummary`

You should see that your balance associated withproductIdof0now reflects your deposit amount.

`productId`
`0`

## Full example

[PreviousQuery Markets & Products](/developer-resources/typescript-sdk/how-to/query-markets-and-products)
[NextWithdraw Funds](/developer-resources/typescript-sdk/how-to/withdraw-funds)

Last updated1 month ago