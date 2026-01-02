---
url: https://nadohq.github.io/nado-python-sdk/_modules/nado_protocol/client/apis/perp.html
---

# Source code for nado_protocol.client.apis.perp

```python

from nado_protocol.client.apis.perp.query import PerpQueryAPI

[docs]class PerpAPI(PerpQueryAPI):
    """
    A unified interface for Perpetual (Perp) operations in the Nado Protocol.

    This class extends functionalities from PerpQueryAPI into a single interface, providing a simpler and more consistent way to perform Perp operations.
    Currently, it allows for querying (data retrieval) operations for Perp products.

    Inheritance:
        PerpQueryAPI: This provides functionalities to retrieve various kinds of information related to Perp products.
        These include operations like retrieving the latest index and mark price for a specific Perp product.

    Attributes and Methods: Inherited from PerpQueryAPI.
    """

    pass

```