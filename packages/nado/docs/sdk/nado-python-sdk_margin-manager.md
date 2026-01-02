---
url: https://nadohq.github.io/nado-python-sdk/margin-manager.html
---

# Margin Manager

The Margin Manager provides comprehensive margin calculations for your Nado Protocol subaccounts. It calculates health, margin usage, leverage, and position-level metrics to help you understand your account’s risk profile.

## Overview

The margin manager calculates:

- Health Metrics: Initial, maintenance, and unweighted health

Health Metrics: Initial, maintenance, and unweighted health

- Margin Usage: Percentage of margin being used (0-100%)

Margin Usage: Percentage of margin being used (0-100%)

- Position Metrics: Individual position details with health contributions

Position Metrics: Individual position details with health contributions

- Leverage: Overall account leverage

Leverage: Overall account leverage

- Available Funds: How much margin is available for new positions

Available Funds: How much margin is available for new positions

## Key Concepts

### Health Types

The system uses three levels of health/margin requirements:

Type

Purpose

Description

Initial

Open new positions

Strictest requirement. Uses*_weight_initialfields (e.g., 0.9 for 10x max leverage)

Maintenance

Avoid liquidation

Less strict. Uses*_weight_maintenancefields (e.g., 0.95 for 20x)

Unweighted

Raw asset value

No haircuts applied (weight = 1.0). Used as reference.

### Health Calculation

For each balance:

```python
health_contribution = amount × oracle_price × weight

```

Where weight depends on position direction:

- Long positions(amount ≥ 0): Uselong_weight_*

Long positions(amount ≥ 0): Uselong_weight_*

- Short positions(amount < 0): Useshort_weight_*

Short positions(amount < 0): Useshort_weight_*

For the entire subaccount:

```python
assets = sum of positive health contributions
liabilities = sum of negative health contributions (absolute value)
health = assets - liabilities

```

Liquidation occurs when maintenance health < 0.

### Margin Modes

**Cross Margin**
  Margin is shared across all positions. All balances contribute to a single health pool.margin_usage = (unweighted_health - initial_health) / unweighted_health

Margin is shared across all positions. All balances contribute to a single health pool.

```python
margin_usage = (unweighted_health - initial_health) / unweighted_health

```

**Isolated Margin**
  Dedicated margin per perp position. Only USDT can be used. Max 1 isolated position per market.net_margin = quote_amount + unsettled_pnl
leverage = notional_value / net_margin

Dedicated margin per perp position. Only USDT can be used. Max 1 isolated position per market.

```python
net_margin = quote_amount + unsettled_pnl
leverage = notional_value / net_margin

```

## Quick Start

### Basic Usage

```python
import time
from nado_protocol.client import create_nado_client, NadoClientMode
from nado_protocol.utils.margin_manager import MarginManager, print_account_summary

client = create_nado_client(NadoClientMode.TESTNET)

# Optionally override defaults (subaccount hex, timestamp, etc.)
manager = MarginManager.from_client(
    client,
    include_indexer_events=True,
    snapshot_timestamp=int(time.time()),
)

summary = manager.calculate_account_summary()
print_account_summary(summary)

```

If you skip the optional indexer request (include_indexer_events=False),CrossPositionMetrics.est_pnlremainsNoneand the printed summary displaysN/Afor Est. PnL.

Passingsnapshot_active_only=True(the default) ensures the indexer only returns
balances that are live at the requested timestamp, keeping the snapshot focused on
current positions.

### Manual setup (advanced)

If you need more control over the data-fetching steps, you can assemble the manager
yourself:

```python
import time
from nado_protocol.engine_client import EngineQueryClient, EngineClientOpts
from nado_protocol.indexer_client import IndexerQueryClient, IndexerClientOpts
from nado_protocol.indexer_client.types.query import IndexerAccountSnapshotsParams
from nado_protocol.utils.bytes32 import subaccount_to_hex
from nado_protocol.utils.margin_manager import MarginManager, print_account_summary

# Create read-only clients (no private key needed)
engine_client = EngineQueryClient(
    EngineClientOpts(url="https://gateway.test.nado.xyz/v1")
)
indexer_client = IndexerQueryClient(
    IndexerClientOpts(url="https://archive.test.nado.xyz/v1")
)

# Get subaccount data
wallet_address = "0x1234..."
subaccount = subaccount_to_hex(wallet_address, "default")

subaccount_info = engine_client.get_subaccount_info(subaccount)
isolated_positions = engine_client.get_isolated_positions(subaccount).isolated_positions

# Optional: fetch indexer events for Est. PnL display
current_timestamp = int(time.time())
snapshot_response = indexer_client.get_multi_subaccount_snapshots(
    IndexerAccountSnapshotsParams(
        subaccounts=[subaccount],
        timestamps=[current_timestamp],
        isolated=False,
        active=True,
    )
)
snapshots_map = snapshot_response.snapshots
snapshot_events = []
if snapshots_map:
    snapshots_for_subaccount = snapshots_map.get(subaccount) or next(
        iter(snapshots_map.values())
    )
    if snapshots_for_subaccount:
        latest_key = max(snapshots_for_subaccount.keys(), key=int)
        snapshot_events = snapshots_for_subaccount.get(latest_key, [])
indexer_events = snapshot_events

# Calculate all margin metrics
margin_manager = MarginManager(
    subaccount_info,
    isolated_positions,
    indexer_snapshot_events=indexer_events,
)
summary = margin_manager.calculate_account_summary()

# Display formatted summary
print_account_summary(summary)

```

This outputs a complete margin summary:

```python
================================================================================
MARGIN MANAGER ACCOUNT SUMMARY
================================================================================

📊 HEALTH METRICS
  Initial Health:      $999,543,667.24
  Maintenance Health:  $999,761,007.36
  Unweighted Health:   $1,000,086,939.32

📈 MARGIN USAGE
  Initial Margin:      0.05%
  Maintenance Margin:  0.03%

💰 AVAILABLE FUNDS
  Available (Initial):      $999,543,667.24
  Until Liquidation (Maint): $999,761,007.36

📦 PORTFOLIO
  Total Value:  $1,000,086,939.32
  Leverage:     0.11x

```

