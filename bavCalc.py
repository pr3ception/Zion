"""Compute Bav and store it in the ``n6`` list.

Demonstrates the form::
    [B]av = mn(field(axis, state))

Avoid corrupted forms like ``<B>_avg`` or ``⟨B⟩_avg`` which misuse an
underscore.
"""

from typing import Iterable, Callable, Any, List

# In this simple form, `field` is a user-provided function
# that takes axis and state arguments and returns an iterable
# of numeric values.

n6: List[float] = []  # memory store for computed averages


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
