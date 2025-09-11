import numpy as np
from loguru import logger

class Particle:
    def __init__(self, x: float, y: float, vx: float, vy: float, size: float) -> None:
        self._arr = np.array([x, y, vx, vy, size], dtype=float)
    
    def getX(self) -> float:
        return self._arr[0]
    
    def setX(self, x: float) -> None:
        self._arr[0] = x
    
    def getY(self) -> float:
        return self._arr[1]
    
    def setY(self, y: float) -> None:
        self._arr[1] = y
    
    def getVX(self) -> float:
        return self._arr[2]

    def setVX(self, vx: float) -> None:
        self._arr[2] = vx

    def getVY(self) -> float:
        return self._arr[3]

    def setVY(self, vy: float) -> None:
        self._arr[3] = vy

    def getSize(self) -> float:
        return self._arr[4]

    def setSize(self, size: float) -> None:
        self._arr[4] = size
