print ("My project is working!")
print ("Boshhhhh")
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Board Game Test")

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 150, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 200, 150))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