## Tutorial

### Example 1: Check Account Risk

Monitor your account’s liquidation risk:

```python
from nado_protocol.client import create_nado_client
from nado_protocol.utils.bytes32 import subaccount_to_hex
from nado_protocol.utils.margin_manager import MarginManager

# Create client
client = create_nado_client("testnet", private_key)
subaccount = subaccount_to_hex(client.context.signer.address, "default")

# Fetch data
subaccount_info = client.context.engine_client.get_subaccount_info(subaccount)
isolated = client.context.engine_client.get_isolated_positions(subaccount).isolated_positions

# Calculate metrics
margin_manager = MarginManager(subaccount_info, isolated)
summary = margin_manager.calculate_account_summary()

# Check risk level
maint_usage = summary.maint_margin_usage_fraction * 100

if maint_usage > 90:
    print("🔴 CRITICAL RISK - Near liquidation!")
elif maint_usage > 75:
    print("🟠 HIGH RISK - Reduce positions")
elif maint_usage > 50:
    print("🟡 MEDIUM RISK")
else:
    print("🟢 LOW RISK")

print(f"Margin Usage: {maint_usage:.2f}%")
print(f"Leverage: {summary.account_leverage:.2f}x")
print(f"Available Margin: ${summary.funds_available:,.2f}")

```

### Example 2: Analyze Individual Positions

Get detailed metrics for each position:

```python
# ... setup margin_manager as above ...

summary = margin_manager.calculate_account_summary()

# Cross margin positions
print("\n🔄 CROSS MARGIN POSITIONS\n")
for pos in summary.cross_positions:
    print(f"Product {pos.product_id}:")
    print(f"  Position Size: {pos.position_size:,.4f}")
    print(f"  Notional: ${pos.notional_value:,.2f}")
    print(f"  Margin Used: ${pos.margin_used:,.2f}")
    print(f"  Initial Health: ${pos.initial_health:,.2f}")
    print(f"  Maint Health: ${pos.maintenance_health:,.2f}")

    # Calculate position-specific margin usage
    if pos.notional_value > 0:
        pos_leverage = pos.notional_value / pos.margin_used
        print(f"  Effective Leverage: {pos_leverage:.2f}x")
    print()

# Isolated margin positions
print("\n🔒 ISOLATED MARGIN POSITIONS\n")
for pos in summary.isolated_positions:
    print(f"Product {pos.product_id}:")
    print(f"  Position Size: {pos.position_size:,.4f}")
    print(f"  Notional: ${pos.notional_value:,.2f}")
    print(f"  Net Margin: ${pos.net_margin:,.2f}")
    print(f"  Leverage: {pos.leverage:.2f}x")
    print()

```

### Example 3: Calculate Maximum Position Size

Determine how large of a position you can open:

```python
from decimal import Decimal

# ... setup margin_manager as above ...

summary = margin_manager.calculate_account_summary()

# Get oracle price for a product (e.g., BTC)
btc_product_id = 1
btc_product = next(
    (p for p in subaccount_info.perp_products if p.product_id == btc_product_id),
    None
)

if btc_product:
    from nado_protocol.utils.math import from_x18

    oracle_price = Decimal(from_x18(int(btc_product.oracle_price_x18)))
    long_weight_initial = Decimal(from_x18(int(btc_product.risk.long_weight_initial_x18)))

    # Calculate max position size
    available_margin = summary.funds_available
    leverage_factor = Decimal(1) - long_weight_initial  # e.g., 0.1 for 10x

    max_notional = available_margin / leverage_factor
    max_size = max_notional / oracle_price

    print(f"BTC Oracle Price: ${oracle_price:,.2f}")
    print(f"Available Margin: ${available_margin:,.2f}")
    print(f"Max Position Size: {max_size:.4f} BTC")
    print(f"Max Notional: ${max_notional:,.2f}")

```

### Example 4: Monitor Spot Deposits and Borrows

Track your spot lending activity:

```python
# ... setup margin_manager as above ...

summary = margin_manager.calculate_account_summary()

print("💵 SPOT BALANCE SUMMARY\n")
print(f"Total Deposits: ${summary.total_spot_deposits:,.2f}")
print(f"Total Borrows:  ${summary.total_spot_borrows:,.2f}")
print(f"Net Balance:    ${summary.total_spot_deposits - summary.total_spot_borrows:,.2f}")

# Calculate utilization
if summary.total_spot_deposits > 0:
    utilization = (summary.total_spot_borrows / summary.total_spot_deposits) * 100
    print(f"Utilization:    {utilization:.2f}%")

```

### Example 5: Read-Only Access (No Private Key)

View any public subaccount’s margin metrics:

```python
import time
from nado_protocol.engine_client import EngineQueryClient, EngineClientOpts
from nado_protocol.indexer_client import IndexerQueryClient, IndexerClientOpts
from nado_protocol.indexer_client.types.query import IndexerAccountSnapshotsParams
from nado_protocol.utils.bytes32 import subaccount_to_hex
from nado_protocol.utils.margin_manager import MarginManager

# Any wallet address (no private key needed)
wallet_to_analyze = "0x8D7d64d6cF1D4F018Dd101482Ac71Ad49e30c560"

# Create engine client
engine_client = EngineQueryClient(
    EngineClientOpts(url="https://gateway.test.nado.xyz/v1")
)
indexer_client = IndexerQueryClient(
    IndexerClientOpts(url="https://archive.test.nado.xyz/v1")
)

# Get data
subaccount = subaccount_to_hex(wallet_to_analyze, "default")
subaccount_info = engine_client.get_subaccount_info(subaccount)
isolated = engine_client.get_isolated_positions(subaccount).isolated_positions

# Fetch latest indexer snapshot for Est. PnL (optional)
timestamp = int(time.time())
snapshot = indexer_client.get_multi_subaccount_snapshots(
    IndexerAccountSnapshotsParams(
        subaccounts=[subaccount],
        timestamps=[timestamp],
        isolated=False,
        active=True,
    )
)
indexer_events = snapshot.snapshots.get(subaccount, {}).get(str(timestamp), [])

# Analyze
margin_manager = MarginManager(
    subaccount_info,
    isolated,
    indexer_snapshot_events=indexer_events,
)
summary = margin_manager.calculate_account_summary()

print(f"Analyzing wallet: {wallet_to_analyze}")
print(f"Portfolio Value: ${summary.portfolio_value:,.2f}")
print(f"Leverage: {summary.account_leverage:.2f}x")
print(f"Risk Level: {summary.maint_margin_usage_fraction * 100:.2f}% margin used")

```

