"""Simple 2D airflow pattern from three fans facing the center."""

import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Fan:
    x: float
    y: float
    strength: float = 1.0

    def velocity(self, px: float, py: float) -> Tuple[float, float]:
        dx = px - self.x
        dy = py - self.y
        distSq = dx * dx + dy * dy
        if distSq == 0:
            return 0.0, 0.0
        inv = self.strength / distSq
        r = math.sqrt(distSq)
        return inv * dx / r, inv * dy / r


class FanField:
    def __init__(self, radius: float = 1.0) -> None:
        angles = [0.0, 2 * math.pi / 3, 4 * math.pi / 3]
        self.fans: List[Fan] = [Fan(math.cos(a) * radius, math.sin(a) * radius) for a in angles]

    def netVelocity(self, x: float, y: float) -> Tuple[float, float]:
        vx = vy = 0.0
        for fan in self.fans:
            dvx, dvy = fan.velocity(x, y)
            vx += dvx
            vy += dvy
        return vx, vy

    def sample(self, step: float = 0.5, extent: float = 1.5) -> None:
        y = extent
        while y >= -extent:
            row = []
            x = -extent
            while x <= extent:
                vx, vy = self.netVelocity(x, y)
                ang = math.atan2(vy, vx)
                arrow = self.dirChar(ang)
                row.append(arrow)
                x += step
            print(' '.join(row))
            y -= step

    @staticmethod
    def dirChar(angle: float) -> str:
        idx = int((angle + math.pi) / (2 * math.pi) * 8) % 8
        return "^>v<"[idx // 2] if idx % 2 == 0 else "*"


if __name__ == "__main__":
    field = FanField()
    field.sample()
