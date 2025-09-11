from loguru import logger

class ParticleManager:
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def update_particles(self):
        for particle in self.particles:
            particle.update()

    def render_particles(self, screen):
        for particle in self.particles:
            particle.render(screen)