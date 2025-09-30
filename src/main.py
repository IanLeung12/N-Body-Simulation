"""Main module to run particle simulation."""

from particle_manager import ParticleManager
from particle import Particle
from renderer import Renderer
import const.constants as const
import random

def main():
    """Begins particle simulation."""
    manager = ParticleManager()
    for i in range(const.PARTICLES):
        particle = Particle(random.randint(400, 800), random.randint(400, 800),
                            0, 0,
                            random.randint(const.MIN_SIZE, const.MAX_SIZE))
        manager.add_particle(particle)
    renderer = Renderer(manager)
    renderer.run()

if __name__ == "__main__":
    main()