## Advanced Usage

### Individual Calculation Methods

Use specific calculation methods for custom analytics:

```python
from nado_protocol.utils.margin_manager import MarginManager
from decimal import Decimal

# ... setup margin_manager ...

# Create a balance object for calculations
from nado_protocol.utils.margin_manager import BalanceWithProduct

balance = BalanceWithProduct(
    product_id=1,
    amount=Decimal("10"),  # 10 BTC long
    oracle_price=Decimal("50000"),
    long_weight_initial=Decimal("0.9"),
    long_weight_maintenance=Decimal("0.95"),
    short_weight_initial=Decimal("1.1"),
    short_weight_maintenance=Decimal("1.05"),
    balance_type="perp",
    v_quote_balance=Decimal("0")
)

# Calculate notional value
notional = margin_manager.calculate_perp_balance_notional_value(balance)
print(f"Notional: ${notional:,.2f}")  # $500,000

# Calculate margin required (without PnL)
health_metrics = margin_manager.calculate_perp_balance_health_without_pnl(balance)
margin_required = abs(health_metrics.initial)
print(f"Margin Required: ${margin_required:,.2f}")  # $50,000 (10x leverage)

# Calculate health contribution
health = margin_manager.calculate_spot_balance_health(balance)
print(f"Initial Health: ${health.initial:,.2f}")
print(f"Maint Health: ${health.maintenance:,.2f}")

```

### Balance Value Utilities

Use the balance utility functions for quick calculations:

```python
from nado_protocol.utils.balance import (
    calculate_spot_balance_value,
    calculate_perp_balance_notional_value,
    calculate_perp_balance_value,
    parse_spot_balance_value,
    parse_perp_balance_value,
)
from decimal import Decimal

# Direct calculations
eth_value = calculate_spot_balance_value(
    amount=Decimal("100"),
    oracle_price=Decimal("2000")
)
print(f"ETH Value: ${eth_value:,.2f}")  # $200,000

# Perp notional
btc_notional = calculate_perp_balance_notional_value(
    amount=Decimal("-5"),  # 5 BTC short
    oracle_price=Decimal("50000")
)
print(f"BTC Notional: ${btc_notional:,.2f}")  # $250,000

# Parse from SDK types
spot_value = parse_spot_balance_value(balance, product)
perp_value = parse_perp_balance_value(balance, product)

```

## Understanding the Results

### AccountSummary Fields

Field

Description

initial_health

Health using initial weights. Must be > 0 to open new positions.

maintenance_health

Health using maintenance weights. Must be > 0 to avoid liquidation.

unweighted_health

Raw portfolio value without haircuts.

margin_usage_fraction

Fraction [0, 1] of initial margin being used.

maint_margin_usage_fraction

Fraction [0, 1] of maintenance margin being used. Risk indicator.

funds_available

Available margin for new positions (= max(0, initial_health)).

funds_until_liquidation

Distance to liquidation (= max(0, maintenance_health)).

portfolio_value

Total portfolio value including isolated positions.

account_leverage

Overall leverage multiplier.

cross_positions

List of cross margin position metrics.

isolated_positions

List of isolated margin position metrics.

total_spot_deposits

Total value of spot deposits.

total_spot_borrows

Total value of spot borrows (absolute).

### CrossPositionMetrics Fields

Field

Description

product_id

Product identifier.

position_size

Position size (positive for long, negative for short).

notional_value

Absolute notional value (= abs(size × oracle_price)).

est_pnl

Estimated PnL from indexer (amount × oracle_price - netEntryUnrealized). Requires indexer data.

unsettled

Full perp balance value (amount × oracle_price + v_quote_balance). This represents unrealized PnL.

margin_used

Margin consumed by position, excluding PnL impact.

initial_health

Health contribution using initial weights.

maintenance_health

Health contribution using maintenance weights.

### IsolatedPositionMetrics Fields

Field

Description

product_id

Product identifier.

position_size

Position size.

notional_value

Absolute notional value.

net_margin

Deposited margin + unsettled PnL.

leverage

Position leverage (= notional / net_margin).

initial_health

Health for the isolated position (initial).

maintenance_health

Health for the isolated position (maintenance).

### Does margin manager use oracle price or market price?

All margin calculations use ORACLE PRICE.

Market prices (bid/ask from the orderbook) are only used for:
- Estimated exit price for unrealized PnL display
-NOTfor any margin or health calculations

### Do I need to convert USDT to USD?

No conversion needed!All values from the engine are already in the correct denomination.

Oracle prices are denominated in the primary quote token (USDT), and all margin calculations work directly with these values. The UI displays dollar signs ($) as a convention, but no USDT→USD price conversion is applied.

Key points:

- Perp tracked variables(netEntryUnrealized,netFundingUnrealized, etc.) are already in quote (USDT) terms

Perp tracked variables(netEntryUnrealized,netFundingUnrealized, etc.) are already in quote (USDT) terms

- No multiplication by USDT/USD ratein any margin calculation

No multiplication by USDT/USD ratein any margin calculation

