---
url: https://docs.nado.xyz/developer-resources/api/trigger/queries
title: Queries
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Trigger
[Trigger](/developer-resources/api/trigger)

# Queries

Trigger Service - Queries

All queries go through the following endpoint; the exact details of the query are specified by the JSON payload.

- REST:POST [TRIGGER_ENDPOINT]/query

REST:POST [TRIGGER_ENDPOINT]/query

`POST [TRIGGER_ENDPOINT]/query`

## API Response

Allqueriesreturn in the format:

`queries`

```
{
  "status": "success" | "failure",
  "data"?: {data},
  "error"?: "{error_msg}",
  "error_code"?: {error_code},
  "request_type": "{request_type}"
}
```

## Available Queries:

[List Trigger Orders](/developer-resources/api/trigger/queries/list-trigger-orders)
[List TWAP Executions](/developer-resources/api/trigger/queries/list-twap-executions)
[PreviousCancel Product Orders](/developer-resources/api/trigger/executes/cancel-product-orders)
[NextList Trigger Orders](/developer-resources/api/trigger/queries/list-trigger-orders)

Last updated1 month ago