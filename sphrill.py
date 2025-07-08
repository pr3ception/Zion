"""Estimate laser energy to drill a hole in a neodymium sphere."""

from dataclasses import dataclass
import math


@dataclass
class NeoSphere:
    radius: float  # meters
    density: float = 7240.0  # kg/m^3 for NdFeB
    meltTemp: float = 1297.0  # K
    boilTemp: float = 3347.0  # K
    specHeat: float = 200.0   # J/(kg·K) rough average
    latentMelt: float = 120e3  # J/kg
    latentVapor: float = 2800e3  # J/kg


def holeEnergy(sphere: NeoSphere, holeRadius: float) -> float:
    """Return joules needed to vaporize a cylindrical hole through the sphere."""
    if holeRadius <= 0 or holeRadius >= sphere.radius:
        raise ValueError("holeRadius must be between 0 and sphere radius")
    vol = math.pi * holeRadius ** 2 * (2 * sphere.radius)
    mass = vol * sphere.density
    heatToMelt = sphere.specHeat * (sphere.meltTemp - 300) * mass
    melt = sphere.latentMelt * mass
    heatToBoil = sphere.specHeat * (sphere.boilTemp - sphere.meltTemp) * mass
    vapor = sphere.latentVapor * mass
    return heatToMelt + melt + heatToBoil + vapor


if __name__ == "__main__":
    nd = NeoSphere(radius=0.016)  # 0.63" radius
    energy = holeEnergy(nd, holeRadius=0.001)
    print(f"Energy to drill: {energy/1000:.1f} kJ")
