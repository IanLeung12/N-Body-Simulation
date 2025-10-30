# N-Body Particle Gravity Simulation using Barnes-Hut Algorithm #

Allows for heavy configuration by editing variables in the ```src/const/constants.py``` file
* PARTICLES: number of particles
* THETA: Threshold for barnes hut to stop at a parent node (node width/distance > Theta)
* BARNES_HUT: Use barnes hut vs brute force approach
* Several others variables to configure

## Demonstration: ##


Brute Force Approach - O(N^2):


![Untitled video - Made with Clipchamp](https://github.com/user-attachments/assets/a61c5393-b28f-480e-9e65-9785d662b2ac)


Optimized (Barnes Hut) Approach - O(NlogN):


![Untitled video - Made with Clipchamp (1)](https://github.com/user-attachments/assets/a56b9beb-f74d-465f-b3f6-62de1c8a1b03)

## Running Instructions (Windows): ##

1. Create a virtual environment using ```python -m venv .venv```
2. Activate the virtual environment using ```.venv/Scripts/activate```
3. Install libraries using ```pip install -e .```
4. Configure settings in ```src/const/constants.py```
5. Run main using ```python src/main.py```

