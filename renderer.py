"""Renders the particles in the particle system using pyglet."""
import pyglet
from pyglet import shapes
from particle_manager import ParticleManager

class Renderer:
    """Class to render the particles."""

    def __init__(self, manager: ParticleManager) -> None:
        """Initializes the renderer, window, and particles.
        
        Args:
        ----
            manager (ParticleManager): The particle manager to get particles from.

        """
        self.particles = manager.particles
        self.window = pyglet.window.Window(caption="Particle System", 
                                           width=1000, height=1000)
        self.batch = pyglet.graphics.Batch()
        self.circles = [
            shapes.Circle(
                particle.getX(), particle.getY(), 
                particle.getSize(), color=(255, 255, 255), batch=self.batch
            )
            for particle in self.particles
        ]

        @self.window.event
        def on_draw() -> None:
            self.window.clear()
            self.batch.draw()

    def update(self, dt: float) -> None:
        """Updates the position of all particles in the system.
        
        Args:
        ----
            dt (float): Delta time.

        """
        for particle, circle in zip(self.particles, self.circles):
            particle.setX(particle.getX() + particle.getVX() * dt)
            particle.setY(particle.getY() + particle.getVY() * dt)
            circle.x = particle.getX()
            circle.y = particle.getY()

    def run(self) -> None:
        """Runs the pyglet application."""
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()
