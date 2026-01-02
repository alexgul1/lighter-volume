---
url: https://docs.nado.xyz/developer-resources/api/api-changelog
title: API Changelog
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# API Changelog

This document tracks all changes to the Nado API.

Archive Indexer: Orders & Matches fields

- Addedclosed_amount(x18) andrealized_pnl(x18) to archive indexer responses for bothordersandmatches.

Addedclosed_amount(x18) andrealized_pnl(x18) to archive indexer responses for bothordersandmatches.

`closed_amount`
`realized_pnl`
[orders](/developer-resources/api/archive-indexer/orders)
[matches](/developer-resources/api/archive-indexer/matches)

Risk System Updates

Spread Weight Caps

- Introduced upper bounds for spread weights to manage risk at extreme leverage levels:initial_spread_weight: Maximum0.99maintenance_spread_weight: Maximum0.994

Introduced upper bounds for spread weights to manage risk at extreme leverage levels:

- initial_spread_weight: Maximum0.99

initial_spread_weight: Maximum0.99

`initial_spread_weight`
- maintenance_spread_weight: Maximum0.994

maintenance_spread_weight: Maximum0.994

`maintenance_spread_weight`
- Impact:Existing markets (≤20x leverage): No change in behaviorFuture high-leverage markets (30x+): Spread positions will have capped health benefitsPrevents extreme leverage abuse via spread positions

Impact:

- Existing markets (≤20x leverage): No change in behavior

Existing markets (≤20x leverage): No change in behavior

- Future high-leverage markets (30x+): Spread positions will have capped health benefits

Future high-leverage markets (30x+): Spread positions will have capped health benefits

- Prevents extreme leverage abuse via spread positions

Prevents extreme leverage abuse via spread positions

- Technical Details:Base spread weight calculated as:spread_weight = 1 - (1 - product_weight) / 5Final spread weight:min(spread_weight, cap)Cap applies during health calculations for spread positions

Technical Details:

- Base spread weight calculated as:spread_weight = 1 - (1 - product_weight) / 5

Base spread weight calculated as:spread_weight = 1 - (1 - product_weight) / 5

`spread_weight = 1 - (1 - product_weight) / 5`
- Final spread weight:min(spread_weight, cap)

Final spread weight:min(spread_weight, cap)

`min(spread_weight, cap)`
- Cap applies during health calculations for spread positions

Cap applies during health calculations for spread positions

Minimum Liquidation Penalties

- Introduced minimum distance requirements between oracle price and liquidation price:Non-spread liquidations: Minimum0.5%from oracle priceSpread liquidations: Minimum0.25%from oracle price

Introduced minimum distance requirements between oracle price and liquidation price:

- Non-spread liquidations: Minimum0.5%from oracle price

Non-spread liquidations: Minimum0.5%from oracle price

- Spread liquidations: Minimum0.25%from oracle price

Spread liquidations: Minimum0.25%from oracle price

- Impact:Ensures liquidators always have sufficient incentive to execute liquidationsPrevents unprofitable liquidation scenarios for low-volatility assetsParticularly important for high-leverage positions where natural penalties may be very small

Impact:

- Ensures liquidators always have sufficient incentive to execute liquidations

Ensures liquidators always have sufficient incentive to execute liquidations

- Prevents unprofitable liquidation scenarios for low-volatility assets

Prevents unprofitable liquidation scenarios for low-volatility assets

- Particularly important for high-leverage positions where natural penalties may be very small

Particularly important for high-leverage positions where natural penalties may be very small

- Technical Details:Non-spread longs:oracle_price × (1 - max((1 - maint_asset_weight) / 5, 0.005))Non-spread shorts:oracle_price × (1 + max((maint_liability_weight - 1) / 5, 0.005))Spread selling:spot_price × (1 - max((1 - perp_maint_asset_weight) / 10, 0.0025))Spread buying:spot_price × (1 + max((spot_maint_liability_weight - 1) / 10, 0.0025))

Technical Details:

- Non-spread longs:oracle_price × (1 - max((1 - maint_asset_weight) / 5, 0.005))

