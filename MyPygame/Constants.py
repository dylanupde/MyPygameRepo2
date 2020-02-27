#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Stores magic numbers
#####################################################

from Vector2 import Vector2

FRAME_RATE = 60
WORLD_WIDTH = 800
WORLD_HEIGHT = 600
BACKGROUND_COLOR = (100, 149, 237)
PLAYER_SIZE = 10
PLAYER_SPEED = 5.5
PLAYER_COLOR = (255, 255, 0)
ENEMY_COLOR = (0, 255, 0)
ENEMY_SIZE = 10
ENEMY_SPEED = 5
HUNTER_COLOR = (202, 31, 123)
UNTAGGABLE_FLASH_COLOR = (255, 255, 255)
DOGSHEEP_SIZE = Vector2(16, 32)
VELOCITY_LINE_SCALE = 5

# Flocking stuff
SHEEP_NEIGHBOR_RADIUS = 150
SHEEP_BOUNDARY_RADIUS = 50
SHEEP_ALIGNMENT_WEIGHT = 0.3
SHEEP_SEPARATION_WEIGHT = 0.325
SHEEP_COHESION_WEIGHT = 0.3
SHEEP_DOG_INFLUENCE_WEIGHT = 0
SHEEP_BOUNDARY_INFLUENCE_WEIGHT = 0.2
MIN_ATTACK_DIST = 200