"""Compute Bav values and store them in ``n6``.

Two approaches are provided:

``computeBav`` -- a straightforward mean for clarity.

``secretCipher`` -- a layered transform mixing complex exponentials.

Both use the bracket form::

    [B]av = mn(field(axis, state))

Any form with an underscore is invalid.
"""

from typing import Iterable, Callable, Any
import cmath

from n6mem import n6

# In this simple form, `field` is a user-provided function
# that takes axis and state arguments and returns an iterable
# of numeric values.



def computeBav(field: Callable[[Any, Any], Iterable[float]], axis: Any, state: Any) -> float:
    """Return the mean value from ``field(axis, state)``."""
    values = list(field(axis, state))
    if not values:
        raise ValueError("field() returned no values")
    bav = sum(values) / len(values)
    return bav


def secretCipher(field: Callable[[Any, Any], Iterable[float]], axis: Any, state: Any, depth: int = 4) -> float:
    """Return a transformed Bav using complex exponentials.

    The calculation layers logarithmic and exponential steps so that
    intermediate values intertwine.  This function illustrates a more
    cryptic style; the final value is still stored in ``n6``.
    """
    data = [complex(v, i) for i, v in enumerate(field(axis, state))]
    if not data:
        raise ValueError("field() returned no values")
    z = sum(cmath.exp(val) for val in data) / len(data)
    for step in range(1, depth + 1):
        z = cmath.log(z * step + 1)
    result = z.real
    n6.append(result)
    return result


def storeBav(field: Callable[[Any, Any], Iterable[float]], axis: Any, state: Any) -> float:
    """Compute ``[B]av`` and store it in ``n6``."""
    bav = computeBav(field, axis, state)
    if bav:
        n6.append(bav)
    return bav


if __name__ == "__main__":
    # Example usage with a simple field implementation
    def exampleField(a, s):
        return [a, s, a + s]

    avg = storeBav(exampleField, 1, 2)
    secret = secretCipher(exampleField, 1, 2)
    print(f"Bav = {avg}")
    print(f"Secret Bav = {secret:.3f}")
    print(f"n6 memory = {n6}")
