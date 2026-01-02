---
url: https://docs.nado.xyz/fees-and-rebates
title: Fees & Rebates
---

# Fees & Rebates

Learn about Nado's scaling fee structure and maker rebates.

Nado's fee structure is designed for precision and fairness, rewarding liquidity providers while keeping costs lean for active traders.

The fee model follows a classic maker-taker structure across spot and perpetuals markets:

- Makers(limit orders adding liquidity): Earn rebates at higher tiers.

Makers(limit orders adding liquidity): Earn rebates at higher tiers.

- Takers(market orders removing liquidity): Pay a modest fee.

Takers(market orders removing liquidity): Pay a modest fee.

All fees are calculated in basis points (bps, or 0.01%) of the trade's notional value and settled instantly in USDT0 from your collateral.

Setting Nado apart from fixed-rate models, the volume-based scaling tiers update monthly to encourage deeper orderbooks and sustained activity. As your 30-day trading volume (maker + taker) climbs, taker fees decrease and maker rebates increase, creating a virtuous cycle of growing efficiency and participation.

Traders can monitor their current tier and monthly volume accrual directly in the account overview, with epochs resetting on the first of each UTC month.

Fee tiers compete with DeFi's most cost-effective venues, letting high-volume users pay as little as 1.5 bps as a taker – while elite makers are compensated to bolster the book.

### Trading Fees & Scaling Tiers

Nado's fee tiers scale based on your total trading volume (maker + taker) over the prior 30 days, aggregated across spot and perpetuals. Starting at accessible entry levels, they progress to elite rebates, encouraging consistent engagement without arbitrary barriers. Benefits include:

- Capital Efficiency: Lower fees free up more funds for positioning, amplifying returns on scale.

Capital Efficiency: Lower fees free up more funds for positioning, amplifying returns on scale.

- Liquidity Incentives: Maker rebates (expressed as negative fees) directly reward orderbook depth, tightening spreads for all traders.

Liquidity Incentives: Maker rebates (expressed as negative fees) directly reward orderbook depth, tightening spreads for all traders.

- Transparency: Real-time tier visibility lets you strategize volume to unlock better rates, with no hidden multipliers.

Transparency: Real-time tier visibility lets you strategize volume to unlock better rates, with no hidden multipliers.

Fees apply per execution:

- For a partial fill, only the matched portion incurs fee charges.

For a partial fill, only the matched portion incurs fee charges.

- No fees are applied to deposits or non-trading actions like borrowing.

No fees are applied to deposits or non-trading actions like borrowing.

#### Minimum Fee for Takers

Taker orders are subject to a minimum fee based on each product's minimum size:

- Orders ≥ minimum size: Standard fee applies to the full notional value:orderSize × feeRate

Orders ≥ minimum size: Standard fee applies to the full notional value:orderSize × feeRate

`orderSize × feeRate`
- Orders < minimum size: Minimum fee applies:minSize × feeRate(effectively treating small orders as if they were minSize)

Orders < minimum size: Minimum fee applies:minSize × feeRate(effectively treating small orders as if they were minSize)

`minSize × feeRate`

The minimum size is measured innotional dollar value(USDT0), not the asset quantity itself. For example, if minSize is $100, you could trade 0.001 BTC at $100,000/BTC (= $100 notional) or 0.033 ETH at $3,000/ETH (= $100 notional).

While certain order types enforce a minimum order size, the minimum fee applies to ALL taker orders regardless of size. This ensures consistent fee collection even for order types that allow smaller sizes.

Example - Large order: Assume minSize = $100. A $50,000 taker order at 3.5 bps:

- Fee: $50,000 × 0.035% = $17.50 (standard calculation)

Fee: $50,000 × 0.035% = $17.50 (standard calculation)

Example - Small order: Assume minSize = $100. A $75 taker order at 3.5 bps:

- Fee: $100 × 0.035% = $0.035 (minimum fee applies, calculated as if the order was minSize)

Fee: $100 × 0.035% = $0.035 (minimum fee applies, calculated as if the order was minSize)

Maker orders do not have minimum fee requirements and are charged or receive rebates on the full notional value based on your fee tier (see fee table above).

#### Example: Impact of Fee Tiers on a Trade

Consider a $50,000 ETH perpetuals market order (taker) or limit order (maker) at ETH $3,000.

Entry Tier($0 volume): Taker pays 3.5 bps = $17.50 (0.035% × $50,000). Maker pays 1 bp = $5.00.

Mid-Tier($25M volume): Taker pays 3 bps = $15.00. Maker pays 0.5 bps = $2.50.

Elite Tier($5B+ volume): Taker pays 1.5 bps = $7.50. Maker receives rebate of 0.8 bps = -$4.00 (added to collateral).

The scaling dynamic rewards whales without alienating newcomers, as even base rates (3.5 bps taker) beat many other exchange venues fee models.

Maker rebates accrue instantly to your subaccount, boosting health and compounding on unified cross-margin.

### Sequencer & Network Fees

Nado's off-chain sequencer handles order matching for sub-15 ms speed, with on-chain settlement via Ink L2.

To cover onchain interactions without gas volatility, Nado charges flat, predictable fees in USDT0 (or equivalent asset for withdrawals) – cheaper than typical L2 costs.

- Deposits: 0 USDT0 (instant bridging from Ink).

Deposits: 0 USDT0 (instant bridging from Ink).

- Order Placement(Maker): 0 USDT0.

Order Placement(Maker): 0 USDT0.

- Order Placement(Taker): 0 USDT0 (bundled with trading fee).

Order Placement(Taker): 0 USDT0 (bundled with trading fee).

- Subaccount Transfers:Standard: 1 USDT0Isolated subaccounts: 0.1 USDT0 (when either sender or recipient is isolated)

Subaccount Transfers:

- Standard: 1 USDT0

Standard: 1 USDT0

- Isolated subaccounts: 0.1 USDT0 (when either sender or recipient is isolated)

Isolated subaccounts: 0.1 USDT0 (when either sender or recipient is isolated)

- Liquidations: 1 USDT0 (to the liquidator).

Liquidations: 1 USDT0 (to the liquidator).

- Withdrawals:USDT0: 1 USDT0wETH: 0.0006 wETHkBTC: 0.00004 kBTC

Withdrawals:

- USDT0: 1 USDT0

USDT0: 1 USDT0

- wETH: 0.0006 wETH

wETH: 0.0006 wETH

- kBTC: 0.00004 kBTC

kBTC: 0.00004 kBTC

Sequencer fees are exclusively applied upon successful execution of the corresponding action. Failed actions, such as an attempt at an under-collateralized withdrawal, incur no sequencer fee charge.

Nado submits orders on-chain to the Ink L2 in batches to optimize for gas efficiency. During instances of excessive network congestion and high gas costs on-chain, Nado withdrawals may queue longer than usual, typically settling within ~30 minutes maximum.

### Fast Withdrawals

Users can also select the option for "Fast Withdrawals" anytime for withdrawal priority, which incurs an extra USDT0 charge, calculated as follows:

For BTC, the fee calculation is:

With tiered scaling and minimal overhead, Nado's fee model turns every fill into forward momentum – precise, scalable, and built for the long-haul.

[PreviousOracles](/oracles)
[NextFunding Rates](/funding-rates)

Last updated20 days ago