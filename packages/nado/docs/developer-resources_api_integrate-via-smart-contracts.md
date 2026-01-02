---
url: https://docs.nado.xyz/developer-resources/api/integrate-via-smart-contracts
title: Integrate via Smart Contracts
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Integrate via Smart Contracts

Integrating with Nado via a Smart Contract

Smart contracts can use theLinkSignertransaction type (seeLink Signer) to perform the following:

`LinkSigner`
[Link Signer](/developer-resources/api/gateway/executes/link-signer)
- Deposit into Nado.

Deposit into Nado.

- LinkSigner an externally owned account (EOA).

LinkSigner an externally owned account (EOA).

[EOA](https://ethereum.org/en/developers/docs/accounts/#externally-owned-accounts-and-key-pairs)
- Have the externally owned account trade using the smart contract's assets on Nado.

Have the externally owned account trade using the smart contract's assets on Nado.

## Setup: Depositing into Nado + Linking an EOA

- Deposits are always on-chain, as such, users can simply have their smart contract calldepositCollateralon ourEndpointcontract (seeContractsfor addresses).

Deposits are always on-chain, as such, users can simply have their smart contract calldepositCollateralon ourEndpointcontract (seeContractsfor addresses).

`depositCollateral`
`Endpoint`
[Contracts](https://github.com/nadohq/nado-docs/blob/main/docs/developer-resources/contracts.md)
- The contract needs to have 1 USDT0 available to pay for slow-mode fee and approve the endpoint contract, assemble the bytes for a slow mode linked signer transaction, and submit it viasubmitSlowModeTransaction.

The contract needs to have 1 USDT0 available to pay for slow-mode fee and approve the endpoint contract, assemble the bytes for a slow mode linked signer transaction, and submit it viasubmitSlowModeTransaction.

[submitSlowModeTransaction](https://github.com/nadohq/nado-contracts/blob/main/core/contracts/Endpoint.sol)

You can find the requisite parsing logic in theEndpointcontract.

[Endpoint](https://github.com/nadohq/nado-contracts/blob/main/core/contracts/Endpoint.sol)

### Example

```
struct LinkSigner {
    bytes32 sender;
    bytes32 signer;
    uint64 nonce;
}

function linkNadoSigner(
        address nadoEndpoint,
        address externalAccount,
        address usdt0Address
    ) external {
    // 1. a slow mode fee of 1 USDT0 needs to be avaliable and approved
    ERC20 usdt0Token =  ERC20(usdt0Address);
    
    // NOTE: should double check the USDT0 decimals in the corresponding chain.
    // e.g: it's 1e6 on arbitrum, whereas it's 1e18 on blast, etc.
    uint256 SLOW_MODE_FEE = 1e6;
    usdt0Token.transferFrom(msg.sender, address(this), SLOW_MODE_FEE);
    usdt0Token.approve(nadoEndpoint, SLOW_MODE_FEE);
    
    // 2. assamble the link signer slow mode transaction
    bytes12 defaultSubaccountName = bytes12(abi.encodePacked("default"));
    bytes32 contractSubaccount = bytes32(
        abi.encodePacked(uint160(address(this)), defaultSubaccountName)
    );
    bytes32 externalSubaccount = bytes32(
        uint256(uint160(externalAccount)) << 96
    );
    LinkSigner memory linkSigner = LinkSigner(
        contractSubaccount,
        externalSubaccount,
        IEndpoint(nadoEndpoint).getNonce(contractSubaccount)
    );
    bytes memory txs = abi.encodePacked(
        uint8(13),
        abi.encode(linkSigner)
    );
    
    // 3. submit slow mode transaction
    IEndpoint(nadoEndpoint).submitSlowModeTransaction(txs);
}
```

Once the transaction is confirmed, it may take a few seconds for it to make its way into the Nado offchain sequencer. Afterwards, you can sign transactions that have sendercontractSubaccountusingexternalSubaccount, and they will be accepted by the sequencer and the blockchain.

`contractSubaccount`
`externalSubaccount`
[PreviousWithdrawing (on-chain)](/developer-resources/api/withdrawing-on-chain)
[NextDefinitions / Formulas](/developer-resources/api/definitions-formulas)

Last updated14 days ago