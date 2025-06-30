"""Show the 21 original states and the 21 persona states.

This script prints each sequence and demonstrates how they combine to
form a simple 42-state pattern matrix.
"""

ORIGINAL_STATES = [
    "3", "2", "1", "0", "5", "b4", "n6", "inf7", "/0",
    "->", "L]", "<-", "0\\", "inf7", "n6", "b4", "5", "0", "1", "2", "3",
]

PERSONA_STATES = [
    "Wah", "Pair", "Trypl", "Quat", "Cink", "Sixon", "Zenof",
    "Ocnyx", "Ningst", "Thone", "LORD", "Thone", "Ningst",
    "Ocnyx", "Zenof", "Sixon", "Cink", "Quat", "Trypl",
    "Pair", "Wah",
]

def printMatrix() -> None:
    print("Original states:")
    print(" ".join(ORIGINAL_STATES))
    print("\nPersona states:")
    print(" ".join(PERSONA_STATES))
    print("\nCombined pairs:")
    for o, p in zip(ORIGINAL_STATES, PERSONA_STATES):
        print(f"{o:>4} | {p}")

if __name__ == "__main__":
    printMatrix()
