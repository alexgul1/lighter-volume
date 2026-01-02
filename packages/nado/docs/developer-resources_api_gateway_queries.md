---
url: https://docs.nado.xyz/developer-resources/api/gateway/queries
title: Queries
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)

# Queries

Nado Queries - Websocket and REST API

All queries go through the following endpoint; the exact details of the query are specified by query params orWebsocketmessages.

`Websocket`
- Websocket:WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

Websocket:WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`
- REST:GET [GATEWAY_REST_ENDPOINT]/queryorPOST [GATEWAY_REST_ENDPOINT]/query

REST:GET [GATEWAY_REST_ENDPOINT]/queryorPOST [GATEWAY_REST_ENDPOINT]/query

`GET [GATEWAY_REST_ENDPOINT]/query`
`POST [GATEWAY_REST_ENDPOINT]/query`

## Overview

### Amounts and Prices

In general, amounts come back normalized to 18 decimal places. Meaning that for a balance of 1 USDT0, regardless of the number of decimals USDT0 has on-chain, a value of 1e18 will be returned.

Prices are inx18, so if the price of one wBTC is $20,000, regardless of the number of decimals wBTC has on-chain, the price will be returned as20,000 * 1e18.

`x18`
`20,000 * 1e18`

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

[PreviousLink Signer](/developer-resources/api/gateway/executes/link-signer)
[NextStatus](/developer-resources/api/gateway/queries/status)

Last updated1 month ago