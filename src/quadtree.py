"""QuadTree node for barnes-hut algorithm."""
from __future__ import annotations

from particle import Particle


class Node:
    """A node in the quadtree."""
    particle: Particle | None = None
    children: list[Node | None] | None = None

    def __init__(self, bbox: tuple) -> None:
        """Initialize Node.

        Args:
            bbox (tuple): Bounding box of the node (x_min, y_min, x_max, y_max).
        """
        self.bbox = bbox

    def insert(self, particle: Particle) -> Node:
        """Insert Particle.

        Args:
            particle (Particle): Particle to insert.
        """
        if self.particle is None:
            self.particle = particle
            return self

        elif self.children is None:
            self.children = [None] * 4

        # Insert old particle into inner node
        quadrant = self.getQuadrant(self.particle)
        if self.children[quadrant] is None:
            self.children[quadrant] = Node(self.createBBox(quadrant))
        self.children[quadrant].insert(self.particle)
        self.particle = None

        # Insert new particle into inner node
        quadrant = self.getQuadrant(particle)
        if self.children[quadrant] is None:
            self.children[quadrant] = Node(self.createBBox(quadrant))
        self.children[quadrant].insert(particle)
        return self

    def collectBoxes(self) -> list[tuple]:
        """Collect bounding boxes of all nodes in the quadtree."""
        boxes = [self.bbox]
        if self.children is not None:
            for child in self.children:
                if child is not None:
                    boxes.extend(child.collectBoxes())
        return boxes

    def createBBox(self, quadrant: int) -> tuple:
        """Creates a bounding box a quadrant in the node.

        Args:
            quadrant (int): Quadrant index (0: top-left, 1: top-right,
                            2: bottom-left, 3: bottom-right).

        Returns:
            tuple: Bounding box of the specified quadrant.
        """
        mid_x = (self.bbox[0] + self.bbox[2]) / 2
        mid_y = (self.bbox[1] + self.bbox[3]) / 2
        if quadrant == 0:  # Top-left
            return (self.bbox[0], self.bbox[1], mid_x, mid_y)
        elif quadrant == 1:  # Top-right
            return (mid_x, self.bbox[1], self.bbox[2], mid_y)
        elif quadrant == 2:  # Bottom-left
            return (self.bbox[0], mid_y, mid_x, self.bbox[3])
        else:  # Bottom-right
            return (mid_x, mid_y, self.bbox[2], self.bbox[3])

    def getQuadrant(self, particle: Particle) -> int:
        """Determines which quadrant a particle belongs to.

        Args:
            particle (Particle): Particle to check.

        Returns:
            int: Quadrant index (0: top-left, 1: top-right,
        2: bottom-left, 3: bottom-right).
        """
        mid_x = (self.bbox[0] + self.bbox[2]) / 2
        mid_y = (self.bbox[1] + self.bbox[3]) / 2
        if particle.getX() < mid_x:
            if particle.getY() < mid_y:
                return 0  # Top-left
            else:
                return 2  # Bottom-left
        else:
            if particle.getY() < mid_y:
                return 1  # Top-right
            else:
                return 3  # Bottom-right


