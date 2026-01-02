---
url: https://docs.nado.xyz/developer-resources/api/withdrawing-on-chain
title: Withdrawing (on-chain)
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Withdrawing (on-chain)

Withdrawing collateral from Nado on-chain.

You can withdraw collateral from Nado directly on-chain, by submitting a slow-mode transaction via theEndpointcontract (seeContractsfor addresses).

`Endpoint`

Note:

- This is an alternative to withdrawing collateral via our off-chain sequencer. SeeWithdraw Collateralfor more details.

This is an alternative to withdrawing collateral via our off-chain sequencer. SeeWithdraw Collateralfor more details.

[Withdraw Collateral](/developer-resources/api/gateway/executes/withdraw-collateral)
- Slow mode transactions have a 1 USDT0 fee; as such, an approval of 1 USDT0 is required for the slow mode withdrawal to succeed.

Slow mode transactions have a 1 USDT0 fee; as such, an approval of 1 USDT0 is required for the slow mode withdrawal to succeed.

## Steps

- Assemble the bytes needed for a withdraw collateral transaction by encoding the following struct alongside the transaction type2:

Assemble the bytes needed for a withdraw collateral transaction by encoding the following struct alongside the transaction type2:

`2`

```
struct WithdrawCollateral {
    bytes32 sender;
    uint32 productId;
    uint128 amount;
    uint64 nonce;
}
```

- Submit the transaction viasubmitSlowModeTransactionon ourEndpointcontract.

Submit the transaction viasubmitSlowModeTransactionon ourEndpointcontract.

`submitSlowModeTransaction`
`Endpoint`

### Example

```
function withdrawNadoCollateral(address nadoEndpoint, bytes32 sender, uint32 productId, uint128 amount) internal {
    WithdrawCollateral memory withdrawal = new WithdrawCollateral(sender, productId, amount, 0);
    bytes memory tx = abi.encodePacked(2, abi.encode(withdrawal));
    IEndpoint(nadoEndpoint).submitSlowModeTransaction(tx);
}
```

Once the transaction is confirmed, it may take a few seconds for it to make its way into the Nado offchain sequencer and for the withdrawal to be processed.

[PreviousDepositing](/developer-resources/api/depositing)
[NextIntegrate via Smart Contracts](/developer-resources/api/integrate-via-smart-contracts)

Last updated1 month ago