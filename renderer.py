import time
import pyglet
from loguru import logger

class Renderer:

    def __init__(self, particles: list) -> None:
        self.particles = particles
        self.window = pyglet.window.Window("Particle System")
        self.batch = pyglet.graphics.Batch()

        @self.window.event
        def on_draw():
            self.window.clear()
            self.batch.draw()

    def update(self, dt):
        for particle in self.particles:
            particle.x += particle.vx * dt
            particle.y += particle.vy * dt
            # Update particle position in the batch if necessary
            
    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        pyglet.app.run()

