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


sheepList = [Sheep(Vector2(100, 100), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), Sheep(Vector2(200, 100), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), 
             Sheep(Vector2(300, 100), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), Sheep(Vector2(400, 100), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), 
             Sheep(Vector2(500, 100), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), Sheep(Vector2(100, 500), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), 
             Sheep(Vector2(200, 500), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), Sheep(Vector2(300, 500), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), 
             Sheep(Vector2(400, 500), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE), Sheep(Vector2(500, 500), Constants.ENEMY_SPEED, Constants.DOGSHEEP_SIZE)]

#sheepList = []
#for i in range(0, 10):
#    pass


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        

        screen.fill(Constants.BACKGROUND_COLOR)

        myDog.Update()
        myDog.Draw(screen)

        #for thisEnemy in enemyList:
        #    thisEnemy.Update(myPlayer)
        #    thisEnemy.Draw(screen)

        for thisSheep in sheepList:
            thisSheep.DoFlockingStuff(sheepList)
            thisSheep.Update(myDog)
            thisSheep.Draw(screen)

        pygame.display.flip()
        clock.tick(Constants.FRAME_RATE)