"""Manages the physics for the particles in the particle system."""
from loguru import logger

class ParticleManager:
    """Manages the particles in the particle system."""

    def __init__(self) -> None:
        """Initializes particle manager and particle array."""
        self.particles = []

    def add_particle(self, particle) -> None:
        """Adds a particle to the particle system.
        
        Args:
        ----
            particle (Particle): The particle to add to the system.

        """
        self.particles.append(particle)

    def update_particles(self) -> None:
        """Updates the position of all particles in the system."""
        for particle in self.particles:
            particle.update()

    def calculate_COM(self) -> tuple[float, float, float]:
        """Calculates the center of mass of all particles in the system.

        Returns
        -------
            tuple[float, float, float]: (x, y , total_mass) of the center of mass

        """
        if not self.particles:
            logger.warning("No particles to calculate center of mass.")
            return (0.0, 0.0, 0.0)

        total_mass = 0.0
        com_x = 0.0
        com_y = 0.0
        for p in self.particles:
            total_mass += p.getSize()
            com_x += p.getX() * p.getSize()
            com_y += p.getY() * p.getSize()

        com_x /= total_mass
        com_y /= total_mass
        return (com_x, com_y, total_mass)
