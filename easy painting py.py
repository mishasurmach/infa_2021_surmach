import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((320, 450))

back_clouds_surface = pygame.Surface((320, 450))
back_clouds_surface.set_alpha(120)

front_clouds_surface = pygame.Surface((320, 450))
front_clouds_surface.set_alpha(120)

#фон
screen.fill([183, 196, 200])
rect(screen, [83, 108, 103], (0, 290, 320, 160))
ellipse(screen, [183, 200, 196], (-50, 375, 500, 150))
ellipse(back_clouds_surface, [148, 166, 166], (-100, 180, 275, 75))
ellipse(back_clouds_surface, [148, 166, 166], (-90, 25, 315, 75))
line(screen, (250, 250, 250), (0, 290), (320, 290), 2)

screen.blit(back_clouds_surface, (0, 0))

#машина
ellipse(screen, [0, 0, 0], (115, 400, 15, 3))
rect(screen, [0, 200, 250], (125, 390, 135, 20))
rect(screen, [0, 200, 250], (150, 375, 66, 15))
rect(screen, [210, 245, 255], (155, 380, 19, 10))
rect(screen, [210, 245, 255], (190, 380, 19, 10))
ellipse(screen, [0, 0, 0], (135, 400, 25, 20))
ellipse(screen, [0, 0, 0], (225, 400, 25, 20))

#дома
rect(screen, [147, 167, 172], (8, 12, 68, 282))
rect(screen, [147, 172, 167], (85, 26, 66, 276))
rect(screen, [183, 200, 196], (53, 67, 71, 272))
rect(screen, [219, 227, 226], (240, 9, 72, 291))
rect(screen, [111, 145, 138], (213, 82, 65, 265))

#передние тучи и выхлопные газы
ellipse(front_clouds_surface, [148, 166, 166], (70, 110, 315, 73))
ellipse(front_clouds_surface, [148, 166, 166], (73, -5, 315, 73))
ellipse(front_clouds_surface, [148, 166, 166], (28, 386, 81, 24))
ellipse(front_clouds_surface, [148, 166, 166], (25, 356, 81, 24))
ellipse(front_clouds_surface, [148, 166, 166], (-35, 326, 81, 24))


screen.blit(front_clouds_surface, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
