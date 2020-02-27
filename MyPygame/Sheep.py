#####################################################
# Author: Dylan Updegrave
# Date: 02/26/20
# Email: dupdegra@uccs.edu
# 
# One shoop
#####################################################

import pygame
from Vector2 import Vector2
import Constants
from Agent import Agent
import random
import math

class Sheep(Agent):
    """A shoop"""

    def __init__(self, inputPos, inputSpeed, inputSize):
        self.boundingRect = None
        super().__init__(inputPos, inputSpeed, inputSize)
        self.velocity = Vector2(random.random() - 0.5, random.random() - 0.5).Normalized()
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)
        self.angle = math.degrees(self.angle)
        self.currentSpeed = 0
        self.linearAcceleration = 0
        self.angularVelocity = 0
        self.color = Constants.ENEMY_COLOR
        self.originalArtSurface = pygame.image.load("sheep.png")
        self.myNeighborsList = []


    def Update(self, inputPlayer):
        self.CalculateVelocity(inputPlayer)

        # Update the angle
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)
        self.angle = math.degrees(self.angle) - 90
        
        self.MoveSelf()

        self.currentArtSurface = pygame.transform.rotate(self.originalArtSurface, self.angle)
        self.UpdateBoundingRect()
        self.CalculateCenter()

        self.ConstrainToWorldSize()



    def Draw(self, inputScreen):
        self.hasDrawn = True

        inputScreen.blit(self.currentArtSurface, [self.position.x, self.position.y])

        pygame.draw.rect(inputScreen, (0, 0, 0), self.boundingRect, 2)

        if self.currentSpeed != 0:
            pygame.draw.line(inputScreen, (255, 0, 0), (self.center.x, self.center.y), (self.targetPos.x, self.targetPos.y), 1)
    
        for thisNeighbor in self.myNeighborsList:
            pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (thisNeighbor.center.x, thisNeighbor.center.y), 1)

        self.DrawVelocityLine(inputScreen)


    def DrawVelocityLine(self, inputScreen):
        lineVector = self.velocity.Scale(self.currentSpeed).Scale(Constants.VELOCITY_LINE_SCALE)
        pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (self.center.x + lineVector.x, self.center.y + lineVector.y), 3)


    def CalculateVelocity(self, inputPlayer):
        #self.targetPos = inputPlayer.center
        #playerToSelfVector = self.position - inputPlayer.position
        #if playerToSelfVector.Magnitude() < Constants.MIN_ATTACK_DIST:
        #    self.velocity = playerToSelfVector.Normalized()
        #    self.currentSpeed = self.maxSpeed
        #else:
        #    self.currentSpeed = 0

        self.velocity = self.velocity + self.flockingVelocityToAdd


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






    ### FLOCKING!!!!!!!!!!!!!!
    def DoFlockingStuff(self, inputSheepList):
        self.myNeighborsList = self.CalculateNeighbors(inputSheepList)
        alignmentVector = self.GetAlignmentVector(self.myNeighborsList)

        self.flockingVelocityToAdd = alignmentVector


    def CalculateNeighbors(self, inputSheepList):
        neighborList = []

        for thisShoop in inputSheepList:
            if thisShoop != self:
                distanceFromThisShoop = (self.position - thisShoop.position).Magnitude()
                if distanceFromThisShoop < Constants.SHEEP_NEIGHBOR_RADIUS:
                    neighborList.append(thisShoop)

        return neighborList


    def GetAlignmentVector(self, inputNeighborList):
        totalVelocity = Vector2(0, 0)
        neighborCount = 0

        for thisShoop in inputNeighborList:
            if thisShoop != self:
                distanceFromThisShoop = (self.position - thisShoop.position).Magnitude()
                if distanceFromThisShoop < Constants.SHEEP_NEIGHBOR_RADIUS:
                    totalVelocity = totalVelocity + thisShoop.velocity
                    neighborCount += 1

        if neighborCount != 0:
            totalVelocity.x /= neighborCount
            totalVelocity.y /= neighborCount
            totalVelocity = totalVelocity.Normalized()

        return totalVelocity