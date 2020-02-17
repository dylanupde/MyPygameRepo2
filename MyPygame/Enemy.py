#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Is a very scary and smart rectangle
#####################################################

import pygame
from Vector2 import Vector2
import Constants
from Agent import Agent

class Enemy(Agent):
    """a very scary enemy :O"""

    def __init__(self, inputPos, inputSpeed, inputSize):
        Agent.__init__(self, inputPos, inputSpeed, inputSize)
        self.color = Constants.ENEMY_COLOR
        self.playerCenter = Vector2(0, 0)
        self.isIt = true;
    
    def Draw(self, inputScreen):
        Agent.Draw(self, inputScreen)
        if self.velocity.x != 0 and self.velocity.y != 0:
            pygame.draw.line(inputScreen, (255, 0, 0), (self.center.x, self.center.y), (self.playerCenter.x, self.playerCenter.y), 1)
            pass



    def Update(self, inputPlayer):
        self.playerCenter = inputPlayer.center
        selfToPlayerVector = inputPlayer.position - self.position
        if selfToPlayerVector.Magnitude() < 200:
            self.velocity = (selfToPlayerVector.Normalized()).Scale(self.speed)
            pass
        else:
            self.velocity = Vector2(0, 0)
            pass
        
        Agent.Update(self);