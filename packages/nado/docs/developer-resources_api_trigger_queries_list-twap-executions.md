---
url: https://docs.nado.xyz/developer-resources/api/trigger/queries/list-twap-executions
title: List TWAP Executions
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Trigger
[Trigger](/developer-resources/api/trigger)
- Queries
[Queries](/developer-resources/api/trigger/queries)

# List TWAP Executions

Gets the execution details for a specific TWAP trigger order by digest.

## Request

POST [TRIGGER_ENDPOINT]/query

`POST [TRIGGER_ENDPOINT]/query`

Body

```

{
  "type": "list_twap_executions",
  "digest": "0x5886d5eee7dc4879c7f8ed1222fdbbc0e3681a14c1e55d7859515898c7bd2038"
}
```

## Request Parameters

digest

string

Yes

The digest of the TWAP trigger order to get execution details for.

## Response

#### Success

```
{
  "status": "success",
  "data": {
    "executions": [
      {
        "execution_id": 1,
        "scheduled_time": 1688768157,
        "status": "pending",
        "updated_at": 1688768157050
      },
      {
        "execution_id": 2,
        "scheduled_time": 1688768187,
        "status": {
          "executed": {
            "executed_time": 1688768187050,
            "execute_response": {
              "status": "success",
              "data": {
                "digest": "0x..."
              },
              "id": 12345,
              "request_type": "place_order"
            }
          }
        },
        "updated_at": 1688768187050
      },
      {
        "execution_id": 3,
        "scheduled_time": 1688768217,
        "status": {
          "failed": "Insufficient balance"
        },
        "updated_at": 1688768217050
      },
      {
        "execution_id": 4,
        "scheduled_time": 1688768247,
        "status": {
          "cancelled": "user_requested"
        },
        "updated_at": 1688768247050
      }
    ]
  },
  "request_type": "query_list_twap_executions"
}
```

Note: TWAP executions can have the following statuses:

- pending: execution is scheduled but has not yet been attempted.

pending: execution is scheduled but has not yet been attempted.

- executed: execution was successful, includes execution time and response details from the engine.

executed: execution was successful, includes execution time and response details from the engine.

- failed: execution failed, includes error message.

failed: execution failed, includes error message.

- cancelled: execution was cancelled, includes cancellation reason (e.g., "user_requested", "linked_signer_changed", "expired", "account_health", "isolated_subaccount_closed", "dependent_order_cancelled").

cancelled: execution was cancelled, includes cancellation reason (e.g., "user_requested", "linked_signer_changed", "expired", "account_health", "isolated_subaccount_closed", "dependent_order_cancelled").

#### Failure

[PreviousList Trigger Orders](/developer-resources/api/trigger/queries/list-trigger-orders)
[NextV2](/developer-resources/api/v2)

Last updated1 month ago