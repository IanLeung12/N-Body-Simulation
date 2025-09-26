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

        comt = self.calculate_COM_totals()
        for particle in self.particles:
            pm = particle.getSize()
            com = {"x": (comt["total_x"] - pm * particle.getX()) / (comt["total_mass"] - pm),
                   "y": (comt["total_y"] - pm * particle.getY()) / (comt["total_mass"] - pm),
                   "total_mass": (comt["total_mass"] - pm)}
            particle.update(com)

    def calculate_COM_totals(self) -> dict[str, float]:
        """Calculates the sum of particles for center of mass calculation.

        Returns:
            dict[str, float]: {total_x, total_y, total_mass} of the particles
        """
        
        comt = {"total_x": 0.0, "total_y": 0.0, "total_mass": 0.0}
        if not self.particles:
            logger.warning("No particles to calculate center of mass.")
            return comt

        for p in self.particles:
            comt["total_mass"] += p.getSize()
            comt["total_x"] += p.getX() * p.getSize()
            comt["total_y"] += p.getY() * p.getSize()

        return comt
