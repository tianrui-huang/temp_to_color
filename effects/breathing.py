# effects/breathing.py

import math


class Breathing:
    def __init__(
        self,
        period: float = 3.0,
        min_brightness: float = 0.3,
        max_brightness: float = 1.0,
    ):
        self.period = period
        self.min = min_brightness
        self.max = max_brightness
        self.t = 0.0

    def update(self, dt: float) -> float:
        """返回当前帧亮度（0~1）"""

        self.t += dt

        phase = (math.sin(self.t / self.period * math.tau) + 1) / 2

        return self.min + (self.max - self.min) * phase