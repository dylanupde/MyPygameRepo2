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
        self.speed = inputSpeed
        self.velocity = Vector2(0, 0)
        self.center = Vector2(self.position.x + (self.size * 0.5), self.position.x + (self.size * 0.5))
        


    def __str__(self):
        return ("Size: " + str(self.size) + ". Position: " + str(self.position) + ". Velocity: " + str(self.velocity) + ". Center: " + 
                str(self.position.x + (self.size * 0.5)) + ", " + str(self.position.y + (self.size * 0.5)))



    ### Draws this bad boi and its velocity line
    def Draw(self, inputScreen):
        # Draw my rectangle at the position
        myRect = pygame.draw.rect(inputScreen, self.color, pygame.Rect(self.position.x, self.position.y, self.size, self.size))
        
        ## Test if we can hit stuff
        #libtardRect = pygame.draw.rect(inputScreen, (0, 0, 255), pygame.Rect(300, 100, 40, 40))
        #if libtardRect.colliderect(myRect):
        #    pygame.draw.rect(inputScreen, (0, 0, 255), pygame.Rect(500, 400, 40, 40))
        #    pass

        # Draw the velocity line
        scaledUpVelocity = self.velocity.Scale(5)
        pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (self.center.x + scaledUpVelocity.x, self.center.y + scaledUpVelocity.y), 3)



    ### Updates the position based on the velocity. Also updates the center
    def Update(self):
        self.velocity = self.velocity.Normalized()
        self.velocity = self.velocity.Scale(self.speed)
        self.position = self.position + self.velocity

        # Calculate our center (in case we need it in debugging)
        self.center = Vector2(self.position.x + (self.size * 0.5), self.position.y + (self.size * 0.5))