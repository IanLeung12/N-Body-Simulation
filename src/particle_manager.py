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

    def add_particle(self, particle: particle.Particle) -> None:
        """Adds a particle to the particle system.

        Args:
            particle (Particle): The particle to add to the system.

        """
        self.particles.append(particle)
        self.quadtree.insert(particle)

    def update_particles(self) -> None:
        """Updates the position of all particles in the system."""
        for i in range(len(self.particles)):
            particle = self.particles[i]
            for j in range(i + 1, len(self.particles)):
                other = self.particles[j]

                distance = max(particle.getSize(),
                               math.hypot(particle.getX() - other.getX(),
                                      particle.getY() - other.getY()))
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


