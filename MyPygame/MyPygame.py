#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Runs the game!
#####################################################


import pygame
from Vector2 import Vector2
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter
from Sheep import Sheep
from Dog import Dog
import Constants
import random
import Graph
import Node
from Graph import *
from Node import *
from random import *

#################################################################################
# Helper Functions
#################################################################################

def buildGates(graph):
	X = 0
	Y = 1
	# Add the gates to the game
	# pick one end, then pick the second end about 50 spaces away (pick a direction, generate the far end
	for gate in Constants.GATES:
		graph.placeObstacle(Vector2(gate[0][X], gate[0][Y]), (0, 255, 0))
		graph.placeObstacle(Vector2(gate[1][X], gate[1][Y]), (255, 0, 0))
		print("Placing Obstacles: " + str(gate[0]) + " " + str(gate[1]))

	# Add the final pen based on the final gate
	finalGate = gate[-2:]
	# If the gate is horizontally arranged
	if finalGate[0][Y] == finalGate[1][Y]:
		# If the green gate (the first gate) is on the right, paddock goes "up"
		if finalGate[0][X] > finalGate[1][X]:
			direction = -1
		else:
			direction = 1
		for y in range(finalGate[0][Y] + direction * 16, finalGate[0][Y] + direction * 112, direction * 16):
			graph.placeObstacle(Vector2(finalGate[0][X], y), (0, 0, 0))
			graph.placeObstacle(Vector2(finalGate[1][X], y), (0, 0, 0))
		for x in range(finalGate[0][X] + direction * 16, finalGate[1][X], direction * 16):
			graph.placeObstacle(Vector2(x, finalGate[0][Y] + direction * 96), (0, 0, 0))
	# If the gate is vertically arranged
	else:
		# If the green gate (the first gate) is on the bottom, paddock goes "right"
		if finalGate[0][Y] < finalGate[1][Y]:
			direction = -1
		else:
			direction = 1
		for x in range(finalGate[0][X] + direction * 16, finalGate[1][X] + direction * 112, direction * 16):
			graph.placeObstacle(Vector2(x, finalGate[0][Y]), (0, 0, 0))
			graph.placeObstacle(Vector2(x, finalGate[1][Y]), (0, 0, 0))
		for y in range(finalGate[0][Y] - direction *  16, finalGate[1][Y], - direction * 16):
			graph.placeObstacle(Vector2(finalGate[0][X] + direction * 96, y), (0, 0, 0))

def buildObstacles(graph):
	# Random Obstacles
	for i in range(Constants.NBR_RANDOM_OBSTACLES):
		start = Vector2(randrange(0, Constants.WORLD_WIDTH), randrange(0, Constants.WORLD_HEIGHT))
		graph.placeObstacle(start, (0, 0, 0))
		for j in range(randrange(Constants.NBR_RANDOM_OBSTACLES)):
			start += Vector2((randrange(3) - 1) * Constants.GRID_SIZE, (randrange(3) - 1) * Constants.GRID_SIZE)
			while(start.x >= Constants.WORLD_WIDTH - Constants.GRID_SIZE or start.y >= Constants.WORLD_HEIGHT - Constants.GRID_SIZE):
				start += Vector2((randrange(3) - 1) * Constants.GRID_SIZE, (randrange(3) - 1) * Constants.GRID_SIZE)
			graph.placeObstacle(start, (0, 0, 0))





##############################################################
# MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIN!!!!!!!!!!!!!!!!!!!!!!!!!!
##############################################################

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False
clock = pygame.time.Clock()
graph = Graph()

playerPos = Vector2((Constants.WORLD_WIDTH * 0.5) - (Constants.DOGSHEEP_SIZE.x * 0.5), (Constants.WORLD_HEIGHT * 0.5) - (Constants.DOGSHEEP_SIZE.y * 0.5))
myDog = Dog(playerPos, Constants.DOG_SPEED, Constants.DOGSHEEP_SIZE)



#sheepHorizontalSeparation = Constants.WORLD_WIDTH / 11
#sheepVerticalSeparation = Constants.WORLD_HEIGHT / 11

##sheepList = [Sheep(Vector2(100, 100), Constants.SHEEP_SPEED, Constants.DOGSHEEP_SIZE)]

