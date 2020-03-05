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
import random
import math

class Agent(object):
    """description of class"""

    def __init__(self, inputPos, inputSpeed, inputSize):
        # Set boundingRect BEFORE the parent calls CalculateCenter so it doesn't ask where tf the variable is
        self.boundingRect = None
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

        inputScreen.blit(self.currentArtSurface, [self.position.x, self.position.y])
        
        self.DrawVelocityLine(inputScreen)

        if Constants.BOUNDING_BOXES_ON:
            pygame.draw.rect(inputScreen, (0, 0, 0), self.boundingRect, 2)



    ### Updates the position based on the velocity. Also updates the center
    def Update(self):
        # Update the angle
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)
        self.angle = math.degrees(self.angle) - 90
        
        self.MoveSelf()

        # Do the rotation/bounding box math here so we can use it to calculate the center
        self.currentArtSurface = pygame.transform.rotate(self.originalArtSurface, self.angle)
        self.UpdateBoundingRect()
        self.CalculateCenter()

        self.ConstrainToWorldSize()



    def DrawVelocityLine(self, inputScreen):
        scaledUpVelocity = self.velocity.Scale(Constants.VELOCITY_LINE_SCALE)
        pygame.draw.line(inputScreen, (0, 255, 0), (self.center.x, self.center.y), (self.center.x + scaledUpVelocity.x, self.center.y + scaledUpVelocity.y), 3)



    def CalculateCenter(self):
        if self.boundingRect != None:
            self.center = Vector2(self.boundingRect.centerx, self.boundingRect.centery)



    def ConstrainToWorldSize(self):
        # Basically however much too far we are over the edge, just go back that exact distance
        if self.boundingRect.left < 0:
            self.position.x -= self.boundingRect.left
        if self.boundingRect.top < 0:
            self.position.y -= self.boundingRect.top
        if self.boundingRect.right > Constants.WORLD_WIDTH:
            difference = self.boundingRect.right - Constants.WORLD_WIDTH
            self.position.x -= difference
        if self.boundingRect.bottom > Constants.WORLD_HEIGHT:
            difference = self.boundingRect.bottom - Constants.WORLD_HEIGHT
            self.position.y -= difference

        self.UpdateBoundingRect()



    def MoveSelf(self):
        vectorToMove = self.velocity.Normalized().Scale(self.currentSpeed)
        self.position = self.position + vectorToMove



    def UpdateBoundingRect(self):
        self.boundingRect = self.currentArtSurface.get_bounding_rect()
        self.boundingRect = self.boundingRect.move(self.position.x, self.position.y)