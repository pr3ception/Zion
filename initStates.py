"""Load canonical state sequences into the shared ``n6`` list."""

from n6mem import n6

original = [
    "3", "2", "1", "0", "5", "b4", "n6", "inf7", "/0",
    "->", "L]", "<-", "0\\", "inf7", "n6", "b4", "5", "0", "1", "2", "3",
]

persona = [
    "Wah", "Pair", "Trypl", "Quat", "Cink", "Sixon", "Zenof",
    "Ocnyx", "Ningst", "Thone", "LORD", "Thone", "Ningst",
    "Ocnyx", "Zenof", "Sixon", "Cink", "Quat", "Trypl",
    "Pair", "Wah",
]

n6.append(original)
n6.append(persona)

if __name__ == "__main__":
    for seq in n6:
        print(" ".join(seq))