Non-spread longs:oracle_price × (1 - max((1 - maint_asset_weight) / 5, 0.005))

`oracle_price × (1 - max((1 - maint_asset_weight) / 5, 0.005))`
- Non-spread shorts:oracle_price × (1 + max((maint_liability_weight - 1) / 5, 0.005))

Non-spread shorts:oracle_price × (1 + max((maint_liability_weight - 1) / 5, 0.005))

`oracle_price × (1 + max((maint_liability_weight - 1) / 5, 0.005))`
- Spread selling:spot_price × (1 - max((1 - perp_maint_asset_weight) / 10, 0.0025))

Spread selling:spot_price × (1 - max((1 - perp_maint_asset_weight) / 10, 0.0025))

`spot_price × (1 - max((1 - perp_maint_asset_weight) / 10, 0.0025))`
- Spread buying:spot_price × (1 + max((spot_maint_liability_weight - 1) / 10, 0.0025))

Spread buying:spot_price × (1 + max((spot_maint_liability_weight - 1) / 10, 0.0025))

`spot_price × (1 + max((spot_maint_liability_weight - 1) / 10, 0.0025))`

API Response Changes

- No breaking changes to API response structure

No breaking changes to API response structure

- Health calculations and liquidation prices automatically reflect new risk parameters

Health calculations and liquidation prices automatically reflect new risk parameters

Documentation Updates

- SeeSubaccounts & Healthfor spread weight cap details

SeeSubaccounts & Healthfor spread weight cap details

