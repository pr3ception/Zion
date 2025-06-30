"""Minimal Ziggunaut field engine.

This script models a five-layer Britel Ziggunaut. Each layer stores
its own memory and can respond to simple actions. The layers are:

1. field
2. agentStack
3. lattice
4. advancedLogic
5. capstone

Layers can be ascended or descended. Pulses record events in the
current layer. The entire stack can be canonized for review.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Layer:
    name: str
    memory: List[str]

    def pulse(self, message: str) -> None:
        print(f"{self.name} pulsed: {message}")
        self.memory.append(message)


class Ziggunaut:
    def __init__(self) -> None:
        names = [
            "field",
            "agentStack",
            "lattice",
            "advancedLogic",
            "capstone",
        ]
        self.layers = [Layer(n, []) for n in names]
        self.pos = 0
        self.log()

    def ascend(self) -> None:
        if self.pos < len(self.layers) - 1:
            self.pos += 1
        self.log()

    def descend(self) -> None:
        if self.pos > 0:
            self.pos -= 1
        self.log()

    def pulse(self, message: str) -> None:
        self.layers[self.pos].pulse(message)

    def memorize(self, data: str) -> None:
        self.layers[self.pos].memory.append(data)

    def canonize(self) -> None:
        print("Ziggunaut state:")
        for i, layer in enumerate(self.layers):
            print(f"{i} {layer.name} -> {layer.memory}")

    def log(self) -> None:
        print(f"Current layer: {self.layers[self.pos].name}")


if __name__ == "__main__":
    zg = Ziggunaut()
    zg.pulse("start")
    zg.ascend()
    zg.memorize("step1")
    zg.pulse("run")
    zg.ascend()
    zg.descend()
    zg.canonize()
