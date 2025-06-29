"""Simple coil-bead optical generator simulation.

This script estimates the voltage produced when a magnetic bead moves near
coils taped to a phone case or similar surface. The model is intentionally
simplified but demonstrates how mechanical motion can induce a voltage.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Coil:
    turns: int
    radius: float  # meters


@dataclass
class Bead:
    radius: float  # meters
    magneticField: float  # tesla at bead surface


def inducedVolt(coil: Coil, bead: Bead, velocity: float) -> float:
    """Return estimated induced voltage for a bead moving over the coil.

    The model assumes the bead passes directly over the coil centre and the
    magnetic field decays with distance cubed. The coil is treated as a
    single loop with area ``pi * radius**2``.
    """
    area = math.pi * coil.radius ** 2
    # approximate field at coil location from bead dipole
    # B = B0 * (bead.radius / distance)**3. assume distance approx bead.radius
    bAtCoil = bead.magneticField * (bead.radius / bead.radius) ** 3
    # Faraday's law: V = -N * dPhi/dt, with flux Phi = B * A.
    # Assume d/dt from bead velocity across coil diameter
    fluxRate = bAtCoil * area * velocity / (2 * coil.radius)
    voltage = coil.turns * fluxRate
    return abs(voltage)


if __name__ == "__main__":
    # Example: 2 taped coils with a 1.26" bead moving at 0.5 m/s
    coil = Coil(turns=20, radius=0.015)  # roughly phone coil size
    bead = Bead(radius=0.016, magneticField=0.03)  # 0.03 T at surface
    v = inducedVolt(coil, bead, velocity=0.5)
    print(f"Induced voltage: {v:.3f} V")
