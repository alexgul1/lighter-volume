---
url: https://docs.nado.xyz/developer-resources/api/trigger/queries/list-trigger-orders
title: List Trigger Orders
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Trigger
[Trigger](/developer-resources/api/trigger)
- Queries
[Queries](/developer-resources/api/trigger/queries)

# List Trigger Orders

Gets cancelled, pending or executed trigger orders for the provided subaccount and products.

## Request

POST [TRIGGER_ENDPOINT]/query

`POST [TRIGGER_ENDPOINT]/query`

Body

```

{
  "type": "list_trigger_orders",
  "tx": {
    "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
    "recvTime": "1688768157050"
  },
  "signature": "0x",
  "product_ids": [1, 2],
  "max_update_time": 1688768157,
  "limit": 20
}
```

POST [TRIGGER_ENDPOINT]/query

`POST [TRIGGER_ENDPOINT]/query`

Body

```

{
  "type": "list_trigger_orders",
  "tx": {
    "sender": "0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43746573743000000000000000",
    "recvTime": "1688768157050"
  },
  "signature": "0x",
  "digests": ["0x5886d5eee7dc4879c7f8ed1222fdbbc0e3681a14c1e55d7859515898c7bd2038"],
  "limit": 20
}
```

POST [TRIGGER_ENDPOINT]/query

`POST [TRIGGER_ENDPOINT]/query`

Body

POST [TRIGGER_ENDPOINT]/query

`POST [TRIGGER_ENDPOINT]/query`

Body

## Request Parameters

Note:max_update_timeIt's the time that the trigger order last changed state. For example, if a trigger order is placed & pending, the update time = time of placement. If the trigger order is cancelled, then the update time = time of cancellation.

`max_update_time`

tx

object

Yes

List trigger orders transaction object. SeeSigningsection for details on the transaction fields.

[Signing](/developer-resources/api/trigger/queries/list-trigger-orders#signing)

tx.sender

string

Yes

Hex string representing the subaccount's 32 bytes (address + subaccount name) of the tx sender.

tx.recvTime

string

Yes

Encoded time in milliseconds after which the list trigger orders transaction will be ignored. cannot be more than 100 seconds from the time it is received by the server.

signature

string

Yes

Signed transaction. SeeSigningsection for more details.

[Signing](/developer-resources/api/trigger/queries/list-trigger-orders#signing)

product_ids

number[]

No

If provided, returns trigger orders for the specified products; otherwise, returns trigger orders for all products.

trigger_types

string[]

No

If provided, filters by trigger type. Values:price_trigger,time_trigger.

`price_trigger`
`time_trigger`

status_types

string[]

No

If provided, filters by order status. Values:cancelled,triggered,internal_error,triggering,waiting_price,waiting_dependency,twap_executing,twap_completed.

`cancelled`
`triggered`
`internal_error`
`triggering`
`waiting_price`
`waiting_dependency`
`twap_executing`
`twap_completed`

max_update_time

number

No

If provided, returns all trigger orders that were last updated up tomax_update_time. must be a unix epoch in seconds.

`max_update_time`

max_digest

string

No

If provided, returns all trigger orders up to the given order digest (exclusive). This can be used for pagination.

digests

string[]

No

If provided, only returns the trigger orders for the associated digests.Note: all other filters are ignored whendigestsis provided.

`digests`

reduce_only

boolean

No

If provided, filters trigger orders by reduce-only flag.truereturns only orders that can only decrease existing positions. If omitted, returns all orders regardless of reduce-only status.

`true`

limit

number

No

If provided, returns the most recently updated trigger orders up tolimit. defaults to 100. max limit is 500.

`limit`

## Signing

See more details and and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The solidity typed data struct that needs to be signed is:

sender: abytes32sent as a hex string; includes the address and the subaccount identifier

`sender`
`bytes32`

recvTime: the time in milliseconds (arecv_time) after which the transaction should be ignored by the trigger service. cannot be more than 100 seconds from the time it is received by the server.

`recvTime`
`recv_time`

Note: for signing you should always use the data type specified in the solidity struct which might be different from the type sent in the request e.g:recvTimeshould be anuint64forSigningbut should be sent as astringin the final payload.

`recvTime`
`uint64`
`string`

## Response

#### Success

Note: trigger orders can have the following statuses:

- cancelled: trigger order was cancelled due to user request, order expiration, or account health issues.

cancelled: trigger order was cancelled due to user request, order expiration, or account health issues.

- triggered: trigger criteria was met, and order was submitted for execution.

triggered: trigger criteria was met, and order was submitted for execution.

- internal_error: an internal error occurred while processing the trigger order.

internal_error: an internal error occurred while processing the trigger order.

- triggering: trigger order is currently being processed for execution.

triggering: trigger order is currently being processed for execution.

- waiting_price: trigger order is waiting for price criteria to be met.

waiting_price: trigger order is waiting for price criteria to be met.

- waiting_dependency: trigger order is waiting for a dependency order to be filled.

waiting_dependency: trigger order is waiting for a dependency order to be filled.

- twap_executing: TWAP order is currently executing individual orders over time.

twap_executing: TWAP order is currently executing individual orders over time.

- twap_completed: TWAP order has completed all scheduled executions.

twap_completed: TWAP order has completed all scheduled executions.

#### Failure

[PreviousQueries](/developer-resources/api/trigger/queries)
[NextList TWAP Executions](/developer-resources/api/trigger/queries/list-twap-executions)

Last updated1 month ago