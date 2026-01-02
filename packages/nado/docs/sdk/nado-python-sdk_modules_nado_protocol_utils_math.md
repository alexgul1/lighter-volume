---
url: https://nadohq.github.io/nado-python-sdk/_modules/nado_protocol/utils/math.html
---

# Source code for nado_protocol.utils.math

```python

from decimal import Decimal
from typing import Union

[docs]def to_pow_10(x: int, pow: int) -> int:
    """
    Converts integer to power of 10 format.

    Args:
        x (int): Integer value.

        pow (int): Power of 10.

    Returns:
        int: Converted value.
    """
    return x * 10**pow

[docs]def to_x6(x: float) -> int:
    """
    Converts a float to a fixed point of 1e6.

    Args:
        x (float): Float value to convert.

    Returns:
        int: Fixed point value represented as an integer.
    """
    return int(Decimal(str(x)) * Decimal(10**6))

[docs]def to_x18(x: float) -> int:
    """
    Converts a float to a fixed point of 1e18.

    Args:
        x (float): Float value to convert.

    Returns:
        int: Fixed point value represented as an integer.
    """
    return int(Decimal(str(x)) * Decimal(10**18))

[docs]def from_pow_10(x: int, pow: int) -> float:
    """
    Reverts integer from power of 10 format.

    Args:
        x (int): Converted value.

        pow (int): Power of 10.

    Returns:
        float: Original value.
    """
    return float(x) / 10**pow

[docs]def from_x6(x: int) -> float:
    """
    Reverts integer from power of 10^6 format.

    Args:
        x (int): Converted value.

    Returns:
        float: Original value.
    """
    return from_pow_10(x, 6)

[docs]def from_x18(x: int) -> float:
    """
    Reverts integer from power of 10^18 format.

    Args:
        x (int): Converted value.

    Returns:
        float: Original value.
    """
    return from_pow_10(x, 18)

def mul_x18(x: Union[float, str], y: Union[float, str]) -> int:
    return int(Decimal(str(x)) * Decimal(str(y)) / Decimal(10**18))

def round_x18(x: Union[int, str], y: Union[str, int]) -> int:
    x, y = int(x), int(y)
    return x - x % y

```