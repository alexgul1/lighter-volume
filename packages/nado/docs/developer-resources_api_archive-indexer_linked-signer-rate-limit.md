---
url: https://docs.nado.xyz/developer-resources/api/archive-indexer/linked-signer-rate-limit
title: Linked Signer Rate Limit
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Archive (indexer)
[Archive (indexer)](/developer-resources/api/archive-indexer)

# Linked Signer Rate Limit

Query current linked signer and rate limit usage for a provided subaccount.

A subaccount can perform a max of 50LinkSignerrequests in 7 days. Use this query to check current usage and wait time.

[LinkSigner](/developer-resources/api/gateway/executes/link-signer)

## Rate limits

- 1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

1200 requests/min or 200 requests/10secs per IP address. (weight = 2)

See more details inAPI Rate limits

[API Rate limits](/developer-resources/api/rate-limits)

## Request

Queries a subaccount's linked signer rate limits.

POST [ARCHIVE_ENDPOINT]

`POST [ARCHIVE_ENDPOINT]`

Body

```
{
  "linked_signer_rate_limit": {
    "subaccount": "0x9b9989a4E0b260B84a5f367d636298a8bfFb7a9b42544353504f540000000000"
  }
}
```

## Response

```
{
  "remaining_tx": "50",
  "wait_time": 0,
  "signer": "0x0000000000000000000000000000000000000000",
  "total_tx_limit": "50"
}
```

Notes:

- remaining_tx: keeps track of the remainingLinkSignerexecutes that can be performed.

remaining_tx: keeps track of the remainingLinkSignerexecutes that can be performed.

`remaining_tx`
`LinkSigner`
- total_tx_limit: that max weekly tx limit.

total_tx_limit: that max weekly tx limit.

`total_tx_limit`
- wait_time: the total seconds you need to wait before performing anotherLinkSignerexecute. Can only perform another request whenwait_timeis0.

wait_time: the total seconds you need to wait before performing anotherLinkSignerexecute. Can only perform another request whenwait_timeis0.

`wait_time`
`LinkSigner`
`wait_time`
`0`
- signer: the current linked signer address (20 bytes) associated to the providedsubaccount. It returns the zero address when no signer is linked.

signer: the current linked signer address (20 bytes) associated to the providedsubaccount. It returns the zero address when no signer is linked.

`signer`
`subaccount`
[PreviousLinked Signers](/developer-resources/api/archive-indexer/linked-signers)
[NextIsolated Subaccounts](/developer-resources/api/archive-indexer/isolated-subaccounts)

Last updated23 days ago