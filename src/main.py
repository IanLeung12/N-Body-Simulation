"""Main module to run particle simulation."""

import random

import const.constants as const
from particle import Particle
from particle_manager import ParticleManager
from renderer import Renderer


def main() -> None:
    """Begins particle simulation."""
    manager = ParticleManager()
    for _ in range(const.PARTICLES):
        particle = Particle(random.randint(495, 505), random.randint(495, 505),
                            random.randint(const.MIN_SIZE, const.MAX_SIZE))
        manager.add_particle(particle)
    renderer = Renderer(manager)
    renderer.run()

if __name__ == "__main__":
    main()
