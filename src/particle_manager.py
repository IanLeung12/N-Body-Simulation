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

        com = self.calculate_COM()
        for particle in self.particles:
            particle.update(com)

    def calculate_COM(self) -> dict[str, float]:
        """Calculates the center of mass of all particles in the system.

        Returns
        -------
            dict[str, float]: {"x": x, "y": y, "total_mass": total_mass} of the center of mass
        """

        return {"x": 500.0, "y": 500.0, "total_mass": 100.0}
        com = {"x": 0.0, "y": 0.0, "total_mass": 0.0}
        if not self.particles:
            logger.warning("No particles to calculate center of mass.")
            return com

        for p in self.particles:
            com["total_mass"] += p.getSize()
            com["x"] += p.getX() * p.getSize()
            com["y"] += p.getY() * p.getSize()

        com["x"] /= com["total_mass"]
        com["y"] /= com["total_mass"]
        return com
