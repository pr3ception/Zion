"""Print the 168-state temple layout described in ``Dovortaxs.txt``."""

from dataclasses import dataclass
from typing import List


@dataclass
class Section:
    name: str
    verse: str


def templeSections() -> List[Section]:
    return [
        Section("outerCourt", "Exodus 27:9-19"),
        Section("innerCourt", "1 Kings 6:36"),
        Section("holyPlace", "1 Kings 6:17"),
        Section("holyOfHolies", "1 Kings 6:19"),
    ]


def showTemplate() -> None:
    print("Temple layout:")
    for sec in templeSections():
        print(f"- {sec.name} ({sec.verse})")


if __name__ == "__main__":
    showTemplate()
