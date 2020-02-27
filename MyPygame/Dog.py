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
        self.boundingRect = None
        super().__init__(inputPos, inputSpeed, inputSize)
        self.color = Constants.PLAYER_COLOR
        self.originalArtSurface = pygame.image.load("collie.png")
        self.velocity = Vector2(random.random() - 0.5, random.random() - 0.5).Normalized()
        self.currentSpeed = 0
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)
        self.angle = math.degrees(self.angle)



    def Draw(self, inputScreen):
        self.hasDrawn = True

        inputScreen.blit(self.currentArtSurface, [self.position.x, self.position.y])

        pygame.draw.rect(inputScreen, (0, 0, 0), self.boundingRect, 2)

        self.DrawVelocityLine(inputScreen)


    def DrawVelocityLine(self, inputScreen):
        lineVector = self.velocity.Scale(self.currentSpeed).Scale(Constants.VELOCITY_LINE_SCALE)
        pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (self.center.x + lineVector.x, self.center.y + lineVector.y), 3)
        #pygame.draw.line(inputScreen, (0, 0, 255), (self.position.x, self.position.y), (self.position.x + lineVector.x, self.position.y + lineVector.y), 3)


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
        

        
        # Update the angle
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)
        self.angle = math.degrees(self.angle) - 90
        
        self.MoveSelf()

        self.currentArtSurface = pygame.transform.rotate(self.originalArtSurface, self.angle)
        self.UpdateBoundingRect()
        self.CalculateCenter()

        self.ConstrainToWorldSize()


    def CalculateCenter(self):
        if self.boundingRect != None:
            self.center = Vector2(self.boundingRect.centerx, self.boundingRect.centery)



    def ConstrainToWorldSize(self):
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