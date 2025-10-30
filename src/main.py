"""Main module to run particle simulation."""

import random

import const.constants as const
from particle import Particle
from particle_manager import ParticleManager
from renderer import Renderer


def main() -> None:
    """Begins particle simulation."""
    manager = ParticleManager()
    used_posns = set()
    for _ in range(const.PARTICLES):
        while True:
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            if (x, y) not in used_posns:
                used_posns.add((x, y))
                particle = Particle(x, y,
                                    random.randint(const.MIN_SIZE, const.MAX_SIZE))
                manager.add_particle(particle)
                break
    renderer = Renderer(manager)
    renderer.run()

if __name__ == "__main__":
    main()