- The only oracle price multiplicationis for spot interest (converting from token units to USD)

The only oracle price multiplicationis for spot interest (converting from token units to USD)

### How do I calculate initial margin for a perp position?

Common Questions
For a perp position, initial margin is:

```python
notional = abs(position_size × oracle_price)
initial_margin = notional × abs(1 - weight_initial)
maintenance_margin = notional × abs(1 - weight_maintenance)

```

Important: Useabs(1-weight)to handle both long and short positions:

- Long positions: weight < 1, so (1 - weight) > 0

Long positions: weight < 1, so (1 - weight) > 0

- Short positions: weight > 1, so (1 - weight) < 0, need abs()

Short positions: weight > 1, so (1 - weight) < 0, need abs()

Example (Long):
- Position: 10 BTC long
- Oracle Price: $50,000
- Long Weight Initial: 0.9 (allows 10x leverage)

```python
notional = abs(10 × 50,000) = $500,000
initial_margin = 500,000 × (1 - 0.9) = 500,000 × 0.1 = $50,000

```

Example (Short):
- Position: -10 BTC short
- Oracle Price: $50,000
- Short Weight Initial: 1.1 (requires 10x leverage)

```python
notional = abs(-10 × 50,000) = $500,000
initial_margin = 500,000 × abs(1 - 1.1) = 500,000 × 0.1 = $50,000

```

Both positions require $50,000 initial margin (10x leverage).

### Why is my margin usage 0% even though I have positions?

Margin usage is only calculated when:

- Unweighted health > 0

Unweighted health > 0

- Account has borrows OR perp positions

Account has borrows OR perp positions

- Zero-health products are excluded

Zero-health products are excluded

If you only have spot deposits (no borrows, no perps), margin usage will be 0%.

### What’s the difference between cross and isolated margin?

Cross Margin:- Margin shared across ALL positions
- Better capital efficiency
- Risk spreads across entire portfolio
- Default mode

Isolated Margin:- Dedicated margin PER position
- Risk limited to individual position
- Only USDT can be used as margin
- Max 1 isolated position per market
- Useful for high-risk trades

### How is leverage calculated?

Account leverage:

```python
leverage = sum(abs(notional_values)) / unweighted_health

```

Where notional values include:
- Spot: abs(amount × oracle_price) for non-quote products
- Perp: abs(amount × oracle_price)

Quote product (USDT) is excluded from the calculation.

## API Reference

### MarginManager Class

**classnado_protocol.utils.margin_manager.MarginManager(subaccount_info,isolated_positions=None,indexer_snapshot_events=None)[source]**
  Bases:objectComprehensive margin calculator for Nado Protocol.Calculates all margin metrics for a subaccount including health, margin usage,
leverage, and position-level details. Matches TypeScript SDK implementation.QUOTE_PRODUCT_ID=0classmethodfrom_client(client,*,subaccount=None,subaccount_name='default',include_indexer_events=True,snapshot_timestamp=None,snapshot_isolated=False,snapshot_active_only=True)[source]Initialize a MarginManager by fetching data via a NadoClient.Return type:MarginManagerArgs:client: Configured Nado client with engine/indexer connectivity.
subaccount: Optional subaccount hex (bytes32). If omitted, derives the defaultsubaccount using the client’s signer andsubaccount_name.subaccount_name: Subaccount suffix (e.g.default) used when deriving thesubaccount hex. Ignored whensubaccountis provided.include_indexer_events: When True (default), fetch indexer snapshot balancesfor estimated PnL calculations.snapshot_timestamp: Epoch seconds to request from the indexer. Defaults toint(time.time())when indexer data is requested.snapshot_isolated: Passed through to the indexer request to limit snapshotsto isolated (True), cross (False), or all (None) balances. Defaults toFalseto match cross-margin behaviour.snapshot_active_only: When True (default), enables the indexer’sactivefilter so only live balances are returned.Returns:MarginManager instance populated with fresh engine and optional indexer data.calculate_account_summary()[source]Calculate complete account margin summary.Return type:AccountSummaryReturns:AccountSummary with all margin calculationscalculate_spot_balance_value(balance)[source]Calculate quote value of a spot balance.Formula: amount * oracle_priceReturn type:Decimalcalculate_perp_balance_notional_value(balance)[source]Calculate notional value of a perp position.Formula: abs(amount * oracle_price)Return type:Decimalcalculate_perp_balance_value(balance)[source]Calculate true quote value of a perp balance (unrealized PnL).Formula: (amount * oracle_price) + v_quote_balanceReturn type:Decimalcalculate_spot_balance_health(balance)[source]Calculate health contribution for a spot balance.Formula: amount * oracle_price * weight
(weight is long_weight if amount >= 0, else short_weight)Return type:HealthMetricscalculate_perp_balance_health_without_pnl(balance)[source]Calculate perp balance health WITHOUT the impact of unsettled PnL.Shows “margin used” by the position, excluding PnL.
Formula: -1 * abs(notional_value) * (1 - long_weight)Return type:HealthMetricscalculate_cross_position_margin_without_pnl(balance)[source]Calculate margin used for a cross position excluding unsettled PnL impact.Used in margin manager “Margin Used” column.
Formula: max(0, -(initial_health - perp_value))Return type:Decimalcalculate_isolated_position_net_margin(base_balance,quote_balance)[source]Calculate net margin in an isolated position.Formula: quote_amount + (base_amount * oracle_price + v_quote_balance)Return type:Decimalcalculate_isolated_position_leverage(base_balance,net_margin)[source]Calculate leverage for an isolated position.Formula: notional_value / net_marginReturn type:Decimalcalculate_margin_usage_fractions(initial_health,maint_health,unweighted_health)[source]Calculate margin usage fractions bounded to [0, 1].Formula: (unweighted_health - health) / unweighted_health
Returns 0 if no borrows/perps or unweighted_health is 0.Return type:MarginUsageFractionscalculate_account_leverage(balances,unweighted_health)[source]Calculate overall account leverage.Formula: sum(abs(unweighted health for non-quote balances)) / unweighted_healthReturn type:Decimalcalculate_cross_position_metrics(balance)[source]Calculate all metrics for a cross margin position.Return type:CrossPositionMetricscalculate_isolated_position_metrics(iso_pos)[source]Calculate all metrics for an isolated position.Return type:IsolatedPositionMetrics

