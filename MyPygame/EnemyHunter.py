#####################################################
# Author: Dylan 
# Date: 02/15/20
# Email: dupdegra@uccs.edu
# 
# Is an even scarier and smarter rectangle
#####################################################

import pygame
from Vector2 import Vector2
import Constants
from Agent import Agent
from Enemy import Enemy

class EnemyHunter(Enemy):
    """I'm smart and spoooky"""

    
    def __init__(self, inputPos, inputSpeed, inputSize):
        super().__init__(inputPos, inputSpeed, inputSize)
        self.color = Constants.HUNTER_COLOR
        self.originalColor = self.color

    def CalculateVelocity(self, inputPlayer):
        distToPlayer = (inputPlayer.position - self.position).Magnitude();
        if distToPlayer < Constants.MIN_ATTACK_DIST:
            framesToGetToPlayer = distToPlayer / self.maxSpeed
            self.targetPos = inputPlayer.position + (inputPlayer.velocity).Scale(framesToGetToPlayer)
            direction = (self.targetPos - self.position).Normalized()
            self.velocity = direction.Scale(self.maxSpeed)
        else:
            self.velocity = Vector2(0, 0)