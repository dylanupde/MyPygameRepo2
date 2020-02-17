#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Controls the player
#####################################################

import pygame
from Vector2 import Vector2
import Constants
from Agent import Agent

class Player(Agent):
    """The playa"""

    def __init__(self, inputPos, inputSpeed, inputSize):
        Agent.__init__(self, inputPos, inputSpeed, inputSize)
        self.color = Constants.PLAYER_COLOR






    ### Updates the position based on the velocity. Also updates the center
    def Update(self):
        self.velocity = Vector2(0, 0)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] : self.velocity.y = -1
        if pressed[pygame.K_s] : self.velocity.y = 1
        if pressed[pygame.K_a] : self.velocity.x = -1
        if pressed[pygame.K_d] : self.velocity.x = 1
        
        Agent.Update(self);