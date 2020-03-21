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
import random
import math
from Agent import Agent

class Sheep(Agent):
    """A shoop"""

    def __init__(self, inputPos, inputSpeed, inputSize):
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
        self.dogForce = Vector2(0, 0)
        self.linesToDrawList = []


    def Update(self, inputPlayer):
        self.CalculateVelocity(inputPlayer)
        super().Update()



    def Draw(self, inputScreen):
        super().Draw(inputScreen)

        if self.dogForce.x != 0 or self.dogForce.y != 0:
            pygame.draw.line(inputScreen, (255, 0, 0), (self.center.x, self.center.y), (self.targetPos.x, self.targetPos.y), 1)
    
        # Draw lines to each neighbor
        if Constants.NEIGHBOR_LINES_ON:
            for thisNeighbor in self.myNeighborsList:
                pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (thisNeighbor.center.x, thisNeighbor.center.y), 1)


        # Anything in this list gets a line drawn for it, so do dat
        for thisVector in self.linesToDrawList:
            lineVector = thisVector.Normalized().Scale(self.currentSpeed).Scale(Constants.VELOCITY_LINE_SCALE)
            pygame.draw.line(inputScreen, (0, 0, 255), (self.center.x, self.center.y), (self.center.x + lineVector.x, self.center.y + lineVector.y), 2)

        # Don't forget to clear the list each frame so we only draw what was added this frame
        self.linesToDrawList.clear()



    def DrawVelocityLine(self, inputScreen):
        lineVector = self.velocity.Normalized().Scale(self.currentSpeed).Scale(Constants.VELOCITY_LINE_SCALE)
        if Constants.SHEEP_VELOCITY_LINE_ON:
            pygame.draw.line(inputScreen, (0, 255, 0), (self.center.x, self.center.y), (self.center.x + lineVector.x, self.center.y + lineVector.y), 3)



    def CalculateVelocity(self, inputPlayer):
        # Calculate our velocity force if the dawg is nearby
        self.targetPos = inputPlayer.center
        playerToSelfVector = self.position - inputPlayer.position
        if playerToSelfVector.Magnitude() < Constants.MIN_ATTACK_DIST and Constants.DOG_FORCES_ON:
            self.dogForce = playerToSelfVector.Normalized().Scale(Constants.SHEEP_DOG_INFLUENCE_WEIGHT)

            # Draw dog vector line
            if Constants.DOG_FORCE_LINE_ON:
                self.linesToDrawList.append(self.dogForce)
        else:
            self.dogForce = Vector2(0, 0)

        # If there's neighbors or the spooky dog is nearby or we're near a boundary, MOVE
        if len(self.myNeighborsList) > 0 or self.dogForce.x != 0 or self.dogForce.y != 0 or self.boundaryForce.x != 0 or self.boundaryForce.y != 0:
            self.currentSpeed = self.maxSpeed
            targetVelocity = self.dogForce + self.flockingVelocityToAdd
            velocityDiffWeighted = (targetVelocity - self.velocity).Scale(Constants.SHEEP_ANGULAR_SPEED)
            self.velocity = self.velocity + velocityDiffWeighted
        else:
            self.currentSpeed = 0










    ### FLOCKING!!!!!!!!!!!!!!
    def DoFlockingStuff(self, inputSheepList, inputGraph):
        self.myNeighborsList = self.CalculateNeighbors(inputSheepList)

        alignmentVector = Vector2(0, 0)
        cohesionVector = Vector2(0, 0)
        separationVector = Vector2(0, 0)
        self.boundaryForce = Vector2(0, 0)

        if Constants.ALIGNMENT_FORCES_ON:
            alignmentVector = self.GetAlignmentVector(self.myNeighborsList)
        if Constants.COHESION_FORCES_ON:
            cohesionVector = self.GetCohesionVector(self.myNeighborsList)
        if Constants.SEPARATION_FORCES_ON:
            separationVector = self.GetSeparationVector(self.myNeighborsList)
        if Constants.BOUNDARY_FORCES_ON:
            self.boundaryForce = self.GetBoundsForceVector()
            fenceForce = self.GetObstaclesForceVector(inputGraph)

        self.flockingVelocityToAdd = alignmentVector + cohesionVector + separationVector + self.boundaryForce + fenceForce


    def CalculateNeighbors(self, inputSheepList):
        neighborList = []

        for thisShoop in inputSheepList:
            if thisShoop != self:
                distanceFromThisShoop = (self.position - thisShoop.position).Magnitude()
                if distanceFromThisShoop < Constants.SHEEP_NEIGHBOR_RADIUS:
                    neighborList.append(thisShoop)

        return neighborList


    # Averages our velocities
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
            totalVelocity = totalVelocity.Normalized().Scale(Constants.SHEEP_ALIGNMENT_WEIGHT)

        return totalVelocity


    # Averages our locations
    def GetCohesionVector(self, inputNeighborList):
        totalPoint = Vector2(0, 0)
        neighborCount = 0

        for thisShoop in inputNeighborList:
            if thisShoop != self:
                distanceFromThisShoop = (self.position - thisShoop.position).Magnitude()
                if distanceFromThisShoop < Constants.SHEEP_NEIGHBOR_RADIUS:
                    totalPoint = totalPoint + thisShoop.position
                    neighborCount += 1

        if neighborCount != 0:
            totalPoint.x /= neighborCount
            totalPoint.y /= neighborCount
            totalPoint = totalPoint - self.position
            totalPoint = totalPoint.Normalized().Scale(Constants.SHEEP_COHESION_WEIGHT)

        return totalPoint


    # Gets social anxiety
    def GetSeparationVector(self, inputNeighborList):
        totalVector = Vector2(0, 0)
        neighborCount = 0

        for thisShoop in inputNeighborList:
            if thisShoop != self:
                distanceFromThisShoop = (self.position - thisShoop.position).Magnitude()
                if distanceFromThisShoop < Constants.SHEEP_NEIGHBOR_RADIUS:
                    totalVector = totalVector + (thisShoop.position - self.position)
                    neighborCount += 1

        if neighborCount != 0:
            totalVector.x /= neighborCount
            totalVector.y /= neighborCount
            totalVector = totalVector.Scale(-1)
            totalVector = totalVector.Normalized().Scale(Constants.SHEEP_SEPARATION_WEIGHT)

        return totalVector


    # Develops phobia of walls
    def GetBoundsForceVector(self):
        boundaryForce = Vector2(0, 0)

        if self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce.x = 1
        if Constants.WORLD_WIDTH - self.center.x < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce.x = -1
        if self.center.y < Constants.SHEEP_BOUNDARY_RADIUS:
            boundaryForce.y = 1
        if Constants.WORLD_HEIGHT - self.center.y < 50:
            boundaryForce.y = -1

        boundaryForce = boundaryForce.Normalized().Scale(Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT)

        if Constants.BOUNDARY_FORCES_LINES_ON:
            self.linesToDrawList.append(boundaryForce)

        return boundaryForce



    def GetObstaclesForceVector(self, inputGraph):
        forceToAdd = Vector2(0, 0)
        for thisObstacle in inputGraph.obstacles:
            distFromSheep = (thisObstacle.center - self.center).Magnitude()
            if distFromSheep < Constants.SHEEP_OBSTACLE_RADIUS:
                forceToAdd = forceToAdd + (self.center - thisObstacle.center).Normalized().Scale(Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT)

        return forceToAdd