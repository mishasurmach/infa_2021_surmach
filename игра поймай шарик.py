import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

### библиотека цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
###

### функции
def new_ball():
    ''' создание шариков '''
    global ball_x, ball_y, ball_r
    ball_x = randint(100,700)
    ball_y = randint(100,500)
    ball_r = randint(150,250)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (ball_x, ball_y), ball_r)
    
def click(event):
    ''' возвратить значения координат мяча'''
    return(ball_x, ball_y, ball_r)
###

pygame.display.update()
clock = pygame.time.Clock()
finished = False

### основное событие
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click(event)
                if ((event.pos[0] - ball_x) ** 2 + (event.pos[1] - ball_y) ** 2 < ball_r ** 2):
                    print('попал')

                    
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
###
    
pygame.quit()
