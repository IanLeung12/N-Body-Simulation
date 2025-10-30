"""Renders the particles in the particle system using pyglet."""
import random

import const.constants as const
import pyglet
from particle_manager import ParticleManager
from pyglet import gl, shapes
from pyglet import math as pyg_math


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
        if const.SHOW_QUADTREE:
            bboxes = self.quadtree.collectBoxes()
            self.rectangles = [
                shapes.BorderedRectangle(
                    bbox[0],
                    bbox[1],
                    bbox[2] - bbox[0],
                    bbox[3] - bbox[1],
                    border=2,
                    color=(0, 0, 0),
                    border_color=(255, 0, 0),
                    batch=self.batch
                )
                for bbox in bboxes
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
            if const.FIT_TREE and self.manager.quadtree is not None:
                # Fit to current quadtree root each frame
                self._set_projection_to_bbox(self.manager.quadtree.bbox, margin=0.05)
            self.batch.draw()

    def _set_projection_to_bbox(self,
                                bbox: tuple[float, float, float, float],
                                margin: float = 0.05) -> None:
        """Zoom/fit the window projection to the given bbox."""
        left, bottom, right, top = bbox
        w = max(1e-6, right - left)
        h = max(1e-6, top - bottom)

        # Add margin around content
        left   -= w * margin
        right  += w * margin
        bottom -= h * margin
        top    += h * margin
        w = right - left
        h = top - bottom

        # Letterbox to preserve window aspect ratio
        win_w, win_h = self.window.width, self.window.height
        window_ar = win_w / max(1, win_h)
        bbox_ar = w / max(1e-6, h)
        if bbox_ar > window_ar:
            # Expand height
            new_h = w / window_ar
            pad = (new_h - h) / 2
            bottom -= pad
            top += pad
        else:
            # Expand width
            new_w = h * window_ar
            pad = (new_w - w) / 2
            left -= pad
            right += pad

        # Set orthographic projection (pyglet 2.x preferred, else legacy GL)
        if pyg_math is not None and hasattr(self.window, "projection"):
            self.window.projection = pyg_math.Mat4.orthogonal_projection(
                left, right, bottom, top, -1.0, 1.0)
        else:
            gl.glMatrixMode(gl.GL_PROJECTION)
            gl.glLoadIdentity()
            gl.gluOrtho2D(left, right, bottom, top)
            gl.glMatrixMode(gl.GL_MODELVIEW)
            gl.glLoadIdentity()

    def update(self, dt: float) -> None:
        """Updates the position of all particles in the system.

        Args:
            dt (float): Delta time.

        """
        self.manager.update_particles()
        for particle, circle in zip(self.manager.particles, self.circles):
                circle.x = particle.getX()
                circle.y = particle.getY()
        if const.SHOW_QUADTREE:
            self.update_rectangles()


    def update_rectangles(self) -> None:
        """Updates the quadtree rectangles."""
        for rectangle in self.rectangles:
            rectangle.delete()
        self.rectangles.clear()

        if self.manager.quadtree is not None:
            bboxes = self.manager.quadtree.collectBoxes()
            self.rectangles = [
                shapes.BorderedRectangle(
                    bbox[0],
                    bbox[1],
                    bbox[2] - bbox[0],
                    bbox[3] - bbox[1],
                    border=2,
                    color=(0, 0, 0),  # Transparent fill
                    border_color=(255, 0, 0),
                    batch=self.batch
                )
                for bbox in bboxes
            ]

    def run(self) -> None:
        """Runs the pyglet application."""
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        pyglet.app.run()
