#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Stuff that moves, really
#####################################################

import pygame
from Vector2 import Vector2
import Constants

class Agent(object):
    """description of class"""

    def __init__(self, inputPos, inputSpeed, inputSize):
        self.position = inputPos
        self.size = inputSize
        self.maxSpeed = inputSpeed
        self.velocity = Vector2(0, 0)
        self.center = Vector2(0, 0)
        self.CalculateCenter()
        self.myRect = None
        self.hasDrawn = False


    def __str__(self):
        return ("Size: " + str(self.size) + ". Position: " + str(self.position) + ". Velocity: " + str(self.velocity) + ". Center: " + str(self.center))


    ### Draws this bad boi and its velocity line
    def Draw(self, inputScreen):
        self.hasDrawn = True

        # Draw my rectangle at the position
        self.myRect = pygame.draw.rect(inputScreen, self.color, pygame.Rect(self.position.x, self.position.y, self.size, self.size))

        self.DrawVelocityLine(inputScreen)



    ### Updates the position based on the velocity. Also updates the center
    def Update(self):
        self.MoveSelf()
        self.ConstrainToWorldSize()
        self.CalculateCenter()



    def DrawVelocityLine(self, inputScreen):
        scaledUpVelocity = self.velocity.Scale(Constants.VELOCITY_LINE_SCALE)
        pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (self.center.x + scaledUpVelocity.x, self.center.y + scaledUpVelocity.y), 3)



    def CalculateCenter(self):
        self.center = Vector2(self.position.x + (self.size * 0.5), self.position.y + (self.size * 0.5))


    def ConstrainToWorldSize(self):
        if self.position.x < 0:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = 0
        if self.position.x > (Constants.WORLD_WIDTH - self.size):
            self.position.x = Constants.WORLD_WIDTH - self.size
        if self.position.y > (Constants.WORLD_HEIGHT - self.size):
            self.position.y = Constants.WORLD_HEIGHT - self.size


    def MoveSelf(self):
        self.velocity = self.velocity.Normalized()
        self.velocity = self.velocity.Scale(self.maxSpeed)
        self.position = self.position + self.velocity