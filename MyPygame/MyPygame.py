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
import Constants

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

#xPos = 120
#yPos = 30
clock = pygame.time.Clock()


#-=TESTING=-
testVector = Vector2(3, 4)
testVectorA = Vector2(1, 1)
testVectorB = testVector - testVectorA
print(testVector.Normalized())
#-=TESTING=-

playerPos = Vector2((Constants.WORLD_WIDTH * 0.5) - (Constants.PLAYER_SIZE * 0.5), (Constants.WORLD_HEIGHT * 0.5) - (Constants.PLAYER_SIZE * 0.5))
myPlayer = Player(playerPos, Constants.PLAYER_SPEED, Constants.PLAYER_SIZE)
print(myPlayer);

enemyPos = Vector2(100, 100)
mySeekerEnemy = Enemy(enemyPos, Constants.ENEMY_SPEED, Constants.ENEMY_SIZE)
print(mySeekerEnemy)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        

        screen.fill(Constants.BACKGROUND_COLOR)

        myPlayer.Update()
        myPlayer.Draw(screen)

        mySeekerEnemy.Update(myPlayer)
        mySeekerEnemy.Draw(screen)

        pygame.display.flip()
        clock.tick(Constants.FRAME_RATE)