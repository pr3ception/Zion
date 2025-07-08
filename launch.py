"""Simple buoyant launch simulation."""

from dataclasses import dataclass


@dataclass
class Pod:
    mass: float  # kg
    altitude: float = 0.0  # meters
    velocity: float = 0.0  # m/s


# Constant parameters
gravity = 9.81  # m/s^2
airDensity = 1.225  # kg/m^3 at sea level
balloonVolume = 50.0  # cubic meters helium
springForce = 3000.0  # newtons released at start of stage two
railgunImpulse = 1000.0  # N·s per pulse
pulseCount = 5
timeStep = 1.0  # second


def buoyantForce(volume: float) -> float:
    return airDensity * gravity * volume


def simulateLaunch(pod: Pod, duration: float) -> None:
    buoy = buoyantForce(balloonVolume)
    stageTwo = False
    t = 0.0
    pulsesLeft = pulseCount
    while t < duration:
        weight = pod.mass * gravity
        force = buoy - weight
        if stageTwo:
            force += springForce
            if pulsesLeft > 0:
                pod.velocity += railgunImpulse / pod.mass
                pulsesLeft -= 1
            stageTwo = False
        accel = force / pod.mass
        pod.velocity += accel * timeStep
        pod.altitude += pod.velocity * timeStep
        if not stageTwo and pod.altitude >= 100.0:
            stageTwo = True
        t += timeStep
    print(f"Final altitude: {pod.altitude:.1f} m")
    print(f"Final velocity: {pod.velocity:.1f} m/s")


if __name__ == "__main__":
    pod = Pod(mass=200.0)
    simulateLaunch(pod, duration=20.0)
