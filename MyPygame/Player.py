import pygame
import Vector2

class Player(object):
    """The playa"""

    def __init__(self, inputPosition, inputVelocity, inputSize):
        self.position = inputPosition
        self.velocity = inputVelocity
        self.size = inputSize
        self.speed = 10


    def draw(self, inputScreen):
        myRect = pygame.draw.rect(inputScreen, (0, 0, 255), pygame.Rect(self.position.x, self.position.y, self.size, self.size))
        
        libtardRect = pygame.draw.rect(inputScreen, (0, 255, 0), pygame.Rect(400, 300, 40, 40))
        if libtardRect.colliderect(myRect):
            pygame.draw.rect(inputScreen, (0, 255, 0), pygame.Rect(500, 400, 40, 40))
            pass

        scaledUpVelocity = self.velocity.scale(10)
        middlePosition = self.position + Vector2.Vector2(self.size * 0.5, self.size * 0.5)
        pygame.draw.line(inputScreen, (255, 0, 0), (middlePosition.x, middlePosition.y), (middlePosition.x + scaledUpVelocity.x, middlePosition.y + scaledUpVelocity.y), 3)


    def update(self):
        self.velocity = Vector2.Vector2(0, 0)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] : self.velocity.y = -1
        if pressed[pygame.K_s] : self.velocity.y = 1
        if pressed[pygame.K_a] : self.velocity.x = -1
        if pressed[pygame.K_d] : self.velocity.x = 1
        
        self.velocity = self.velocity.normalized()
        self.velocity = self.velocity.scale(5)
        self.position = self.position + self.velocity