Bases:object

Comprehensive margin calculator for Nado Protocol.

Calculates all margin metrics for a subaccount including health, margin usage,
leverage, and position-level details. Matches TypeScript SDK implementation.

**QUOTE_PRODUCT_ID=0**

**classmethodfrom_client(client,*,subaccount=None,subaccount_name='default',include_indexer_events=True,snapshot_timestamp=None,snapshot_isolated=False,snapshot_active_only=True)[source]**
  Initialize a MarginManager by fetching data via a NadoClient.Return type:MarginManagerArgs:client: Configured Nado client with engine/indexer connectivity.
subaccount: Optional subaccount hex (bytes32). If omitted, derives the defaultsubaccount using the client’s signer andsubaccount_name.subaccount_name: Subaccount suffix (e.g.default) used when deriving thesubaccount hex. Ignored whensubaccountis provided.include_indexer_events: When True (default), fetch indexer snapshot balancesfor estimated PnL calculations.snapshot_timestamp: Epoch seconds to request from the indexer. Defaults toint(time.time())when indexer data is requested.snapshot_isolated: Passed through to the indexer request to limit snapshotsto isolated (True), cross (False), or all (None) balances. Defaults toFalseto match cross-margin behaviour.snapshot_active_only: When True (default), enables the indexer’sactivefilter so only live balances are returned.Returns:MarginManager instance populated with fresh engine and optional indexer data.

Initialize a MarginManager by fetching data via a NadoClient.

**Return type:**
  MarginManager

MarginManager

**Args:**
  client: Configured Nado client with engine/indexer connectivity.
subaccount: Optional subaccount hex (bytes32). If omitted, derives the defaultsubaccount using the client’s signer andsubaccount_name.subaccount_name: Subaccount suffix (e.g.default) used when deriving thesubaccount hex. Ignored whensubaccountis provided.include_indexer_events: When True (default), fetch indexer snapshot balancesfor estimated PnL calculations.snapshot_timestamp: Epoch seconds to request from the indexer. Defaults toint(time.time())when indexer data is requested.snapshot_isolated: Passed through to the indexer request to limit snapshotsto isolated (True), cross (False), or all (None) balances. Defaults toFalseto match cross-margin behaviour.snapshot_active_only: When True (default), enables the indexer’sactivefilter so only live balances are returned.

client: Configured Nado client with engine/indexer connectivity.
subaccount: Optional subaccount hex (bytes32). If omitted, derives the default

subaccount using the client’s signer andsubaccount_name.

**subaccount_name: Subaccount suffix (e.g.default) used when deriving the**
  subaccount hex. Ignored whensubaccountis provided.

subaccount hex. Ignored whensubaccountis provided.

**include_indexer_events: When True (default), fetch indexer snapshot balances**
  for estimated PnL calculations.

for estimated PnL calculations.

**snapshot_timestamp: Epoch seconds to request from the indexer. Defaults to**
  int(time.time())when indexer data is requested.

int(time.time())when indexer data is requested.

**snapshot_isolated: Passed through to the indexer request to limit snapshots**
  to isolated (True), cross (False), or all (None) balances. Defaults toFalseto match cross-margin behaviour.

to isolated (True), cross (False), or all (None) balances. Defaults toFalseto match cross-margin behaviour.

**snapshot_active_only: When True (default), enables the indexer’sactive**
  filter so only live balances are returned.

filter so only live balances are returned.

**Returns:**
  MarginManager instance populated with fresh engine and optional indexer data.

MarginManager instance populated with fresh engine and optional indexer data.

**calculate_account_summary()[source]**
  Calculate complete account margin summary.Return type:AccountSummaryReturns:AccountSummary with all margin calculations

Calculate complete account margin summary.

**Return type:**
  AccountSummary

AccountSummary

**Returns:**
  AccountSummary with all margin calculations

AccountSummary with all margin calculations

**calculate_spot_balance_value(balance)[source]**
  Calculate quote value of a spot balance.Formula: amount * oracle_priceReturn type:Decimal

Calculate quote value of a spot balance.

Formula: amount * oracle_price

**Return type:**
  Decimal

Decimal

**calculate_perp_balance_notional_value(balance)[source]**
  Calculate notional value of a perp position.Formula: abs(amount * oracle_price)Return type:Decimal

Calculate notional value of a perp position.

Formula: abs(amount * oracle_price)

**Return type:**
  Decimal

Decimal

**calculate_perp_balance_value(balance)[source]**
  Calculate true quote value of a perp balance (unrealized PnL).Formula: (amount * oracle_price) + v_quote_balanceReturn type:Decimal

Calculate true quote value of a perp balance (unrealized PnL).

Formula: (amount * oracle_price) + v_quote_balance

**Return type:**
  Decimal

Decimal

**calculate_spot_balance_health(balance)[source]**
  Calculate health contribution for a spot balance.Formula: amount * oracle_price * weight
(weight is long_weight if amount >= 0, else short_weight)Return type:HealthMetrics

Calculate health contribution for a spot balance.

Formula: amount * oracle_price * weight
(weight is long_weight if amount >= 0, else short_weight)

**Return type:**
  HealthMetrics

HealthMetrics

**calculate_perp_balance_health_without_pnl(balance)[source]**
  Calculate perp balance health WITHOUT the impact of unsettled PnL.Shows “margin used” by the position, excluding PnL.
Formula: -1 * abs(notional_value) * (1 - long_weight)Return type:HealthMetrics

Calculate perp balance health WITHOUT the impact of unsettled PnL.

