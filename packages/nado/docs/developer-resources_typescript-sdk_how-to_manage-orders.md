---
url: https://docs.nado.xyz/developer-resources/typescript-sdk/how-to/manage-orders
title: Manage Orders
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📘TypeScript SDK
[📘TypeScript SDK](/developer-resources/typescript-sdk)
- How To
[How To](/developer-resources/typescript-sdk/how-to)

# Manage Orders

This guide shows you how to:

- Create an order.

Create an order.

- Place an order.

Place an order.

- Cancel an order.

Cancel an order.

- Query orders by subaccount.

Query orders by subaccount.

If you inspect the underlying types for these transactions, you'll notice that anoncefield is required. This is a unique integer in ascending order. Our off-chain engine has anoncequery to return the latest nonce for a given subaccount. All this is abstracted away within the SDK, so you do not need to manually use this query.

`nonce`
`nonce`

## Import the functions

```
import { getNadoClient, prettyPrintJson } from "./common";
import { nowInSeconds, toFixedPoint, packOrderAppendix } from "@nado-protocol/shared";
```

## Scaffold Your Subaccount

To place orders, we need a subaccount with funds. We need to perform thedeposit fundsstep as before, this time with 1000 USDT0.

[deposit funds](/developer-resources/typescript-sdk/how-to/deposit-funds)

```
const nadoClient = getNadoClient();
const { walletClient, publicClient } = nadoClient.context;

const address = walletClient!.account.address;
const subaccountName = 'default';
const depositAmount = toFixedPoint(1000, 6);

const mintTxHash = await nadoClient.spot._mintMockERC20({
  amount: depositAmount,
  productId: 0,
});
await publicClient.waitForTransactionReceipt({
  hash: mintTxHash,
});

const approveTxHash = await nadoClient.spot.approveAllowance({
  amount: depositAmount,
  productId: 0,
});
await publicClient.waitForTransactionReceipt({
  hash: approveTxHash,
});

const depositTxHash = await nadoClient.spot.deposit({
  subaccountName: 'default',
  amount: depositAmount,
  productId: 0,
});
await publicClient.waitForTransactionReceipt({
  hash: depositTxHash,
});

await new Promise((resolve) => setTimeout(resolve, 10000));
```

## Create an order

Placing an order requires a number of parameters, represented by thePlaceOrderParams['order']type.

`PlaceOrderParams['order']`

In the example below:

- The orderappendixindicates order execution type and other flags. Please refer toOrder Appendixfor more details.

The orderappendixindicates order execution type and other flags. Please refer toOrder Appendixfor more details.

`appendix`
[Order Appendix](/developer-resources/api/order-appendix)
- The orderexpirationtime is given by calling thenowInSecondsfunction from theutilspackage and adding 60 seconds. This means the order will expire 60 seconds from now.

The orderexpirationtime is given by calling thenowInSecondsfunction from theutilspackage and adding 60 seconds. This means the order will expire 60 seconds from now.

`expiration`
`nowInSeconds`
`utils`
- Thepricefield is set at80000- a low value (at the time of writing) to prevent execution. This enables us to cancel the order later on without it being instantly filled. Please adjust this price accordingly.

Thepricefield is set at80000- a low value (at the time of writing) to prevent execution. This enables us to cancel the order later on without it being instantly filled. Please adjust this price accordingly.

`price`
`80000`
- Theamountfield is set at10**16- this is the amount to buy/sell. A positive value is to buy, negative is to sell.Amount is normalized to 18 decimal places, which is whattoFixedPointdoes by default.NOTE: Min limit order size forBTCis10**16and forETHis10**17. Orders below these sizes will fail to be placed.

Theamountfield is set at10**16- this is the amount to buy/sell. A positive value is to buy, negative is to sell.

`amount`
`10**16`
- Amount is normalized to 18 decimal places, which is whattoFixedPointdoes by default.

Amount is normalized to 18 decimal places, which is whattoFixedPointdoes by default.

`toFixedPoint`
- NOTE: Min limit order size forBTCis10**16and forETHis10**17. Orders below these sizes will fail to be placed.

NOTE: Min limit order size forBTCis10**16and forETHis10**17. Orders below these sizes will fail to be placed.

`BTC`
`10**16`
`ETH`
`10**17`

## Place the order

Use the order parameters to place the order with theplaceOrderfunction.

`placeOrder`

## Alternative order placement

Alternatively, you can manually usepayloadBuilderto manually generate the place order payload. This may be useful in cases where you want to build thetxseparately from sending the execute API call.

`payloadBuilder`
`tx`

## Order digest

You can optionally generate the order digest, which can then be used to further manage the order e.g: cancelling the order. The order digest is also returned upon executing theplaceOrdertransaction.

`placeOrder`

## Query orders on the subaccount

Now we can query the subaccount for open orders with thegetOpenSubaccountOrdersfunction.

`getOpenSubaccountOrders`

## Cancel order

Cancel the order using the digest of the placed order. You can cancel multiple orders at once.

### Query Orders to Verify Cancellation

Runquery orders on the subaccountagain to make sure the cancellation was successful.

[query orders on the subaccount](/developer-resources/typescript-sdk/how-to/manage-orders#query-orders-on-the-subaccount)

## Clean up

Finally, clean up by withdrawing the same amount as you have deposited, minus the 1 USDT0 withdrawal fee.

## Full example

[PreviousWithdraw Funds](/developer-resources/typescript-sdk/how-to/withdraw-funds)

Last updated1 month ago