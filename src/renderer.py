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
        self.manager = manager
        self.window = pyglet.window.Window(caption="Particle System", 
                                           width=1000, height=1000)
        self.batch = pyglet.graphics.Batch()
        self.circles = [
            shapes.Circle(
                particle.getX(), particle.getY(), 
                particle.getSize(), color=(255, 255, 255), batch=self.batch
            )
            for particle in self.manager.particles
        ]

        self.com_circle = shapes.Circle(0, 0, 10, color=(255, 0, 0), batch=self.batch)

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
        self.manager.update_particles()
        com = self.manager.calculate_COM()
        x = max(0, min(self.window.width, com["x"]))
        y = max(0, min(self.window.height, com["y"]))
        self.com_circle.x = x
        self.com_circle.y = y

        for particle, circle in zip(self.manager.particles, self.circles):
            particle.setX(particle.getX() + particle.getVX() * dt)
            particle.setY(particle.getY() + particle.getVY() * dt)
            circle.x = particle.getX()
            circle.y = particle.getY()

    def run(self) -> None:
        """Runs the pyglet application."""
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()