Shows “margin used” by the position, excluding PnL.
Formula: -1 * abs(notional_value) * (1 - long_weight)

**Return type:**
  HealthMetrics

HealthMetrics

**calculate_cross_position_margin_without_pnl(balance)[source]**
  Calculate margin used for a cross position excluding unsettled PnL impact.Used in margin manager “Margin Used” column.
Formula: max(0, -(initial_health - perp_value))Return type:Decimal

Calculate margin used for a cross position excluding unsettled PnL impact.

Used in margin manager “Margin Used” column.
Formula: max(0, -(initial_health - perp_value))

**Return type:**
  Decimal

Decimal

**calculate_isolated_position_net_margin(base_balance,quote_balance)[source]**
  Calculate net margin in an isolated position.Formula: quote_amount + (base_amount * oracle_price + v_quote_balance)Return type:Decimal

Calculate net margin in an isolated position.

Formula: quote_amount + (base_amount * oracle_price + v_quote_balance)

**Return type:**
  Decimal

Decimal

**calculate_isolated_position_leverage(base_balance,net_margin)[source]**
  Calculate leverage for an isolated position.Formula: notional_value / net_marginReturn type:Decimal

Calculate leverage for an isolated position.

Formula: notional_value / net_margin

**Return type:**
  Decimal

Decimal

**calculate_margin_usage_fractions(initial_health,maint_health,unweighted_health)[source]**
  Calculate margin usage fractions bounded to [0, 1].Formula: (unweighted_health - health) / unweighted_health
Returns 0 if no borrows/perps or unweighted_health is 0.Return type:MarginUsageFractions

Calculate margin usage fractions bounded to [0, 1].

Formula: (unweighted_health - health) / unweighted_health
Returns 0 if no borrows/perps or unweighted_health is 0.

**Return type:**
  MarginUsageFractions

MarginUsageFractions

**calculate_account_leverage(balances,unweighted_health)[source]**
  Calculate overall account leverage.Formula: sum(abs(unweighted health for non-quote balances)) / unweighted_healthReturn type:Decimal

Calculate overall account leverage.

Formula: sum(abs(unweighted health for non-quote balances)) / unweighted_health

**Return type:**
  Decimal

Decimal

**calculate_cross_position_metrics(balance)[source]**
  Calculate all metrics for a cross margin position.Return type:CrossPositionMetrics

Calculate all metrics for a cross margin position.

**Return type:**
  CrossPositionMetrics

CrossPositionMetrics

**calculate_isolated_position_metrics(iso_pos)[source]**
  Calculate all metrics for an isolated position.Return type:IsolatedPositionMetrics

Calculate all metrics for an isolated position.

**Return type:**
  IsolatedPositionMetrics

IsolatedPositionMetrics

### Models

**classnado_protocol.utils.margin_manager.AccountSummary(**data)[source]**
  Complete account margin summary.initial_health:Decimalmaintenance_health:Decimalunweighted_health:Decimalmargin_usage_fraction:Decimalmaint_margin_usage_fraction:Decimalfunds_available:Decimalfunds_until_liquidation:Decimalportfolio_value:Decimalaccount_leverage:Decimalcross_positions:list[CrossPositionMetrics]isolated_positions:list[IsolatedPositionMetrics]spot_positions:list[BalanceWithProduct]total_spot_deposits:Decimaltotal_spot_borrows:DecimalclassConfig[source]arbitrary_types_allowed=True

Complete account margin summary.

**initial_health:Decimal**

**maintenance_health:Decimal**

**unweighted_health:Decimal**

**margin_usage_fraction:Decimal**

**maint_margin_usage_fraction:Decimal**

**funds_available:Decimal**

**funds_until_liquidation:Decimal**

**portfolio_value:Decimal**

**account_leverage:Decimal**

**cross_positions:list[CrossPositionMetrics]**

**isolated_positions:list[IsolatedPositionMetrics]**

**spot_positions:list[BalanceWithProduct]**

**total_spot_deposits:Decimal**

**total_spot_borrows:Decimal**

**classConfig[source]**
  arbitrary_types_allowed=True

**arbitrary_types_allowed=True**

**classnado_protocol.utils.margin_manager.CrossPositionMetrics(**data)[source]**
  Metrics for a cross margin position.product_id:intsymbol:strposition_size:Decimalnotional_value:Decimalest_pnl:Optional[Decimal]unsettled:Decimalmargin_used:Decimalinitial_health:Decimalmaintenance_health:Decimallong_weight_initial:Decimallong_weight_maintenance:Decimalshort_weight_initial:Decimalshort_weight_maintenance:DecimalclassConfig[source]arbitrary_types_allowed=True

Metrics for a cross margin position.

**product_id:int**

**symbol:str**

**position_size:Decimal**

**notional_value:Decimal**

**est_pnl:Optional[Decimal]**

**unsettled:Decimal**

**margin_used:Decimal**

**initial_health:Decimal**

**maintenance_health:Decimal**

**long_weight_initial:Decimal**

**long_weight_maintenance:Decimal**

**short_weight_initial:Decimal**

**short_weight_maintenance:Decimal**

**classConfig[source]**
  arbitrary_types_allowed=True

**arbitrary_types_allowed=True**

**classnado_protocol.utils.margin_manager.IsolatedPositionMetrics(**data)[source]**
  Metrics for an isolated margin position.product_id:intsymbol:strposition_size:Decimalnotional_value:Decimalnet_margin:Decimalleverage:Decimalinitial_health:Decimalmaintenance_health:DecimalclassConfig[source]arbitrary_types_allowed=True

Metrics for an isolated margin position.

**product_id:int**

**symbol:str**

**position_size:Decimal**

**notional_value:Decimal**

**net_margin:Decimal**

**leverage:Decimal**

**initial_health:Decimal**

**maintenance_health:Decimal**

**classConfig[source]**
  arbitrary_types_allowed=True

**arbitrary_types_allowed=True**

