---
url: https://docs.nado.xyz/developer-resources/api/gateway
title: Gateway
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Gateway

Interactions with Nado's offchain sequencer

There are two types of actions. AnExecuteinvolves a modification to state, and aQuerymerely fetches information from state.

`Execute`
`Query`

All actions can be sent over websocket as json payloads atWEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]

`WEBSOCKET [GATEWAY_WEBSOCKET_ENDPOINT]`

Additionally, you can send executes and queries overHTTP, atPOST [GATEWAY_REST_ENDPOINT]/executeandGET/POST [GATEWAY_REST_ENDPOINT]/queryrespectively. For executes, the request should be sent with a json payload, while for queries, the payload should be encoded into url query strings.

`POST [GATEWAY_REST_ENDPOINT]/execute`
`GET/POST [GATEWAY_REST_ENDPOINT]/query`

HTTPrequests must set theAccept-Encodingto includegzip,brordeflate

`HTTP`
`Accept-Encoding`
`gzip`
`br`
`deflate`

## Endpoints

### Testnet:

- Websocket:wss://gateway.test.nado.xyz/v1/ws

Websocket:wss://gateway.test.nado.xyz/v1/ws

`wss://gateway.test.nado.xyz/v1/ws`
- REST:https://gateway.test.nado.xyz/v1

REST:https://gateway.test.nado.xyz/v1

`https://gateway.test.nado.xyz/v1`

## Websocket

Notes onkeeping websocket connections alive:

- When interacting with our API via websocket, you must send ping frames every 30 seconds to keep the websocket connection alive.

When interacting with our API via websocket, you must send ping frames every 30 seconds to keep the websocket connection alive.

- Ping / Pong frames are built into the websocket protocol and should be supported natively by your websocket library. SeePing/Pong framesfor more info.

Ping / Pong frames are built into the websocket protocol and should be supported natively by your websocket library. SeePing/Pong framesfor more info.

[Ping/Pong frames](https://datatracker.ietf.org/doc/html/rfc6455#section-5.5.2)
[Executes](/developer-resources/api/gateway/executes)
[Queries](/developer-resources/api/gateway/queries)
[PreviousEndpoints](/developer-resources/api/endpoints)
[NextExecutes](/developer-resources/api/gateway/executes)

Last updated1 month ago