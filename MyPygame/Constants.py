#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Stores magic numbers
#####################################################

from Vector2 import Vector2

FRAME_RATE = 60
WORLD_WIDTH = 1024
WORLD_HEIGHT = 768
BACKGROUND_COLOR = (100, 149, 237)
DOG_SPEED = 5
DOG_ANGULAR_SPEED = 1
PLAYER_COLOR = (255, 255, 0)
ENEMY_COLOR = (0, 255, 0)
ENEMY_SIZE = 10
ENEMY_SPEED = 5
HUNTER_COLOR = (202, 31, 123)
UNTAGGABLE_FLASH_COLOR = (255, 255, 255)
DOGSHEEP_SIZE = Vector2(16, 32)
VELOCITY_LINE_SCALE = 5
SHEEP_SPEED = 5
SHEEP_COUNT = 1
SHEEP_ANGULAR_SPEED = .2

# Flocking stuff
SHEEP_NEIGHBOR_RADIUS = 50
SHEEP_BOUNDARY_RADIUS = 50
SHEEP_OBSTACLE_RADIUS = 50
SHEEP_ALIGNMENT_WEIGHT = 0.3
SHEEP_SEPARATION_WEIGHT = 0.325
SHEEP_COHESION_WEIGHT = 0.3
SHEEP_DOG_INFLUENCE_WEIGHT = 0.2
SHEEP_BOUNDARY_INFLUENCE_WEIGHT = 0.3
SHEEP_OBSTACLE_INFLUENCE_WEIGHT = 0.3
MIN_ATTACK_DIST = 100

SHEEP_VELOCITY_LINE_ON = False
DOG_FORCE_LINE_ON = False
BOUNDARY_FORCES_LINES_ON = False
NEIGHBOR_LINES_ON = False
BOUNDING_BOXES_ON = False
DOG_FORCES_ON = True
ALIGNMENT_FORCES_ON = True
SEPARATION_FORCES_ON = True
COHESION_FORCES_ON = True
BOUNDARY_FORCES_ON = True
DEBUG_GRID_LINES = True
DEBUG_NEIGHBOR_LINES = True

# Pathfinding
GATE_COUNT = 4
GATE_WIDTH = 100
GATES = [ [ [104, 552], [104, 664] ], \
	      [ [104, 216], [104, 104] ], \
		  [ [808, 616], [696, 616] ], \
		  [ [936, 152], [824, 152] ], \
		  #[ [456, 440], [456, 328] ]  ]		# vertical, green is on bottom (backwards c)
		  #[ [568, 328], [568, 440] ]  ]		# vertical, green is on top (c)
		  [ [456, 328], [568, 328] ]  ]	# horizontal, green on left (u)
		  #[ [568, 440], [456, 440] ]  ]	# horizontal, green on right (n)
		  
NBR_RANDOM_OBSTACLES = 20
GRID_SIZE = 16
DEBUG_LINE_WIDTH = 1