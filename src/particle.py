"""Particle Object Class."""
import numpy as np
import const.constants as const
import math


class Particle:
    """Particle class"""

    def __init__(self, x: float, y: float, vx: float, vy: float, size: float) -> None:
        """Initializes a particle to a numpy array."""
        self._arr = np.array([x, y, vx, vy, size], dtype=float)

    def update(self, com: dict[str, float]) -> None:
        distance = max(25.0, math.hypot(self.getX() - com["x"], self.getY() - com["y"]))
        force = const.GRAVITY * self.getSize() * com["total_mass"] / distance**2
        direction = math.atan2(com["y"] - self.getY(), com["x"] - self.getX())
        ax = force * math.cos(direction) / self.getSize()
        ay = force * math.sin(direction) / self.getSize()
        self.setVX(self.getVX() + ax)
        self.setVY(self.getVY() + ay)

    def getX(self) -> float:
        """Gets the x position of the particle."""
        return self._arr[0]

    def setX(self, x: float) -> None:
        """Sets the x position of the particle."""
        self._arr[0] = x

    def getY(self) -> float:
        """Gets the y position of the particle."""
        return self._arr[1]

    def setY(self, y: float) -> None:
        """Sets the y position of the particle."""
        self._arr[1] = y

    def getVX(self) -> float:
        """Gets the x velocity of the particle."""
        return self._arr[2]

    def setVX(self, vx: float) -> None:
        """Sets the x velocity of the particle."""
        self._arr[2] = vx

    def getVY(self) -> float:
        """Gets the y velocity of the particle."""
        return self._arr[3]

    def setVY(self, vy: float) -> None:
        """Sets the y velocity of the particle."""
        self._arr[3] = vy

    def getSize(self) -> float:
        """Gets the size of the particle."""
        return self._arr[4]

    def setSize(self, size: float) -> None:
        """Sets the size of the particle."""
        self._arr[4] = size
