---
url: https://docs.nado.xyz/developer-resources/api/subscriptions/authentication
title: Authentication
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Subscriptions
[Subscriptions](/developer-resources/api/subscriptions)

# Authentication

Access Nado's authenticated streams.

### Rate limits

Asingle wallet addresscan be authenticated by up to 5 websocket connections, regardless of the originating IP address. Connections exceeding these limits will be automatically disconnected.

Seerate limitsfor more details.

[rate limits](/developer-resources/api/subscriptions/rate-limits)

### Request

To access streams that require authentication, submit a request with themethodfield set toauthenticate.

`method`
`authenticate`

Connect

WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]

`WEBSOCKET [SUBSCRIPTIONS_ENDPOINT]`

Message

```
{
  "method": "authenticate",
  "id": 0,
  "tx": {
    "sender": "0x...",
    "expiration": "1..."
  },
  "signature": "0x..."
}
```

### Request Parameters

method

string

Yes

authenticate

`authenticate`

id

number

Yes

Can be set to any positive integer. Can be used to identify the websocket request / response.

tx

object

Yes

StreamAuthenticationobject that needs to be signed. SeeSigningsection for more details.

`StreamAuthentication`
[Signing](/developer-resources/api/subscriptions/authentication#signing)

tx.sender

string

Yes

A hex string representing abytes32of a specific subaccount.

`bytes32`

tx.expiration

string

Yes

Represents the expiration time in milliseconds since the Unix epoch.

signature

string

Yes

Hex string representing hash of thesignedStreamAuthenticationobject.SeeSigningsection for more details.

`StreamAuthentication`
[Signing](/developer-resources/api/subscriptions/authentication#signing)

Notes:

- Althoughsenderspecifies a specific subaccount, authentication applies to the entire wallet address, enabling access to authenticated streams for different subaccounts under that address.

Althoughsenderspecifies a specific subaccount, authentication applies to the entire wallet address, enabling access to authenticated streams for different subaccounts under that address.

- Once authenticated, the authentication status of that websocket connection cannot be changed and stays for the duration of the connection.

Once authenticated, the authentication status of that websocket connection cannot be changed and stays for the duration of the connection.

## Signing

See more details and examples in oursigningpage.

[signing](/developer-resources/api/gateway/signing)

The typed data struct that needs to be signed is:

sender: A hex string representing abytes32of a specific subaccount. The signature must be signed by the wallet address specified by sender.

`sender`
`bytes32`

expiration: Represents the expiration time in milliseconds since the Unix epoch. Requests will be denied if the expiration is either smaller than the current time or more than 100 seconds ahead of it.

`expiration`

Notes:

- Should use the endpoint address asverifyingContract.

Should use the endpoint address asverifyingContract.

`verifyingContract`
- For signing, you should always use the data type specified in the typed data struct which might be different from the type sent in the request e.g:expirationshould be anuint64forSigningbut should be sent as astringin the final payload.

For signing, you should always use the data type specified in the typed data struct which might be different from the type sent in the request e.g:expirationshould be anuint64forSigningbut should be sent as astringin the final payload.

`expiration`
`uint64`
`string`

### Response

[PreviousSubscriptions](/developer-resources/api/subscriptions)
[NextStreams](/developer-resources/api/subscriptions/streams)

Last updated1 month ago