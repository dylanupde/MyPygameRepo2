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

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

clock = pygame.time.Clock()

playerPos = Vector2((Constants.WORLD_WIDTH * 0.5) - (Constants.DOGSHEEP_SIZE.x * 0.5), (Constants.WORLD_HEIGHT * 0.5) - (Constants.DOGSHEEP_SIZE.y * 0.5))
myDog = Dog(playerPos, Constants.PLAYER_SPEED, Constants.DOGSHEEP_SIZE)
print(myDog);

#sheepHorizontalSeparation = Constants.WORLD_WIDTH / 11
#sheepVerticalSeparation = Constants.WORLD_HEIGHT / 11

##sheepList = [Sheep(Vector2(100, 100), Constants.SHEEP_SPEED, Constants.DOGSHEEP_SIZE)]

sheepList = []

for x in range(0, 100):
    xCoord = random.randint(Constants.DOGSHEEP_SIZE.x, Constants.WORLD_WIDTH - Constants.DOGSHEEP_SIZE.x)
    yCoord = random.randint(Constants.DOGSHEEP_SIZE.y, Constants.WORLD_HEIGHT - Constants.DOGSHEEP_SIZE.y)
    sheepPosition = Vector2(xCoord, yCoord)
    sheepList.append(Sheep(sheepPosition, Constants.SHEEP_SPEED, Constants.DOGSHEEP_SIZE))

#for x in range(1, 11):
#    xCoord = x * sheepHorizontalSeparation

#    for y in range(1, 11):
#        yCoord = y * sheepVerticalSeparation
#        sheepPosition = Vector2(xCoord, yCoord)
#        sheepList.append(Sheep(sheepPosition, Constants.SHEEP_SPEED, Constants.DOGSHEEP_SIZE))




while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        

        screen.fill(Constants.BACKGROUND_COLOR)
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            Constants.SHEEP_VELOCITY_LINE_ON = not Constants.SHEEP_VELOCITY_LINE_ON
            print("SheepVelocityLineOn: ", Constants.SHEEP_VELOCITY_LINE_ON)
        if pressed[pygame.K_2]:
            Constants.DOG_FORCE_LINE_ON = not Constants.DOG_FORCE_LINE_ON
            print("DogForceLineOn: ", Constants.DOG_FORCE_LINE_ON)
        if pressed[pygame.K_3]:
            Constants.BOUNDARY_FORCES_LINES_ON = not Constants.BOUNDARY_FORCES_LINES_ON
            print("BoundaryForceLinesOn: ", Constants.BOUNDARY_FORCES_LINES_ON)
        if pressed[pygame.K_4]:
            Constants.NEIGHBOR_LINES_ON = not Constants.NEIGHBOR_LINES_ON
            print("NeighborLinesOn: ", Constants.NEIGHBOR_LINES_ON)
        if pressed[pygame.K_5]:
            Constants.BOUNDING_BOXES_ON = not Constants.BOUNDING_BOXES_ON
            print("BoundingBoxesOn: ", Constants.BOUNDING_BOXES_ON)
        if pressed[pygame.K_6]:
            Constants.DOG_FORCES_ON = not Constants.DOG_FORCES_ON
            print("DogForcesOn: ", Constants.DOG_FORCES_ON)
        if pressed[pygame.K_7]:
            Constants.ALIGNMENT_FORCES_ON = not Constants.ALIGNMENT_FORCES_ON
            print("AlignmentForcesOn: ", Constants.ALIGNMENT_FORCES_ON)
        if pressed[pygame.K_8]:
            Constants.SEPARATION_FORCES_ON = not Constants.SEPARATION_FORCES_ON
            print("SeparationForcesOn: ", Constants.SEPARATION_FORCES_ON)
        if pressed[pygame.K_9]:
            Constants.COHESION_FORCES_ON = not Constants.COHESION_FORCES_ON
            print("CohesionForcesOn: ", Constants.COHESION_FORCES_ON)
        if pressed[pygame.K_0]:
            Constants.BOUNDARY_FORCES_ON = not Constants.BOUNDARY_FORCES_ON
            print("BoundaryForcesOn: ", Constants.BOUNDARY_FORCES_ON)

        myDog.Update()
        myDog.Draw(screen)

        for thisSheep in sheepList:
            thisSheep.DoFlockingStuff(sheepList)
            thisSheep.Update(myDog)
            thisSheep.Draw(screen)

        pygame.display.flip()
        clock.tick(Constants.FRAME_RATE)