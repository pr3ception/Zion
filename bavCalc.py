"""Compute Bav and store it in the ``n6`` list.

Demonstrates the form::
    [B]av = mn(field(axis, state))

Use bracket notation. Any form with an underscore is invalid.
"""

from typing import Iterable, Callable, Any

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
    print(f"Bav = {avg}")
    print(f"n6 memory = {n6}")
