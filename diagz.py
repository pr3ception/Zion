"""Diagonal expansion of the 42-state grid to 84.

This script demonstrates one way the diagonal conditions in Dovortaxs
might double the base 42 patterns. It offsets the persona sequence
relative to the original states to form two diagonal pairings.
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

def diagonal(offset: int) -> list[str]:
    n = len(personaStates)
    return [f"{o}-{personaStates[(i+offset)%n]}" for i, o in enumerate(originalStates)]

def show() -> None:
    diag1 = diagonal(1)
    diag2 = diagonal(-1)
    print("Diagonal set 1:")
    print(" ".join(diag1))
    print("\nDiagonal set 2:")
    print(" ".join(diag2))
    count = len(originalStates) + len(personaStates) + len(diag1) + len(diag2)
    print(f"\nTotal states including diagonals: {count}")

if __name__ == "__main__":
    show()
