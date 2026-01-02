---
url: https://docs.nado.xyz/developer-resources/api/definitions-formulas
title: Definitions / Formulas
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Definitions / Formulas

Useful definitions and formulas to better understand Nado API.

## Definitions

### Unsettled USDT0

Perp balances have two main components:

- amount

amount

`amount`
- v_quote_balance

v_quote_balance

`v_quote_balance`

When you buy a perp,amountincrements andv_quote_balancedecrements, and vice versa for selling.

`amount`
`v_quote_balance`

Settlement is the process of converting fromv_quote_balanceinto actual USDT0 balance. This happens mostly on position close, but may happen on extremely negative PNL positions when we need to pay out positive PNL positions.

The amount that is transferred betweenv_quote_balancein the perp and your USDT0 balance is an amount that results inamount * oracle_price + v_quote_balance == 0. Unsettled USDT0 is the total amount that would be transferred betweenv_quote_balanceand your USDT0 balance summed across all perps.

`v_quote_balance`
`amount * oracle_price + v_quote_balance == 0`
`v_quote_balance`

### Unsettled PNL

Note:Technically, there is no such concept as "Unsettled PNL" in our system. However, the UI displays "Unsettled PnL" in some places (e.g., in the USDT0 Balance section) for user clarity.

What the UI actually shows:When you see "Unsettled PnL" in the UI, it refers toUnsettled USDT0(see above) - the total unsettled quote balance across all perp positions.

For developers:Always useUnsettled USDT0when referring to this value programmatically. It represents the sum ofamount × oracle_price + v_quote_balanceacross all perp positions, which is the amount that would be settled into your USDT0 balance.

`amount × oracle_price + v_quote_balance`

### Unrealized PNL

Refers to the estimated gains or losses of a current position based on the difference between the average entry price and the current oracle price.

## Formulas

### Unrealized PNL

Using theindexer's events query, your unrealized PNL at the end of some event is given by:

[indexer's events query](/developer-resources/api/archive-indexer/events)

### Total PNL

Your total PNL betweenevent1andevent2, assumingevent1is afterevent2- is given by:

`event1`
`event2`
`event1`
`event2`

Notes:

- You can use 0 for the second term for the PNL to compute since the beginning of time.

You can use 0 for the second term for the PNL to compute since the beginning of time.

- For spots, we will count deposits and withdraws towards your PNL. i.e. if you deposit BTC, for PNL tracking purposes it is counted as a BTC long at the oracle price.

For spots, we will count deposits and withdraws towards your PNL. i.e. if you deposit BTC, for PNL tracking purposes it is counted as a BTC long at the oracle price.

[PreviousIntegrate via Smart Contracts](/developer-resources/api/integrate-via-smart-contracts)
[NextAPI Changelog](/developer-resources/api/api-changelog)

Last updated1 month ago