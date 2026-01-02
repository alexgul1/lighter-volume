---
url: https://docs.nado.xyz/developer-resources/api/trigger/executes
title: Executes
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Trigger
[Trigger](/developer-resources/api/trigger)

# Executes

Trigger Service - Executes

## Overview

All executes go through the following endpoint; the exact details of the execution are specified by the JSON payload.

- REST:POST [TRIGGER_ENDPOINT]/execute

REST:POST [TRIGGER_ENDPOINT]/execute

`POST [TRIGGER_ENDPOINT]/execute`

## API Response

AllExecutemessages return the following information:

`Execute`

```
{
  "status": "success" | "failure",
  "error"?: "{error_msg}",
  "error_code"?: {error_code},
  "request_type": "{request_type}",
}
```

## Available Executes:

[Place Order](/developer-resources/api/trigger/executes/place-order)
[Cancel Orders](/developer-resources/api/trigger/executes/cancel-orders)
[Cancel Product Orders](/developer-resources/api/trigger/executes/cancel-product-orders)
[PreviousTrigger](/developer-resources/api/trigger)
[NextPlace Order](/developer-resources/api/trigger/executes/place-order)

Last updated1 month ago