sheepList = []

for x in range(0, 1):
    xCoord = randint(Constants.DOGSHEEP_SIZE.x, Constants.WORLD_WIDTH - Constants.DOGSHEEP_SIZE.x)
    yCoord = randint(Constants.DOGSHEEP_SIZE.y, Constants.WORLD_HEIGHT - Constants.DOGSHEEP_SIZE.y)
    sheepPosition = Vector2(xCoord, yCoord)
    sheepList.append(Sheep(sheepPosition, Constants.SHEEP_SPEED, Constants.DOGSHEEP_SIZE))

#for x in range(1, 11):
#    xCoord = x * sheepHorizontalSeparation

#    for y in range(1, 11):
#        yCoord = y * sheepVerticalSeparation
#        sheepPosition = Vector2(xCoord, yCoord)
#        sheepList.append(Sheep(sheepPosition, Constants.SHEEP_SPEED, Constants.DOGSHEEP_SIZE))


# Setup the gates and obstacles
buildGates(graph)
buildObstacles(graph)

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == pygame.K_1:
                    Constants.SHEEP_VELOCITY_LINE_ON = not Constants.SHEEP_VELOCITY_LINE_ON
                    print("SheepVelocityLineOn: ", Constants.SHEEP_VELOCITY_LINE_ON)
                if event.key == pygame.K_2:
                    Constants.DOG_FORCE_LINE_ON = not Constants.DOG_FORCE_LINE_ON
                    print("DogForceLineOn: ", Constants.DOG_FORCE_LINE_ON)
                if event.key == pygame.K_3:
                    Constants.BOUNDARY_FORCES_LINES_ON = not Constants.BOUNDARY_FORCES_LINES_ON
                    print("BoundaryForceLinesOn: ", Constants.BOUNDARY_FORCES_LINES_ON)
                if event.key == pygame.K_4:
                    Constants.NEIGHBOR_LINES_ON = not Constants.NEIGHBOR_LINES_ON
                    print("NeighborLinesOn: ", Constants.NEIGHBOR_LINES_ON)
                if event.key == pygame.K_5:
                    Constants.BOUNDING_BOXES_ON = not Constants.BOUNDING_BOXES_ON
                    print("BoundingBoxesOn: ", Constants.BOUNDING_BOXES_ON)
                if event.key == pygame.K_6:
                    Constants.DOG_FORCES_ON = not Constants.DOG_FORCES_ON
                    print("DogForcesOn: ", Constants.DOG_FORCES_ON)
                if event.key == pygame.K_7:
                    Constants.ALIGNMENT_FORCES_ON = not Constants.ALIGNMENT_FORCES_ON
                    print("AlignmentForcesOn: ", Constants.ALIGNMENT_FORCES_ON)
                if event.key == pygame.K_8:
                    Constants.SEPARATION_FORCES_ON = not Constants.SEPARATION_FORCES_ON
                    print("SeparationForcesOn: ", Constants.SEPARATION_FORCES_ON)
                if event.key == pygame.K_9:
                    Constants.COHESION_FORCES_ON = not Constants.COHESION_FORCES_ON
                    print("CohesionForcesOn: ", Constants.COHESION_FORCES_ON)
                if event.key == pygame.K_0:
                    Constants.BOUNDARY_FORCES_ON = not Constants.BOUNDARY_FORCES_ON
                    print("BoundaryForcesOn: ", Constants.BOUNDARY_FORCES_ON)
                if event.key == pygame.K_a:
                    graph.findPath_AStar(1, 2)
                if event.key == pygame.K_s:
                    graph.findPath_BestFirst(1, 2)
                if event.key == pygame.K_d:
                    graph.findPath_Djikstra(1, 2)
                if event.key == pygame.K_f:
                    graph.findPath_Breadth(1, 2)


    screen.fill(Constants.BACKGROUND_COLOR)
            
    graph.draw(screen)
    myDog.Update()
    myDog.Draw(screen)

    testNode = graph.getNodeFromPoint(Vector2(50, 90))

    for thisSheep in sheepList:
        thisSheep.DoFlockingStuff(sheepList)
        thisSheep.Update(myDog)
        thisSheep.Draw(screen)

    pygame.display.flip()
    clock.tick(Constants.FRAME_RATE)