---
url: https://docs.nado.xyz/developer-resources/api/trigger
title: Trigger
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Trigger

Place conditional orders triggered by price levels or time intervals, including stop orders and TWAP execution.

The trigger service enables sophisticated order execution strategies through conditional triggers:

## Order Types

### Price Triggers

Execute orders when price conditions are met:

- Stop orders: Trigger when price moves above or below a threshold

Stop orders: Trigger when price moves above or below a threshold

- Take profit/Stop loss: Automated position management

Take profit/Stop loss: Automated position management

- Support multiple price sources: Oracle price, last trade price, or mid-book price

Support multiple price sources: Oracle price, last trade price, or mid-book price

### Time Triggers (TWAP)

Execute large orders over time using Time-Weighted Average Price:

- Split large orders: Break into smaller executions to reduce market impact

Split large orders: Break into smaller executions to reduce market impact

- Configurable intervals: Set time between executions

Configurable intervals: Set time between executions

- Slippage protection: Built-in slippage limits for each execution

Slippage protection: Built-in slippage limits for each execution

- Custom amounts: Specify exact amounts for each execution or split evenly

Custom amounts: Specify exact amounts for each execution or split evenly

## API Structure

There are two types of actions:

- Execute: Modifies state (place/cancel orders)

Execute: Modifies state (place/cancel orders)

`Execute`
- Query: Fetches information (list orders, TWAP status)

Query: Fetches information (list orders, TWAP status)

`Query`

HTTP Endpoints:

- POST [TRIGGER_ENDPOINT]/executefor order placement and cancellation

POST [TRIGGER_ENDPOINT]/executefor order placement and cancellation

`POST [TRIGGER_ENDPOINT]/execute`
- POST [TRIGGER_ENDPOINT]/queryfor querying trigger order status

POST [TRIGGER_ENDPOINT]/queryfor querying trigger order status

`POST [TRIGGER_ENDPOINT]/query`

HTTPrequests must set theAccept-Encodingto includegzip,brordeflate

`HTTP`
`Accept-Encoding`
`gzip`
`br`
`deflate`

## Rate Limits

- Maximum pending orders: 25 pending trigger orders per product per subaccount

Maximum pending orders: 25 pending trigger orders per product per subaccount

- TWAP constraints: Must use IOC execution type, cannot combine with isolated margin

TWAP constraints: Must use IOC execution type, cannot combine with isolated margin

## Key Requirements

### Order Appendix Configuration

All trigger orders require properOrder Appendixconfiguration:

[Order Appendix](/developer-resources/api/order-appendix)
- Trigger type: Specify price (1), TWAP (2), or TWAP with custom amounts (3) in appendix bits

Trigger type: Specify price (1), TWAP (2), or TWAP with custom amounts (3) in appendix bits

- Execution type: TWAP ordersmustuse IOC execution

Execution type: TWAP ordersmustuse IOC execution

- TWAP parameters: Encode execution count and slippage limits in appendix value field

TWAP parameters: Encode execution count and slippage limits in appendix value field

## Endpoints

### Testnet:

- https://trigger.test.nado.xyz/v1

https://trigger.test.nado.xyz/v1

`https://trigger.test.nado.xyz/v1`
[Executes](/developer-resources/api/trigger/executes)
[Queries](/developer-resources/api/trigger/queries)
[PreviousInk Airdrop](/developer-resources/api/archive-indexer/ink-airdrop)
[NextExecutes](/developer-resources/api/trigger/executes)

Last updated1 month ago