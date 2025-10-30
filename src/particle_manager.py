"""Manages the physics for the particles in the particle system."""
import math

import const.constants as const
import particle
import quadtree


class ParticleManager:
    """Manages the particles in the particle system."""

    def __init__(self) -> None:
        """Initializes particle manager and particle array."""
        self.particles = []
        self.quadtree = quadtree.Node((0, 0, 1000, 1000))
        self.rebuild_counter = 0

    def add_particle(self, particle: particle.Particle) -> None:
        """Adds a particle to the particle system.

        Args:
            particle (Particle): The particle to add to the system.

        """
        self.particles.append(particle)
        self.quadtree.insert(particle)

    def update_particles(self) -> None:
        """Updates the position of all particles in the system."""
        if self.rebuild_counter < const.REBUILD_RATE:
            self.rebuild_counter += 1
        else:
            self.rebuild_counter = 0
            self._build_quadtree()
            for particle in self.particles:
                self.quadtree.insert(particle)
        if const.BARNES_HUT:
            for particle in self.particles:
                fx, fy = self._calculate_forces(particle, self.quadtree, (0.0, 0.0))
                particle.setForceX(fx)
                particle.setForceY(fy)
                particle.update()
        else:
            for particle in self.particles:
                particle.setForceX(0)
                particle.setForceY(0)

            for i in range(len(self.particles)):
                particle = self.particles[i]
                self.quadtree.insert(particle)
                for j in range(i + 1, len(self.particles)):
                    other = self.particles[j]

                    distance = max(particle.getSize(),
                                math.hypot(particle.getX() - other.getX(),
                                        particle.getY() - other.getY()))
                    if distance < const.EPSILON:
                        particle.setX(particle.getX() + const.EPSILON)
                    fg = const.GRAVITY * particle.getSize() * other.getSize()
                    direction = math.atan2(other.getY() - particle.getY(),
                                        other.getX() - particle.getX())

                    particle.setForceX(particle.getForceX() +
                                    fg * math.cos(direction) / distance)
                    particle.setForceY(particle.getForceY() +
                                    fg * math.sin(direction) / distance)

                    other.setForceX(other.getForceX() -
                                    fg * math.cos(direction) / distance)
                    other.setForceY(other.getForceY() -
                                    fg * math.sin(direction) / distance)

                particle.update()

    def _build_quadtree(self) -> None:
        """Builds the quadtree for the current particles."""
        xs = [p.getX() for p in self.particles]
        ys = [p.getY() for p in self.particles]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # Make square, add padding
        cx = (min_x + max_x) / 2
        cy = (min_y + max_y) / 2
        half = max(max_x - min_x, max_y - min_y) / 2
        half = max(half, 1.0)
        padding = half * 0.1 + 10.0
        half += padding

        bbox = (cx - half, cy - half, cx + half, cy + half)
        self.quadtree = quadtree.Node(bbox, depth=0)

    def _calculate_forces(self, particle: particle.Particle,
                          node: quadtree.Node,
                          acc: tuple[float, float]) -> tuple[float, float]:
        """Calculates the net gravitational force on a particle from the quadtree.

        Args:
            particle (Particle): Particle to calculate forces for.
            node (Node): Current quadtree node.
            acc (tuple): Accumulated force in x and y directions.

        Returns:
        tuple: Net force in x and y directions.
        """
        if node is None:
            return acc

        else:
            if node.isLeaf():
                fx, fy = self._calculate_force(particle,
                                              node.particle.getX(),
                                              node.particle.getY(),
                                              node.particle.getSize())
                return acc[0] + fx, acc[1] + fy
            else:
                node_x, node_y = node.getCenter()
                distance = math.hypot(node_x - particle.getX(),
                                      node_y - particle.getY())
                if distance < const.EPSILON:
                    distance = const.EPSILON
                if node.getWidth() / distance < const.THETA:
                    com_x, com_y, com_m = node.getCOM()
                    fx, fy = self._calculate_force(particle, com_x, com_y, com_m)
                    return acc[0] + fx, acc[1] + fy
                else:
                    # Otherwise, check the children
                    for child in node.children:
                        acc = self._calculate_forces(particle, child, acc)
                    return acc

    def _calculate_force(self, p1: particle.Particle,
                         x: float,
                         y: float,
                         m: float) -> tuple[float, float]:
        """Calculates gravitational force between a particle and a mass point.

        Args:
            p1 (Particle): Particle to calculate force for.
            x (float): X position of the mass point.
            y (float): Y position of the mass point.
            m (float): Mass of the mass point.

        Returns:
            tuple: Force in x and y directions.
        """
        distance = math.hypot(p1.getX() - x, p1.getY() - y)
        if distance < const.EPSILON:
            return 0.0, 0.0

        fg = const.GRAVITY * p1.getSize() * m
        direction = math.atan2(y - p1.getY(), x - p1.getX())

        fx = fg * math.cos(direction) / distance
        fy = fg * math.sin(direction) / distance
        return fx, fy