[Subaccounts & Health](/subaccounts-and-health#spreads)
- SeeLiquidationsfor minimum liquidation penalty details

SeeLiquidationsfor minimum liquidation penalty details

[Liquidations](/liquidations#liquidation-price)

Query Enhancements

Pre-State Simulation for SubaccountInfo Query

- Addedpre_stateparameter toSubaccountInfoqueryType:string(accepts"true"or"false")When set to"true"along withtxns, returns apre_stateobject in the responsepre_statecontains the subaccount statebeforethe simulated transactions were appliedUseful for comparing before/after states when simulating tradespre_stateincludes:healths: Health information before transactionshealth_contributions: Per-product health contributions before transactionsspot_balances: Spot balances before transactionsperp_balances: Perpetual balances before transactions

Addedpre_stateparameter toSubaccountInfoquery

`pre_state`
`SubaccountInfo`
- Type:string(accepts"true"or"false")

Type:string(accepts"true"or"false")

`string`
`"true"`
`"false"`
- When set to"true"along withtxns, returns apre_stateobject in the response

When set to"true"along withtxns, returns apre_stateobject in the response

`"true"`
`txns`
`pre_state`
- pre_statecontains the subaccount statebeforethe simulated transactions were applied

pre_statecontains the subaccount statebeforethe simulated transactions were applied

`pre_state`
- Useful for comparing before/after states when simulating trades

Useful for comparing before/after states when simulating trades

- pre_stateincludes:healths: Health information before transactionshealth_contributions: Per-product health contributions before transactionsspot_balances: Spot balances before transactionsperp_balances: Perpetual balances before transactions

pre_stateincludes:

`pre_state`
- healths: Health information before transactions

healths: Health information before transactions

`healths`
- health_contributions: Per-product health contributions before transactions

health_contributions: Per-product health contributions before transactions

`health_contributions`
- spot_balances: Spot balances before transactions

spot_balances: Spot balances before transactions

`spot_balances`
- perp_balances: Perpetual balances before transactions

perp_balances: Perpetual balances before transactions

`perp_balances`

Use Cases:

- Position simulation and preview

Position simulation and preview

- Risk analysis for potential trades

Risk analysis for potential trades

- UI/UX for showing before/after comparisons

UI/UX for showing before/after comparisons

- Testing transaction impacts without on-chain execution

Testing transaction impacts without on-chain execution

Documentation:SeeSubaccount Info Queryfor detailed examples.

[Subaccount Info Query](/developer-resources/api/gateway/queries/subaccount-info#example-with-pre_state)

#### Core Changes

1. Removal of LP Functionality

- SubaccountInfono longer has:lp_balanceinspot_balancesandperp_balanceslp_stateinspot_productsandperp_productslp_spread_x18inbook_infoof bothspot_productsandperp_products

SubaccountInfono longer has:

`SubaccountInfo`
- lp_balanceinspot_balancesandperp_balances

lp_balanceinspot_balancesandperp_balances

`lp_balance`
`spot_balances`
`perp_balances`
- lp_stateinspot_productsandperp_products

lp_stateinspot_productsandperp_products

`lp_state`
`spot_products`
`perp_products`
- lp_spread_x18inbook_infoof bothspot_productsandperp_products

lp_spread_x18inbook_infoof bothspot_productsandperp_products

`lp_spread_x18`
`book_info`
`spot_products`
`perp_products`
- Historicaleventsno longer include:net_entry_lp_unrealizednet_entry_lp_cumulative

Historicaleventsno longer include:

`events`
- net_entry_lp_unrealized

net_entry_lp_unrealized

`net_entry_lp_unrealized`
- net_entry_lp_cumulative

net_entry_lp_cumulative

`net_entry_lp_cumulative`

2. Removal of Redundant Fields

- SubaccountInfono longer has:last_cumulative_multiplier_x18inbalanceofspot_balances

SubaccountInfono longer has:

`SubaccountInfo`
- last_cumulative_multiplier_x18inbalanceofspot_balances

last_cumulative_multiplier_x18inbalanceofspot_balances

`last_cumulative_multiplier_x18`
`balance`
`spot_balances`

3. Products Config Model Updates

- Added:withdraw_fee_x18andmin_deposit_rate_x18tospot_products.config

Added:withdraw_fee_x18andmin_deposit_rate_x18tospot_products.config

`withdraw_fee_x18`
`min_deposit_rate_x18`
`spot_products.config`

4. Products Risk Model Updates

- Added:price_x18to bothspot_products.riskandperp_products.risk

Added:price_x18to bothspot_products.riskandperp_products.risk

`price_x18`
`spot_products.risk`
`perp_products.risk`
- Removed:large_position_penalty_x18

Removed:large_position_penalty_x18

`large_position_penalty_x18`

5. Deposit Rate Query

- Removed:min_deposit_ratesquery

Removed:min_deposit_ratesquery

`min_deposit_rates`
- Usemin_deposit_rate_x18inspot_products.configinstead

Usemin_deposit_rate_x18inspot_products.configinstead

`min_deposit_rate_x18`
`spot_products.config`

#### Market Structure Changes

6. Removal of Virtual Books

- Contractsquery no longer returnsbook_addrs

Contractsquery no longer returnsbook_addrs

`Contracts`
`book_addrs`
- PlaceOrderverify contract is nowaddress(product_id)&#xNAN;Example: product18→0x0000000000000000000000000000000000000012

PlaceOrderverify contract is nowaddress(product_id)&#xNAN;Example: product18→0x0000000000000000000000000000000000000012

`PlaceOrder`
`address(product_id)`
`0x0000000000000000000000000000000000000012`

7. Minimum Size denomination

- min_sizeis nowUSDT0 denominated(not base denominated)min_size = 10→ minimum order size = 10 USDT0 (order_price * order_amount)

min_sizeis nowUSDT0 denominated(not base denominated)

`min_size`
- min_size = 10→ minimum order size = 10 USDT0 (order_price * order_amount)

min_size = 10→ minimum order size = 10 USDT0 (order_price * order_amount)

`min_size = 10`
`order_price * order_amount`
- size_incrementremainsbase denominatedExample: BTC withsize_increment = 0.0001andmin_size = 20:✅ Valid: 100,000 * 0.0002 = 20 USDT0❌ Invalid: 100,000 * 0.0001 = 10 USDT0❌ Invalid: 100,000 * 0.00025 (not multiple of 0.0001)

size_incrementremainsbase denominated

`size_increment`
- Example: BTC withsize_increment = 0.0001andmin_size = 20:✅ Valid: 100,000 * 0.0002 = 20 USDT0❌ Invalid: 100,000 * 0.0001 = 10 USDT0❌ Invalid: 100,000 * 0.00025 (not multiple of 0.0001)

Example: BTC withsize_increment = 0.0001andmin_size = 20:

`size_increment = 0.0001`
`min_size = 20`
- ✅ Valid: 100,000 * 0.0002 = 20 USDT0

✅ Valid: 100,000 * 0.0002 = 20 USDT0

- ❌ Invalid: 100,000 * 0.0001 = 10 USDT0

❌ Invalid: 100,000 * 0.0001 = 10 USDT0

- ❌ Invalid: 100,000 * 0.00025 (not multiple of 0.0001)

❌ Invalid: 100,000 * 0.00025 (not multiple of 0.0001)

#### Orders & Signing

8. Place Orders Execute

- Added:place_ordersexecute - place multiple orders in a single requestAccepts array of orders with same structure asplace_orderOptionalstop_on_failureparameter to stop processing remaining orders on first failureReturns array of results withdigest(if successful) orerror(if failed) for each orderRate limit weight calculated per order

Added:place_ordersexecute - place multiple orders in a single request

`place_orders`
- Accepts array of orders with same structure asplace_order

Accepts array of orders with same structure asplace_order

`place_order`
- Optionalstop_on_failureparameter to stop processing remaining orders on first failure

Optionalstop_on_failureparameter to stop processing remaining orders on first failure

`stop_on_failure`
- Returns array of results withdigest(if successful) orerror(if failed) for each order

Returns array of results withdigest(if successful) orerror(if failed) for each order

`digest`
`error`
- Rate limit weight calculated per order

Rate limit weight calculated per order

SeePlace Ordersfor details.

[Place Orders](/developer-resources/api/gateway/executes/place-orders)

9. EIP712OrderStruct Update

`Order`

```
struct Order {
    bytes32 sender;
    int128 priceX18;
    int128 amount;
    uint64 expiration;
    uint64 nonce;
    uint128 appendix;
}
```

- New field:appendix

New field:appendix

`appendix`
- All order flags (IOC, post only, reduce-only, triggers) moved intoappendix

All order flags (IOC, post only, reduce-only, triggers) moved intoappendix

`appendix`
- expirationis now strictly a timestamp

expirationis now strictly a timestamp

`expiration`
- appendixbitfield:

appendixbitfield:

`appendix`

```
| value   | reserved | trigger | reduce only | order type | isolated | version |
| 64 bits | 50 bits  | 2 bits  | 1 bit       | 2 bits     | 1 bit    | 8 bits  |
```

- Special encodings:trigger= 2 or 3 →valueencodes TWAP settings (times,slippage_x6)isolated = 1→valueencodes isolated margin

Special encodings:

- trigger= 2 or 3 →valueencodes TWAP settings (times,slippage_x6)

trigger= 2 or 3 →valueencodes TWAP settings (times,slippage_x6)

`trigger`
`value`
`times`
`slippage_x6`
- isolated = 1→valueencodes isolated margin

isolated = 1→valueencodes isolated margin

`isolated = 1`
`value`
- Constraints:Isolated orders cannot be TWAPTWAP orders must use IOC execution type

Constraints:

- Isolated orders cannot be TWAP

Isolated orders cannot be TWAP

- TWAP orders must use IOC execution type

TWAP orders must use IOC execution type

SeeOrder Appendix Docs.

[Order Appendix Docs](/developer-resources/api/order-appendix)

10. TWAP Order Execution

- Addedlist_twap_executionsquery to trigger service

Addedlist_twap_executionsquery to trigger service

`list_twap_executions`
- TWAP orders track individual execution status (pending, executed, failed, cancelled)

TWAP orders track individual execution status (pending, executed, failed, cancelled)

- TWAP execution statuses include execution time and engine response data

TWAP execution statuses include execution time and engine response data

11. Trigger Service Rate Limits

- Updated trigger order limits from 100 pending orders per subaccount to25 pending orders per product per subaccount

Updated trigger order limits from 100 pending orders per subaccount to25 pending orders per product per subaccount

`25 pending orders per product per subaccount`

12. EIP712 Domain Change

- Signing domain updated fromVertex→NadoSeeSigning Docs.

Signing domain updated fromVertex→NadoSeeSigning Docs.

`Vertex`
`Nado`
[Signing Docs](/developer-resources/api/gateway/signing)

#### Query Updates

13.max_order_size

`max_order_size`
- Added:isolatedparameter - when set totrue, calculates max order size for an isolated margin position. Defaults tofalse.

Added:isolatedparameter - when set totrue, calculates max order size for an isolated margin position. Defaults tofalse.

`isolated`
`true`
`false`

14.ordersQuery

`orders`
- Added:trigger_typesparameter - filter orders by trigger type(s)

Added:trigger_typesparameter - filter orders by trigger type(s)

`trigger_types`

15. Historical Events

- Added:quote_volume_cumulative- tracks cumulative trading volume for the subaccount in quote unitsAvailable in:eventsandsubaccount_snapshotsqueries

Added:quote_volume_cumulative- tracks cumulative trading volume for the subaccount in quote units

`quote_volume_cumulative`
- Available in:eventsandsubaccount_snapshotsqueries

Available in:eventsandsubaccount_snapshotsqueries

`events`
`subaccount_snapshots`

16.subaccount_snapshotsQuery

`subaccount_snapshots`
- Added:activeparameter - filter snapshots by position statustrue: returns only products withnon-zero balanceat the timestampfalse: returns products withevent historybefore the timestamp (default)

Added:activeparameter - filter snapshots by position status

`active`
- true: returns only products withnon-zero balanceat the timestamp

true: returns only products withnon-zero balanceat the timestamp

`true`
- false: returns products withevent historybefore the timestamp (default)

false: returns products withevent historybefore the timestamp (default)

`false`

17. Trigger Orders

- Added:place_atfield - timestamp when trigger order should be placed

Added:place_atfield - timestamp when trigger order should be placed

`place_at`

18. Removal ofsummaryQuery

`summary`
- Removed:summaryquery from indexer API

Removed:summaryquery from indexer API

`summary`
- Usesubaccount_snapshotsquery instead for historical subaccount data

Usesubaccount_snapshotsquery instead for historical subaccount data

`subaccount_snapshots`

19. Query Renaming

- Renamed:usdc_price→quote_pricequerySeeQuote Price

Renamed:usdc_price→quote_pricequery

`usdc_price`
`quote_price`
- SeeQuote Price

SeeQuote Price

[Quote Price](/developer-resources/api/archive-indexer/quote-price)

20. Multi-Subaccountevents,matches,orders

`events`
`matches`
`orders`
- The indexerevents,matches, andordersqueries now accept asubaccountsarray so you can fetch history for multiple subaccounts in a single request instead of fanning out per subaccount. Please note that the old single-subaccount version isno longer supported.

The indexerevents,matches, andordersqueries now accept asubaccountsarray so you can fetch history for multiple subaccounts in a single request instead of fanning out per subaccount. Please note that the old single-subaccount version isno longer supported.

`events`
`matches`
`orders`
`subaccounts`

#### Streams

SeeSubscriptions > Streamsfor more details

[Subscriptions > Streams](/developer-resources/api/subscriptions/streams)

21.OrderUpdate

`OrderUpdate`
- Can now subscribe across all products by settingproduct_id = null

Can now subscribe across all products by settingproduct_id = null

`product_id = null`
- product_idtype changed fromu32→Option<u32>

product_idtype changed fromu32→Option<u32>

`product_id`
`u32`
`Option<u32>`

22.Fill

`Fill`
- Added:fee,submission_idx, andappendix

Added:fee,submission_idx, andappendix

`fee`
`submission_idx`
`appendix`
- Can now subscribe across all products by settingproduct_id = null

Can now subscribe across all products by settingproduct_id = null

`product_id = null`

23.PositionChange

`PositionChange`
- Can now subscribe across all products by settingproduct_id = null

Can now subscribe across all products by settingproduct_id = null

`product_id = null`
- product_idtype changed fromu32→Option<u32>

product_idtype changed fromu32→Option<u32>

`product_id`
`u32`
`Option<u32>`
- Added:isolated- indicates whether the position change is for an isolated margin position

Added:isolated- indicates whether the position change is for an isolated margin position

`isolated`

24.FundingPayment

`FundingPayment`
- New stream:FundingPayment

New stream:FundingPayment

`FundingPayment`
- Param:product_id: u32

Param:product_id: u32

`product_id: u32`
- Emits hourly funding payment events

Emits hourly funding payment events

Request

```
{
  "method": "subscribe",
  "stream": {
    "type": "funding_payment",
    "product_id": 1
  },
  "id": 123
}
```

Response

```
{
  "type": "funding_payment",
  "timestamp": 1234567890000,
  "product_id": 1,
  "payment_amount": "1000000000000000000",
  "open_interest": "50000000000000000000",
  "cumulative_funding_long_x18": "100000000000000000",
  "cumulative_funding_short_x18": "-100000000000000000",
  "dt": 3600000
}
```

25.Liquidation

`Liquidation`
- New stream:Liquidation

New stream:Liquidation

`Liquidation`
- Param:product_idornull(all products)

Param:product_idornull(all products)

`product_id`
`null`
- Emits liquidation info (liquidator, liquidatee, amount, price)

Emits liquidation info (liquidator, liquidatee, amount, price)

Request

```
{
  "method": "subscribe",
  "stream": {
    "type": "liquidation",
    "product_id": 1
  },
  "id": 123
}
```

Response

```
{
  "type": "liquidation",
  "timestamp": "1234567890000",
  "product_ids": [1],
  "liquidator": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
  "liquidatee": "0x8b6fd3859f7065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
  "amount": "1000000000000000000",
  "price": "50000000000000000000"
}
```

26.LatestCandlestick

`LatestCandlestick`
- New stream:LatestCandlestick

New stream:LatestCandlestick

`LatestCandlestick`
- Params:product_id,granularity(seconds)

Params:product_id,granularity(seconds)

`product_id`
`granularity`
- Emits candlestick updates on every trade

Emits candlestick updates on every trade

Request

```
{
  "method": "subscribe",
  "stream": {
    "type": "latest_candlestick",
    "product_id": 1,
    "granularity": 60
  },
  "id": 123
}
```

Response

```
{
  "type": "latest_candlestick",
  "timestamp": 1234567890000,
  "product_id": 1,
  "granularity": 60,
  "open_x18": "50000000000000000000",
  "high_x18": "51000000000000000000",
  "low_x18": "49000000000000000000",
  "close_x18": "50500000000000000000",
  "volume": "1000000000000000000"
}
```

27.FundingRate

`FundingRate`
- New stream:FundingRate

New stream:FundingRate

`FundingRate`
- Param:product_idornull(all products)

Param:product_idornull(all products)

`product_id`
`null`
- Emits funding rate updates every 20 seconds

Emits funding rate updates every 20 seconds

- funding_rate_x18andupdate_timevalues are identical to those from theFunding Rateindexer endpoint

funding_rate_x18andupdate_timevalues are identical to those from theFunding Rateindexer endpoint

`funding_rate_x18`
`update_time`
[Funding Rate](/developer-resources/api/archive-indexer/funding-rate)

Request

```
{
  "method": "subscribe",
  "stream": {
    "type": "funding_rate",
    "product_id": 1
  },
  "id": 123
}
```

Subscribe to all products:

```
{
  "method": "subscribe",
  "stream": {
    "type": "funding_rate",
    "product_id": null
  },
  "id": 123
}
```

Response

```
{
  "type": "funding_rate",
  "timestamp": "1234567890123456789",
  "product_id": 1,
  "funding_rate_x18": "50000000000000000",
  "update_time": "1234567890"
}
```

[PreviousDefinitions / Formulas](/developer-resources/api/definitions-formulas)
[NextTypeScript SDK](/developer-resources/typescript-sdk)

Last updated13 days ago