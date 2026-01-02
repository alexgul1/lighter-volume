---
url: https://docs.nado.xyz/developer-resources/api/subscriptions
title: Subscriptions
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Subscriptions

Allows to subscribe to a number of live data feeds to receive real-time trading updates from Nado.

## Overview

To interact with the subscription API, send websocket messages toWEBSOCKET [SUBSCRIPTIONS_ENDPOINT].

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Subscription connections must set theSec-WebSocket-Extensionsheader to includepermessage-deflate.

`Sec-WebSocket-Extensions`
`permessage-deflate`

## Endpoints

### Testnet:

- wss://gateway.test.nado.xyz/v1/subscribe

wss://gateway.test.nado.xyz/v1/subscribe

`wss://gateway.test.nado.xyz/v1/subscribe`

Note: You must send ping frames every 30 seconds to keep the websocket connection alive.

[Authentication](/developer-resources/api/subscriptions/authentication)
[Streams](/developer-resources/api/subscriptions/streams)
[Events](/developer-resources/api/subscriptions/events)
[Rate limits](/developer-resources/api/subscriptions/rate-limits)
[PreviousQ&A](/developer-resources/api/gateway/signing/q-and-a)
[NextAuthentication](/developer-resources/api/subscriptions/authentication)

Last updated1 month ago