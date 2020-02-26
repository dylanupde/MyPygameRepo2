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

enemyList = [Enemy(Vector2(100, 100), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), Enemy(Vector2(200, 100), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), 
             Enemy(Vector2(300, 100), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), Enemy(Vector2(400, 100), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), 
             Enemy(Vector2(500, 100), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), EnemyHunter(Vector2(100, 500), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), 
             EnemyHunter(Vector2(200, 500), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), EnemyHunter(Vector2(300, 500), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), 
             EnemyHunter(Vector2(400, 500), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), EnemyHunter(Vector2(500, 500), Constants.ENEMY_SPEED, Constants.ENEMY_SIZE), ]


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        

        screen.fill(Constants.BACKGROUND_COLOR)

        myPlayer.Update()
        myPlayer.Draw(screen)

        for thisEnemy in enemyList:
            thisEnemy.Update(myPlayer)
            thisEnemy.Draw(screen)

        pygame.display.flip()
        clock.tick(Constants.FRAME_RATE)