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
        super().__init__(inputPos, inputSpeed, inputSize)
        self.color = Constants.ENEMY_COLOR
        self.originalColor = self.color
        self.targetPos = Vector2(0, 0)
        self.isIt = True;
        self.untaggableIterator = 0
    
    def Draw(self, inputScreen):
        super().Draw(inputScreen)
        if self.velocity.x != 0 and self.velocity.y != 0:
            pygame.draw.line(inputScreen, (255, 0, 0), (self.center.x, self.center.y), (self.targetPos.x, self.targetPos.y), 1)
            pass



    def Update(self, inputPlayer):
        self.CalculateVelocity(inputPlayer)
        self.CheckIsItStuff(inputPlayer)
        super().Update()


    ## When the timer is NOT zero, it has been started. If it's started, it means we're untaggable. So basically we're untaggable when this isn't zero
    def IterateUntaggableTimer(self):
        self.untaggableIterator += 1

        # If we're at the end of the timer, reset self (to indicate we're taggable now) and set color to normal
        if self.untaggableIterator >= 120:
            self.color = self.originalColor
            self.untaggableIterator = 0
        # Otherwise, if we're at a fifth/sixth frame of the timer, flash white
        elif self.untaggableIterator % 5 == 0 or self.untaggableIterator % 5 == 1:
            self.color = Constants.UNTAGGABLE_FLASH_COLOR
        # Otherwise, be a normal color
        else:
            self.color = self.originalColor


    def CalculateVelocity(self, inputPlayer):
        self.targetPos = inputPlayer.center
        selfToPlayerVector = inputPlayer.position - self.position
        if selfToPlayerVector.Magnitude() < 200:
            self.velocity = (selfToPlayerVector.Normalized()).Scale(self.speed)
            pass
        else:
            self.velocity = Vector2(0, 0)
            pass
        


    def CheckIsItStuff(self, inputPlayer):
        if self.untaggableIterator > 0:
            self.IterateUntaggableTimer()

        if self.hasDrawn and inputPlayer.hasDrawn:
            if self.myRect.colliderect(inputPlayer.myRect) and self.untaggableIterator == 0:
                self.isIt = not self.isIt
                self.IterateUntaggableTimer()

        if self.isIt == False:
            self.velocity = self.velocity.Scale(-1)
            pass