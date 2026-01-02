---
url: https://nadohq.github.io/nado-python-sdk/_modules/nado_protocol/engine_client/types/stream.html
---

# Source code for nado_protocol.engine_client.types.stream

```python

from nado_protocol.engine_client.types.execute import SignatureParams

[docs]class StreamAuthenticationParams(SignatureParams):
    sender: str
    expiration: int

```