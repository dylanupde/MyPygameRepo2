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
import random
import math


class Dog(Agent):
    """The dawg"""

    def __init__(self, inputPos, inputSpeed, inputSize):
        super().__init__(inputPos, inputSpeed, inputSize)
        self.color = Constants.PLAYER_COLOR
        self.originalArtSurface = pygame.image.load("collie.png")
        self.velocity = Vector2(random.random() - 0.5, random.random() - 0.5).Normalized()
        self.currentSpeed = 0
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)
        self.angle = math.degrees(self.angle)

        
    ### Updates the position based on the velocity. Also updates the center
    def Update(self):

        # If any of the WASD buttons are pressed, set our current speed and velocity
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d] :
            
            self.velocity = Vector2(0, 0)
            self.currentSpeed = self.maxSpeed

            if pressed[pygame.K_w] : 
                self.velocity.y = -1
            if pressed[pygame.K_s] : 
                self.velocity.y = 1
            if pressed[pygame.K_a] : 
                self.velocity.x = -1
            if pressed[pygame.K_d] : 
                self.velocity.x = 1
        else :
            self.currentSpeed = 0
        
        super().Update()



    def DrawVelocityLine(self, inputScreen):
        lineVector = self.velocity.Scale(self.currentSpeed).Scale(Constants.VELOCITY_LINE_SCALE)
        pygame.draw.line(inputScreen, (0, 255, 0), (self.center.x, self.center.y), (self.center.x + lineVector.x, self.center.y + lineVector.y), 3)