**classnado_protocol.utils.margin_manager.HealthMetrics(**data)[source]**
  Initial and maintenance health metrics.initial:Decimalmaintenance:Decimal

Initial and maintenance health metrics.

**initial:Decimal**

**maintenance:Decimal**

**classnado_protocol.utils.margin_manager.MarginUsageFractions(**data)[source]**
  Margin usage as a fraction [0, 1].initial:Decimalmaintenance:Decimal

Margin usage as a fraction [0, 1].

**initial:Decimal**

**maintenance:Decimal**

### Utility Functions

**nado_protocol.utils.margin_manager.print_account_summary(summary)[source]**
  Print formatted account summary matching UI layout.Return type:None

Print formatted account summary matching UI layout.

**Return type:**
  None

None

Balance Value Calculation Utilities

**nado_protocol.utils.balance.calculate_spot_balance_value(amount,oracle_price)[source]**
  Calculate the quote value of a spot balance.Formula: amount * oracle_priceThis is used for:
- Calculating health contributions
- Determining deposits vs borrows
- Portfolio value calculationsReturn type:DecimalArgs:amount: Token amount (can be negative for borrows)
oracle_price: Oracle price in quote currencyReturns:Value in quote currency (positive for deposits, negative for borrows)Example:>>>calculate_spot_balance_value(100,2000)# 100 ETH at $2000Decimal('200000')>>>calculate_spot_balance_value(-50,2000)# 50 ETH borrowedDecimal('-100000')

Calculate the quote value of a spot balance.

Formula: amount * oracle_price

This is used for:
- Calculating health contributions
- Determining deposits vs borrows
- Portfolio value calculations

**Return type:**
  Decimal

Decimal

**Args:**
  amount: Token amount (can be negative for borrows)
oracle_price: Oracle price in quote currency

amount: Token amount (can be negative for borrows)
oracle_price: Oracle price in quote currency

**Returns:**
  Value in quote currency (positive for deposits, negative for borrows)

Value in quote currency (positive for deposits, negative for borrows)

**Example:**
  >>>calculate_spot_balance_value(100,2000)# 100 ETH at $2000Decimal('200000')>>>calculate_spot_balance_value(-50,2000)# 50 ETH borrowedDecimal('-100000')

```python
>>> calculate_spot_balance_value(100, 2000)  # 100 ETH at $2000
Decimal('200000')
>>> calculate_spot_balance_value(-50, 2000)  # 50 ETH borrowed
Decimal('-100000')

```

**nado_protocol.utils.balance.calculate_perp_balance_notional_value(amount,oracle_price)[source]**
  Calculate the notional value of a perp position.Formula: abs(amount * oracle_price)This represents the total size of the position in quote currency terms,
regardless of direction (long or short).Return type:DecimalArgs:amount: Position size (positive for long, negative for short)
oracle_price: Oracle price in quote currencyReturns:Absolute notional value in quote currencyExample:>>>calculate_perp_balance_notional_value(10,50000)# 10 BTC longDecimal('500000')>>>calculate_perp_balance_notional_value(-10,50000)# 10 BTC shortDecimal('500000')

Calculate the notional value of a perp position.

Formula: abs(amount * oracle_price)

This represents the total size of the position in quote currency terms,
regardless of direction (long or short).

**Return type:**
  Decimal

Decimal

**Args:**
  amount: Position size (positive for long, negative for short)
oracle_price: Oracle price in quote currency

amount: Position size (positive for long, negative for short)
oracle_price: Oracle price in quote currency

**Returns:**
  Absolute notional value in quote currency

Absolute notional value in quote currency

**Example:**
  >>>calculate_perp_balance_notional_value(10,50000)# 10 BTC longDecimal('500000')>>>calculate_perp_balance_notional_value(-10,50000)# 10 BTC shortDecimal('500000')

```python
>>> calculate_perp_balance_notional_value(10, 50000)  # 10 BTC long
Decimal('500000')
>>> calculate_perp_balance_notional_value(-10, 50000)  # 10 BTC short
Decimal('500000')

```

**nado_protocol.utils.balance.calculate_perp_balance_value(amount,oracle_price,v_quote_balance)[source]**
  Calculate the true quote value of a perp balance (unrealized PnL).Formula: (amount * oracle_price) + v_quote_balanceThe v_quote_balance represents:
- Unrealized PnL from price changes
- Accumulated funding payments
- Entry cost adjustmentsThis value is what would be added to your balance if the position were closed.Return type:DecimalArgs:amount: Position size
oracle_price: Oracle price in quote currency
v_quote_balance: Virtual quote balance (unsettled PnL)Returns:Total value in quote currency (can be positive or negative)Example:>>># Long 10 BTC at $50k, now at $51k, with funding>>>calculate_perp_balance_value(10,51000,-500000)Decimal('10000')  # $10k profit

Calculate the true quote value of a perp balance (unrealized PnL).

Formula: (amount * oracle_price) + v_quote_balance

The v_quote_balance represents:
- Unrealized PnL from price changes
- Accumulated funding payments
- Entry cost adjustments

This value is what would be added to your balance if the position were closed.

**Return type:**
  Decimal

Decimal

**Args:**
  amount: Position size
oracle_price: Oracle price in quote currency
v_quote_balance: Virtual quote balance (unsettled PnL)

amount: Position size
oracle_price: Oracle price in quote currency
v_quote_balance: Virtual quote balance (unsettled PnL)

**Returns:**
  Total value in quote currency (can be positive or negative)

Total value in quote currency (can be positive or negative)

**Example:**
  >>># Long 10 BTC at $50k, now at $51k, with funding>>>calculate_perp_balance_value(10,51000,-500000)Decimal('10000')  # $10k profit

```python
>>> # Long 10 BTC at $50k, now at $51k, with funding
>>> calculate_perp_balance_value(10, 51000, -500000)
Decimal('10000')  # $10k profit

```

**nado_protocol.utils.balance.parse_spot_balance_value(balance,product)[source]**
  Parse spot balance value from raw SDK types.This is a convenience function that extracts values from the SDK types
