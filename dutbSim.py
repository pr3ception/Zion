"""Dual inverted turbine simulation.

This script models two particles travelling along mirrored diagonal paths
(diazanul) inside a simple repulsion-based mechanism. The path repeats through
phases: repulse from centre, travel along the rim, return to centre, and switch
to the opposite turbine.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List
import math


@dataclass
class Particle:
    angle: float  # radians around centre
    radius: float
    phase: str


class DualTurbine:
    def __init__(self, radius: float = 1.0, speed: float = 0.1) -> None:
        self.radius = radius
        self.speed = speed
        self.particles: List[Particle] = [
            Particle(angle=math.pi / 4, radius=0.0, phase="fromCentre"),
            Particle(angle=-3 * math.pi / 4, radius=0.0, phase="fromCentre"),
        ]

    def step(self) -> None:
        for p in self.particles:
            if p.phase == "fromCentre":
                p.radius += self.speed
                if p.radius >= self.radius:
                    p.radius = self.radius
                    p.phase = "aroundRim"
            elif p.phase == "aroundRim":
                p.angle += self.speed
                if p.angle >= math.pi * 3 / 4:
                    p.phase = "toCentre"
            elif p.phase == "toCentre":
                p.radius -= self.speed
                if p.radius <= 0:
                    p.radius = 0
                    p.angle = -p.angle  # switch to opposite diagonal
                    p.phase = "fromCentre"

    def run(self, steps: int) -> None:
        for stepNum in range(steps):
            self.step()
            for i, p in enumerate(self.particles, start=1):
                print(f"Particle {i}: angle={p.angle:.2f}, radius={p.radius:.2f}, phase={p.phase}")
            print("-")


if __name__ == "__main__":
    sim = DualTurbine()
    sim.run(20)
