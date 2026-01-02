---
url: https://docs.nado.xyz/developer-resources/api/gateway/signing/examples
title: Examples
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)
- Gateway
[Gateway](/developer-resources/api/gateway)
- Signing
[Signing](/developer-resources/api/gateway/signing)

# Examples

Nado executes EIP712 typed data examples

The following are full examples of EIP12 typed data for each of Nado's executes. Each execute includes asenderfield which is a soliditybytes32. There are two components to this field:

`sender`
`bytes32`
- anaddressthat is abytes20

anaddressthat is abytes20

`address`
`bytes20`
- a subaccount identifier that is abytes12

a subaccount identifier that is abytes12

`bytes12`

For example, if your address was0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43, and you wanted to use the default subaccount identifier (i.e: an empty identifier"") you can setsenderto0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000, which sets all bytes of the subaccount identifier to0.

`0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43`
`""`
`sender`
`0x7a5ec2748e9065794491a8d29dcf3f9edb8d7c43000000000000000000000000`
`0`

Note: abytes32representation of the sender must used when signing the request.

`bytes32`

See below a sample util to convert a hex to abytes32:

```
def hex_to_bytes32(hex_string):
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]
    data_bytes = bytes.fromhex(hex_string)
    padded_data = data_bytes + b"\x00" * (32 - len(data_bytes))
    return padded_data

sender = hex_to_bytes32('0x841fe4876763357975d60da128d8a54bb045d76a64656661756c740000000000')
```

```
import { arrayify } from 'ethers/lib/utils';

export function hexToBytes32(subaccount: string) {
  const subaccountBytes = arrayify(subaccount);
  const bytes32 = new Uint8Array(32);
  for (let i = 0; i < Math.min(subaccountBytes.length, 32); i++) {
    bytes32[i] = subaccountBytes[i];
  }
  return bytes32;
}

const sender = hexToBytes32('0x841fe4876763357975d60da128d8a54bb045d76a64656661756c740000000000')
```

## EIP712 Typed data examples

```
{
    'types': {
        'EIP712Domain': [
            {'name': 'name', 'type': 'string'},
            {'name': 'version', 'type': 'string'},
            {'name': 'chainId', 'type': 'uint256'},
            {'name': 'verifyingContract', 'type': 'address'}
        ],
        'Order': [
            {'name': 'sender', 'type': 'bytes32'},
            {'name': 'priceX18', 'type': 'int128'},
            {'name': 'amount', 'type': 'int128'},
            {'name': 'expiration', 'type': 'uint64'},
            {'name': 'nonce', 'type': 'uint64'},
            {'name': 'appendix', 'type': 'uint128'},
        ],
    },
    'primaryType': 'Order',
    'domain': {
        'name': 'Nado',
        'version': '0.0.1',
        'chainId': 763373,  
        'verifyingContract': '0x0000000000000000000000000000000000000001'
    },
    'message': {
        'sender': hex_to_bytes32('0x841fe4876763357975d60da128d8a54bb045d76a64656661756c740000000000'),
        'priceX18': 28898000000000000000000,
        'amount': -10000000000000000,
        'expiration': 4611687701117784255,
        'appendix': 1537,  # Version 1, POST_ONLY order
        'nonce': 1764428860167815857,
    },
}
```

[PreviousSigning](/developer-resources/api/gateway/signing)
[NextQ&A](/developer-resources/api/gateway/signing/q-and-a)

Last updated9 days ago