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
        particle = Particle(random.randint(0, 1000), random.randint(0, 1000),
                            random.randint(-10, 10), random.randint(-10, 10), 
                            random.randint(2, 10))
        manager.add_particle(particle)
    renderer = Renderer(manager)
    renderer.run()

if __name__ == "__main__":
    main()
