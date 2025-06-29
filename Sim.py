"""Combined simulations and vibergy example."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List


# --- Coil-bead simulation ----------------------------------------------------

@dataclass
class Coil:
    turns: int
    radius: float  # meters


@dataclass
class Bead:
    radius: float  # meters
    magneticField: float  # tesla at bead surface


def inducedVolt(coil: Coil, bead: Bead, velocity: float) -> float:
    """Estimate induced voltage for a bead moving over the coil."""
    area = math.pi * coil.radius ** 2
    bAtCoil = bead.magneticField
    fluxRate = bAtCoil * area * velocity / (2 * coil.radius)
    voltage = coil.turns * fluxRate
    return abs(voltage)


# --- Dual turbine simulation -------------------------------------------------

@dataclass
class Particle:
    angle: float
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
                    p.angle = -p.angle
                    p.phase = "fromCentre"

    def run(self, steps: int) -> None:
        for stepNum in range(steps):
            self.step()
            for i, p in enumerate(self.particles, start=1):
                print(f"Particle {i}: angle={p.angle:.2f}, radius={p.radius:.2f}, phase={p.phase}")
            print("-")


# --- Vibergy computation -----------------------------------------------------

def vibergy(waveform: List[float], fs: int, mass: float = 0.010) -> float:
    """Return energy in joules from a vibration sample."""
    if not waveform:
        return 0.0
    rms = math.sqrt(sum(x * x for x in waveform) / len(waveform))

    zeroCross = [i for i in range(1, len(waveform))
                 if waveform[i - 1] <= 0 < waveform[i]]
    if len(zeroCross) > 1:
        period = sum(zeroCross[i] - zeroCross[i - 1]
                      for i in range(1, len(zeroCross))) / (len(zeroCross) - 1)
        fPeak = fs / period
    else:
        fPeak = 0.0

    velocity = rms * 2 * math.pi * fPeak
    return 0.5 * mass * velocity ** 2


# --- Demo runner -------------------------------------------------------------

if __name__ == "__main__":
    print("Coil-bead simulation:")
    coil = Coil(turns=20, radius=0.015)
    bead = Bead(radius=0.0041, magneticField=0.03)
    v = inducedVolt(coil, bead, velocity=0.5)
    print(f"Induced voltage: {v:.3f} V\n")

    print("Dual turbine simulation:")
    sim = DualTurbine()
    sim.run(10)

    print("Vibergy example:")
    fs = 44100
    dur = 0.3
    tStep = 1 / fs
    t = [i * tStep for i in range(int(dur * fs))]
    tap = [0.1 * math.sin(2 * math.pi * 2000 * ti) for ti in t]
    energy = vibergy(tap, fs)
    print(f"vibergy \u2248 {energy*1e3:.2f} mJ")
