import pygame
import Vector2
import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

#xPos = 120
#yPos = 30
clock = pygame.time.Clock()


#-=TESTING=-
testVector = Vector2.Vector2(3, 4)
testVectorA = Vector2.Vector2(1, 1)
testVectorB = testVector - testVectorA
print(testVector.normalized())
#-=TESTING=-

playerPos = Vector2.Vector2(50, 50)
myPlayer = Player.Player(playerPos, playerPos, 50)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        

        screen.fill((100, 149, 237))

        myPlayer.update()
        myPlayer.draw(screen)

        pygame.display.flip()
        clock.tick(60)