and calls calculate_spot_balance_value.Return type:DecimalArgs:balance: Spot balance from subaccount info
product: Spot product informationReturns:Balance value in quote currency

Parse spot balance value from raw SDK types.

This is a convenience function that extracts values from the SDK types
and calls calculate_spot_balance_value.

**Return type:**
  Decimal

Decimal

**Args:**
  balance: Spot balance from subaccount info
product: Spot product information

balance: Spot balance from subaccount info
product: Spot product information

**Returns:**
  Balance value in quote currency

Balance value in quote currency

**nado_protocol.utils.balance.parse_perp_balance_notional_value(balance,product)[source]**
  Parse perp notional value from raw SDK types.Return type:DecimalArgs:balance: Perp balance from subaccount info
product: Perp product informationReturns:Notional value in quote currency

Parse perp notional value from raw SDK types.

**Return type:**
  Decimal

Decimal

**Args:**
  balance: Perp balance from subaccount info
product: Perp product information

balance: Perp balance from subaccount info
product: Perp product information

**Returns:**
  Notional value in quote currency

Notional value in quote currency

**nado_protocol.utils.balance.parse_perp_balance_value(balance,product)[source]**
  Parse perp balance value (unrealized PnL) from raw SDK types.Return type:DecimalArgs:balance: Perp balance from subaccount info
product: Perp product informationReturns:Balance value in quote currency

Parse perp balance value (unrealized PnL) from raw SDK types.

**Return type:**
  Decimal

Decimal

**Args:**
  balance: Perp balance from subaccount info
product: Perp product information

balance: Perp balance from subaccount info
product: Perp product information

**Returns:**
  Balance value in quote currency

Balance value in quote currency

**nado_protocol.utils.balance.calculate_total_spot_deposits_and_borrows(balances)[source]**
  Calculate total spot deposits and borrows across all balances.Return type:tuple[Decimal,Decimal]Args:balances: List of (balance, product) tuplesReturns:Tuple of (total_deposits, total_borrows) in quote currency
Both values are positive (borrows is absolute value)Example:>>>balances=[(usdt_balance,usdt_product),(eth_balance,eth_product)]>>>deposits,borrows=calculate_total_spot_deposits_and_borrows(balances)>>>deposits# Total depositsDecimal('10000')>>>borrows# Total borrows (absolute value)Decimal('5000')

Calculate total spot deposits and borrows across all balances.

**Return type:**
  tuple[Decimal,Decimal]

tuple[Decimal,Decimal]

**Args:**
  balances: List of (balance, product) tuples

balances: List of (balance, product) tuples

**Returns:**
  Tuple of (total_deposits, total_borrows) in quote currency
Both values are positive (borrows is absolute value)

Tuple of (total_deposits, total_borrows) in quote currency
Both values are positive (borrows is absolute value)

**Example:**
  >>>balances=[(usdt_balance,usdt_product),(eth_balance,eth_product)]>>>deposits,borrows=calculate_total_spot_deposits_and_borrows(balances)>>>deposits# Total depositsDecimal('10000')>>>borrows# Total borrows (absolute value)Decimal('5000')

```python
>>> balances = [(usdt_balance, usdt_product), (eth_balance, eth_product)]
>>> deposits, borrows = calculate_total_spot_deposits_and_borrows(balances)
>>> deposits  # Total deposits
Decimal('10000')
>>> borrows   # Total borrows (absolute value)
Decimal('5000')

```

**nado_protocol.utils.balance.calculate_total_perp_notional(balances)[source]**
  Calculate total notional value across all perp positions.Return type:DecimalArgs:balances: List of (balance, product) tuplesReturns:Total notional value in quote currencyExample:>>>balances=[(btc_perp_balance,btc_perp_product)]>>>total=calculate_total_perp_notional(balances)>>>totalDecimal('500000')  # Total position size

Calculate total notional value across all perp positions.

**Return type:**
  Decimal

Decimal

**Args:**
  balances: List of (balance, product) tuples

balances: List of (balance, product) tuples

**Returns:**
  Total notional value in quote currency

Total notional value in quote currency

**Example:**
  >>>balances=[(btc_perp_balance,btc_perp_product)]>>>total=calculate_total_perp_notional(balances)>>>totalDecimal('500000')  # Total position size

```python
>>> balances = [(btc_perp_balance, btc_perp_product)]
>>> total = calculate_total_perp_notional(balances)
>>> total
Decimal('500000')  # Total position size

```

**nado_protocol.utils.balance.calculate_total_perp_value(balances)[source]**
  Calculate total unrealized PnL across all perp positions.Return type:DecimalArgs:balances: List of (balance, product) tuplesReturns:Total unrealized PnL in quote currency (can be positive or negative)Example:>>>balances=[(btc_perp_balance,btc_perp_product)]>>>total_pnl=calculate_total_perp_value(balances)>>>total_pnlDecimal('10000')  # $10k unrealized profit

Calculate total unrealized PnL across all perp positions.

**Return type:**
  Decimal

Decimal

**Args:**
  balances: List of (balance, product) tuples

balances: List of (balance, product) tuples

**Returns:**
  Total unrealized PnL in quote currency (can be positive or negative)

Total unrealized PnL in quote currency (can be positive or negative)

**Example:**
  >>>balances=[(btc_perp_balance,btc_perp_product)]>>>total_pnl=calculate_total_perp_value(balances)>>>total_pnlDecimal('10000')  # $10k unrealized profit

```python
>>> balances = [(btc_perp_balance, btc_perp_product)]
>>> total_pnl = calculate_total_perp_value(balances)
>>> total_pnl
Decimal('10000')  # $10k unrealized profit

```

## See Also

- Getting started- SDK basics

Getting started- SDK basics

- user-guides- Other usage examples

user-guides- Other usage examples

- api-reference- Complete API documentation

api-reference- Complete API documentation