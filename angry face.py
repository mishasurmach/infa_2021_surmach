import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill([130, 130, 130])

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (250, 180), 20)
circle(screen, (255, 0, 0), (150, 180), 25)
circle(screen, (0, 0, 0), (250, 180), 10)
circle(screen, (0, 0, 0), (150, 180), 14)

circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (0, 0, 0), (250, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 25, 1)

polygon(screen, (0, 0, 0), [(150, 270), (250, 270), (250, 245), (150, 245)])
polygon(screen, (0, 0, 0), [(110, 110), (115, 105), (175, 160), (165, 165)])
polygon(screen, (0, 0, 0), [(310, 110), (305, 105), (210, 155), (215, 160)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
