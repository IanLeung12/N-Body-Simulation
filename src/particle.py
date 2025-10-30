"""Particle Object Class."""
import numpy as np


class Particle:
    """Particle class."""

    def __init__(self, x: float, y: float, size: float) -> None:
        """Initializes a particle to a numpy array."""
        ## x, y, size, vx, vy, forceX, forceY
        self._arr = np.array([x, y, size, 0.0, 0.0, 0.0, 0.0], dtype=float)

    def update(self) -> None:
        """Updates the particle's position based on its velocity and force."""
        ax = self.getForceX() / self.getSize()
        ay = self.getForceY() / self.getSize()
        self.setVX(self.getVX() + ax)
        self.setVY(self.getVY() + ay)
        self.setX(self.getX() + self.getVX())
        self.setY(self.getY() + self.getVY())
        # Reset forces after update
        self.setForceX(0.0)
        self.setForceY(0.0)

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

    def getSize(self) -> float:
        """Gets the size of the particle."""
        return self._arr[2]

    def setSize(self, size: float) -> None:
        """Sets the size of the particle."""
        self._arr[2] = size

    def getVX(self) -> float:
        """Gets the x velocity of the particle."""
        return self._arr[3]

    def setVX(self, vx: float) -> None:
        """Sets the x velocity of the particle."""
        self._arr[3] = vx

    def getVY(self) -> float:
        """Gets the y velocity of the particle."""
        return self._arr[4]

    def setVY(self, vy: float) -> None:
        """Sets the y velocity of the particle."""
        self._arr[4] = vy

    def getForceX(self) -> float:
        """Gets the X force of the particle."""
        return self._arr[5]

    def setForceX(self, force: float) -> None:
        """Sets the X force of the particle."""
        self._arr[5] = force

    def getForceY(self) -> float:
        """Gets the Y force of the particle."""
        return self._arr[6]

    def setForceY(self, force: float) -> None:
        """Sets the Y force of the particle."""
        self._arr[6] = force
