---
url: https://docs.nado.xyz/developer-resources/api/order-appendix
title: Order Appendix
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Order Appendix

TheOrder Appendixis a 128-bit integer that encodes extra order parameters like execution type, isolated margin, and trigger configurations.

## Bit Layout

```
| value   | reserved | trigger | reduce only | order type | isolated | version |
| 64 bits | 50 bits  | 2 bits  | 1 bit       | 2 bits     | 1 bit    | 8 bits  |
| 127..64 | 63..14   | 13..12  | 11          | 10..9      | 8        | 7..0    |
```

## Fields (from LSB to MSB)

### Version

8-bits (0-7). Protocol version identifier. Currently1. May increment when encoding structure updates.

`1`

### Isolated

1-bit (8). Indicates whether the order uses isolated margin. Isolated positions have dedicated margin for a specific product, creating a separate isolated subaccount. The original account becomes the "parent subaccount" that can manage the isolated position.

Key Properties:

- Creates isolated subaccount with dedicated margin

Creates isolated subaccount with dedicated margin

- Only quote transfers allowed between isolated and parent subaccounts

Only quote transfers allowed between isolated and parent subaccounts

- Parent account can sign orders for isolated subaccount

Parent account can sign orders for isolated subaccount

- Cannot be combined with TWAP orders

Cannot be combined with TWAP orders

Example:

### Order Type

2-bits (9-10). Execution behavior for the order.

Values:

- 0-DEFAULT: Standard limit order behavior.

0-DEFAULT: Standard limit order behavior.

`0`
`DEFAULT`
- 1-IOC (Immediate or Cancel): Execute immediately, cancel unfilled portion.

1-IOC (Immediate or Cancel): Execute immediately, cancel unfilled portion.

`1`
`IOC (Immediate or Cancel)`
- 2-FOK (Fill or Kill): Execute completely or cancel entire order.

2-FOK (Fill or Kill): Execute completely or cancel entire order.

`2`
`FOK (Fill or Kill)`
- 3-POST_ONLY: Only add liquidity, reject if would take liquidity.

3-POST_ONLY: Only add liquidity, reject if would take liquidity.

`3`
`POST_ONLY`

Example:

### Reduce Only

1-bit (11). Restricts order to only decrease existing positions. Prevent accidentally increasing position size. Order will be rejected if it would increase the position in the same direction.

Use Cases:

- Risk management when closing positions.

Risk management when closing positions.

- Taking profits without adding exposure.

Taking profits without adding exposure.

- Automated position reduction strategies.

Automated position reduction strategies.

Example:

### Trigger Type

2-bits (12-13). Conditional execution behavior.

Values:

- 0-NONE: Execute immediately (regular order).

0-NONE: Execute immediately (regular order).

`0`
`NONE`
- 1-PRICE: Price-based conditional order.

1-PRICE: Price-based conditional order.

`1`
`PRICE`
- 2-TWAP: Time-Weighted Average Price execution.

2-TWAP: Time-Weighted Average Price execution.

`2`
`TWAP`
- 3-TWAP_CUSTOM_AMOUNTS: TWAP with randomized amounts.

3-TWAP_CUSTOM_AMOUNTS: TWAP with randomized amounts.

`3`
`TWAP_CUSTOM_AMOUNTS`

Example:

### Reserved

50-bits (14-63). Reserved for future protocol extensions. Must be set to0.

`0`

### Value

64-bits (64-127). Context-dependent data based on other flags.

#### TWAP Configuration (when trigger = 2 or 3)

Encodes TWAP execution parameters in the 64-bit value field:

Fields:

- times: Number of TWAP executions.

times: Number of TWAP executions.

`times`
- slippage_x6: Maximum slippage × 1_000_000 (6 decimal precision).

slippage_x6: Maximum slippage × 1_000_000 (6 decimal precision).

`slippage_x6`

Example:

#### Isolated Margin (when isolated = 1)

Amount of quote (margin_x6) to transfer to isolated subaccount on first fill, stored in the 64-bit value field.

Important:Isolated margin is stored inx6 precision(6 decimals) in the appendix value field.

- Stored asmargin_x6(6 decimal places)

Stored asmargin_x6(6 decimal places)

`margin_x6`
- Takes up 64 bits (bits 64-127 of the appendix)

Takes up 64 bits (bits 64-127 of the appendix)

Example:

## Constraints

- Isolated + TWAP: Cannot combine isolated orders with TWAP (trigger types 2 or 3).

Isolated + TWAP: Cannot combine isolated orders with TWAP (trigger types 2 or 3).

- TWAP Requirements: TWAP orders must specify bothtwap_timesandtwap_slippage_frac.

TWAP Requirements: TWAP orders must specify bothtwap_timesandtwap_slippage_frac.

`twap_times`
`twap_slippage_frac`
- Isolated Margin: Can only setisolated_marginwhenisolated=True.

Isolated Margin: Can only setisolated_marginwhenisolated=True.

`isolated_margin`
`isolated=True`

## Migration from Legacy Format

Before (deprecated):

- Order type encoded inexpirationfield.

Order type encoded inexpirationfield.

`expiration`
- Reduce-only flag encoded innoncefield.

Reduce-only flag encoded innoncefield.

`nonce`
- Limited trigger functionality.

Limited trigger functionality.

After (current):

- All flags consolidated in 128-bitappendix.

All flags consolidated in 128-bitappendix.

`appendix`
- expirationis pure timestamp.

expirationis pure timestamp.

`expiration`
- nonceencodesrecv_timeonly.

nonceencodesrecv_timeonly.

`nonce`
`recv_time`
- Enhanced trigger and isolated margin support.

Enhanced trigger and isolated margin support.

## Building Appendix Values

#### Using Python SDK (Recommended)

#### Manual Bit Manipulation (Advanced)

Refer tonado_protocol.utils.orderfor a detailed implementation.

[nado_protocol.utils.order](https://nadohq.github.io/nado-python-sdk/_modules/nado_protocol/utils/order.html)

### Utility Functions

[PreviousTrades](/developer-resources/api/v2/trades)
[NextRate limits](/developer-resources/api/rate-limits)

Last updated1 month ago