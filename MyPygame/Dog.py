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
        self.currentPath = []
        self.isWaitingOneFrame = True

        
    ### Updates the position based on the velocity. Also updates the center
    def Update(self, inputGraph, inputSheepNode):

        ## If any of the WASD buttons are pressed, set our current speed and velocity
        #pressed = pygame.key.get_pressed()
        #if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d] :
            
        #    self.velocity = Vector2(0, 0)
        #    self.currentSpeed = self.maxSpeed

        #    if pressed[pygame.K_w] : 
        #        self.velocity.y = -1
        #    if pressed[pygame.K_s] : 
        #        self.velocity.y = 1
        #    if pressed[pygame.K_a] : 
        #        self.velocity.x = -1
        #    if pressed[pygame.K_d] : 
        #        self.velocity.x = 1
        #else :
        #    self.currentSpeed = 0

        # Wait one frame for the sheep's center to be right
        if self.isWaitingOneFrame == True:
            self.isWaitingOneFrame = False
            super().Update()
            return

        myNode = inputGraph.getNodeFromPoint(self.center)
        if len(self.currentPath) > 0:
            self.currentSpeed = self.maxSpeed
            targetNodeCenter = self.currentPath[0].center
            distFromNode = (self.center - self.currentPath[0].center).Magnitude()
            # If we're close enough to the node, pop it off
            if distFromNode <= Constants.DOG_SPEED + 10:
                self.currentPath.pop(0)
            targetVelocity = (targetNodeCenter - self.center).Normalized().Scale(self.maxSpeed)
            velocityDiffWeighted = (targetVelocity - self.velocity).Scale(Constants.DOG_ANGULAR_SPEED)
            self.velocity = (self.velocity + velocityDiffWeighted).Normalized().Scale(self.maxSpeed)
        else:
            if Constants.SEARCH_MODE == "A":
                self.currentPath = inputGraph.findPath_Djikstra(myNode, inputSheepNode, True)
            elif Constants.SEARCH_MODE == "BEST":
                self.currentPath = inputGraph.findPath_BestFirst(myNode, inputSheepNode)
            elif Constants.SEARCH_MODE == "DJIKSTRA":
                self.currentPath = inputGraph.findPath_Djikstra(myNode, inputSheepNode, False)
            elif Constants.SEARCH_MODE == "BREADTH":
                self.currentPath = inputGraph.findPath_Breadth(myNode, inputSheepNode)



        super().Update()



    def DrawVelocityLine(self, inputScreen):
        lineVector = self.velocity.Scale(self.currentSpeed).Scale(Constants.VELOCITY_LINE_SCALE)
        pygame.draw.line(inputScreen, (0, 255, 0), (self.center.x, self.center.y), (self.center.x + lineVector.x, self.center.y + lineVector.y), 3)

