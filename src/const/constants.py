"""Constant values for particle simulation."""
GRAVITY = 0.981 # Acceleration due to gravity
PARTICLES = 75 # Number of particles
MIN_SIZE = 5 # Minimum particle size
MAX_SIZE = 10 # Maximum particle size
EPSILON = 1e-3 # Small value to prevent division by zero
MAX_DEPTH = 15 # Maximum depth of the quadtree
THETA = 1 # Barnes-Hut threshold
REBUILD_RATE = 0 # Quadtree rebuild rate
BARNES_HUT = True # Use Barnes-Hut optimization
SHOW_QUADTREE = False # Show quadtree visualization
FIT_TREE = False # Fit quadtree to screen
