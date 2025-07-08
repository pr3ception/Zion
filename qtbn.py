"""Quatbine dual ring simulation.

This script models inner and outer rings spinning in opposite directions.
Each ring holds items distributed evenly around its circumference.
Running the simulation prints the coordinates of each item over time.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple
import math


@dataclass
class Ring:
    radius: float
    itemCount: int
    clockwise: bool
    angle: float = 0.0

    def step(self, amount: float) -> None:
        if self.clockwise:
            self.angle += amount
        else:
            self.angle -= amount

    def positions(self) -> List[Tuple[float, float]]:
        result = []
        for i in range(self.itemCount):
            theta = self.angle + 2 * math.pi * i / self.itemCount
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            result.append((x, y))
        return result


class Qtbn:
    def __init__(self, outerRadius: float = 1.0, innerRadius: float = 0.6, speed: float = 0.1) -> None:
        self.outer = Ring(radius=outerRadius, itemCount=8, clockwise=True)
        self.inner = Ring(radius=innerRadius, itemCount=6, clockwise=False)
        self.speed = speed

    def step(self) -> None:
        self.outer.step(self.speed)
        self.inner.step(self.speed)

    def run(self, steps: int) -> None:
        for stepNum in range(steps):
            self.step()
            outerPos = self.outer.positions()
            innerPos = self.inner.positions()
            print("Outer ring:")
            for x, y in outerPos:
                print(f"  ({x:.2f}, {y:.2f})")
            print("Inner ring:")
            for x, y in innerPos:
                print(f"  ({x:.2f}, {y:.2f})")
            print("-")


if __name__ == "__main__":
    sim = Qtbn()
    sim.run(5)
