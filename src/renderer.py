"""Renders the particles in the particle system using pyglet."""
import random

import pyglet
from particle_manager import ParticleManager
from pyglet import shapes


class Renderer:
    """Class to render the particles."""

    def __init__(self, manager: ParticleManager) -> None:
        """Initializes the renderer, window, and particles.

        Args:
            manager (ParticleManager): The particle manager to get particles from.

        """
        self.manager = manager
        self.window = pyglet.window.Window(caption="Particle System",
                                           width=1000, height=1000)
        self.batch = pyglet.graphics.Batch()
        self.quadtree = self.manager.quadtree
        self.bboxes = self.quadtree.collectBoxes()
        self.rectangles = [
            shapes.BorderedRectangle(
                bbox[0],
                bbox[1],
                bbox[2] - bbox[0],
                bbox[3] - bbox[1],
                border=1,
                color=(0, 0, 0),
                border_color=(255, 0, 0),
                batch=self.batch
            )
            for bbox in self.bboxes
        ]
        self.circles = [
            shapes.Circle(
                particle.getX(),
                particle.getY(),
                particle.getSize(),
                color=(random.randint(100, 255),
                       random.randint(100, 255),
                       random.randint(100, 255)),
                batch=self.batch
            )
            for particle in self.manager.particles
        ]


        @self.window.event
        def on_draw() -> None:
            self.window.clear()
            self.batch.draw()

    def update(self, dt: float) -> None:
        """Updates the position of all particles in the system.

        Args:
            dt (float): Delta time.

        """
        self.manager.update_particles()

        for particle, circle in zip(self.manager.particles, self.circles):
            particle.setX(particle.getX() + particle.getVX() * dt)
            particle.setY(particle.getY() + particle.getVY() * dt)
            circle.x = particle.getX()
            circle.y = particle.getY()

    def run(self) -> None:
        """Runs the pyglet application."""
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()
