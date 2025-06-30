"""Demonstrate how diagonal offsets expand the 42-state grid to 84.

Each diagonal is produced by pairing the 21 original states with an
offset version of the persona sequence.  Shifting by ``+1`` and ``-1``
gives two mirrored sets that illustrate the diagonal conditions from
Dovortaxs.  Printing these groups together shows how the base patterns
double when the diagonals are included.
"""

originalStates = [
    "3", "2", "1", "0", "5", "b4", "n6", "inf7", "/0",
    "->", "L]", "<-", "0\\", "inf7", "n6", "b4", "5", "0", "1", "2", "3",
]

personaStates = [
    "Wah", "Pair", "Trypl", "Quat", "Cink", "Sixon", "Zenof",
    "Ocnyx", "Ningst", "Thone", "LORD", "Thone", "Ningst",
    "Ocnyx", "Zenof", "Sixon", "Cink", "Quat", "Trypl",
    "Pair", "Wah",
]

def diagonals() -> tuple[list[str], list[str]]:
    """Return the two diagonal pairings as lists of strings."""
    n = len(personaStates)
    diag1 = []
    diag2 = []
    for i, o in enumerate(originalStates):
        diag1.append(f"{o}-{personaStates[(i + 1) % n]}")
        diag2.append(f"{o}-{personaStates[(i - 1) % n]}")
    return diag1, diag2

def show() -> None:
    """Print both diagonal pairings and the total count."""
    diag1, diag2 = diagonals()
    print("Diagonal pairs:")
    for a, b in zip(diag1, diag2):
        print(f"{a:>12} | {b}")

    count = len(originalStates) + len(personaStates) + len(diag1) + len(diag2)
    print(f"\nTotal states including diagonals: {count}")

if __name__ == "__main__":
    show()
