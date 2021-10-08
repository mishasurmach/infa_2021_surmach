import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((320, 450))

### библиотека функций
def draw_blackhouse(x, y, size, alpha_constant):
    '''
    Функция рисует черные дома на экране с заданной прозрачностью.
    x, y - координаты верхней левой точки дома (int)
    size - размер дома (int)
    alpha_constant - константа розрачности (int)
    '''
    black_houses_surface = pygame.Surface((320, 450))
    black_houses_surface.set_alpha(alpha_constant)
    rect(black_houses_surface, [0, 0, 0], (x, y, int(68 * size), int(282 * size)))
    screen.blit(black_houses_surface, (x, y))

def draw_blackcloud(x, y, size, alpha_constant):
    '''
    Функция рисует черные облака на экране с заданной прозрачностью.
    x, y - координаты верхней левой точки облака (int)
    size - размер облака (int)
    alpha_constant - константа розрачности (int)
    '''
    black_clouds_surface = pygame.Surface((320, 450))
    black_clouds_surface.set_alpha(alpha_constant)
    ellipse(black_clouds_surface, [0, 0, 0], (x, y, int(275 * size), int(75 * size)))
    screen.blit(black_clouds_surface, (x, y))

def draw_background(surface_for_back_clouds, surface_for_houses, x, y, size, direction):
    '''
    Функция рисует жилищный комплекс на экране.
    surface_for_houses - поверхность, на которой будет отображен комплекс.
    surface_for_back_clouds - поверхность, на которой будет отображено облако между домами.
    x, y - координаты верхней левой точки комплекса (int)
    size - размер комплекса (int)
    direction - направление, в котором будети нарисован комплекс (string)
    direction может принимать два значения: 'forward' - прямое направление, 'backward' - обратное направление.
    '''
    if direction is 'forward':
        rect(surface_for_houses, [183, 196, 200], (x, y, int(320 * size), int(290 * size)))
        ellipse(surface_for_back_clouds, [148, 166, 166], (x - int(100 * size), y - int(40 * size), int(275 * size), int(75 * size)))
        rect(screen, (250, 250, 250), (x, y, int(320 * size), int(290 * size)), int(2 * size))

        screen.blit(surface_for_back_clouds, (x, y))

        rect(surface_for_houses, [147, 167, 172], (x + int(8 * size), y + int(12 * size), int(68 * size), int(282 * size)))
        rect(surface_for_houses, [147, 172, 167], (x + int(85 * size), y + int(26 * size), int(66 * size), int(276 * size)))
        rect(surface_for_houses, [183, 200, 196], (x + int(53 * size), y + int(67 * size), int(71 * size), int(272 * size)))
        rect(surface_for_houses, [219, 227, 226], (x + int(240 * size), y + int(9 * size), int(72 * size), int(291 * size)))
        rect(surface_for_houses, [111, 145, 138], (x + int(213 * size), y + int(82 * size), int(65 * size), int(265 * size)))
    elif direction is 'backward':
        rect(surface_for_houses, [183, 196, 200], (x, y, int(320 * size), int(290 * size)))
        ellipse(surface_for_back_clouds, [148, 166, 166], (x - int(100 * size), y - int(40 * size), int(275 * size), int(75 * size)))
        rect(screen, (250, 250, 250), (x, y, int(320 * size), int(290 * size)), int(2 * size))

        screen.blit(surface_for_back_clouds, (x, y))

        rect(surface_for_houses, [147, 167, 172], (x + int(258 * size), y + int(12 * size), int(68 * size), int(282 * size)))
        rect(surface_for_houses, [147, 172, 167], (x + int(185 * size), y + int(26 * size), int(66 * size), int(276 * size)))
        rect(surface_for_houses, [183, 200, 196], (x + int(233 * size), y + int(67 * size), int(71 * size), int(272 * size)))
        rect(surface_for_houses, [219, 227, 226], (x + int(5 * size), y + int(25 * size), int(72 * size), int(291 * size)))
        rect(surface_for_houses, [111, 145, 138], (x + int(43 * size), y + int(90 * size), int(65 * size), int(265 * size)))

def draw_car(surface, x, y, size, direction):
    '''
    Функция рисует машину на экране.
    surface - поверхность, на которой будет отображена машина.
    x, y - координаты верхней левой точки наибольшего прямоугольника, образовывающего машину. (int)
    size - размер машины (int)
    direction - направление, в котором будети нарисована машина (string)
    direction может принимать два значения: 'forward' - прямое направление, 'backward' - обратное направление.
    '''
    if direction is 'forward':
        ellipse(surface, [0, 0, 0], (int(x - 10 * size), int(y + 10 * size), int(15 * size), int(3 * size)))
        rect(surface, [0, 200, 250], (int(x), int(y), int(135 * size), int(20 * size)))
        rect(surface, [0, 200, 250], (int(x + 25 * size), int(y - 13 * size), int(66 * size), int(15 * size)))
        rect(surface, [210, 245, 255], (int(x + 30 * size), int(y - 10 * size), int(19 * size), int(10 * size)))
        rect(surface, [210, 245, 255], (int(x + 65 * size), int(y - 10 * size), int(19 * size), int(10 * size)))
        ellipse(surface, [0, 0, 0], (int(x + 10 * size), int(y + 10 * size), int(25 * size), int(20 * size)))
        ellipse(surface, [0, 0, 0], (int(x + 100 * size), int(y + 10 * size), int(25 * size), int(20 * size)))
    elif direction is 'backward':
        ellipse(surface, [0, 0, 0], (int(x + 127 * size), int(y + 10 * size), int(15 * size), int(3 * size)))
        rect(surface, [0, 200, 250], (int(x), int(y), int(135 * size), int(20 * size)))
        rect(surface, [0, 200, 250], (int(x + 50 * size), int(y - 13 * size), int(66 * size), int(15 * size)))
        rect(surface, [210, 245, 255], (int(x + 90 * size), int(y - 10 * size), int(19 * size), int(10 * size)))
        rect(surface, [210, 245, 255], (int(x + 56 * size), int(y - 10 * size), int(19 * size), int(10 * size)))
        ellipse(surface, [0, 0, 0], (int(x + 10 * size), int(y + 10 * size), int(25 * size), int(20 * size)))
        ellipse(surface, [0, 0, 0], (int(x + 100 * size), int(y + 10 * size), int(25 * size), int(20 * size)))

def draw_smoke(surface, R, G, B, x, y, size):
    '''
    Функция рисует градиентное облако дыма на экране.
    R, G, B - компоненты цвета, заданного в RGB.
    surface - поверхность, на которой будет отображено облако дыма.
    x, y - координаты верхней левой точки облака дыма. (int)
    size - размер облака дыма (int)
    '''
    for i in range (250, 1, -1 ):
        smoke_surface = pygame.Surface((320, 450))
        smoke_surface.set_alpha(60 - i * 60 / 200)
        ellipse(smoke_surface, [R, G, B], (0, 0, int((2 * i) * size), int((i)  * size)), int(6  * size))
        screen.blit(smoke_surface, (x - int(i * size), y -int((i / 2) * size)))
###

###основа рисунка
back_clouds_surface = pygame.Surface((320, 450))
back_clouds_surface.set_alpha(120)

front_clouds_surface = pygame.Surface((320, 450))
front_clouds_surface.set_alpha(120)

screen.fill([150, 150, 150])
###

### рисование объектов    
draw_blackhouse(-50, -30, 2, 25)
draw_blackhouse(0, 30, 1, 100)
draw_blackhouse(55, 5, 1, 60)
draw_blackhouse(65, 25, 1.5, 70)
draw_blackhouse(80, 0, 2, 40)
draw_blackhouse(155, 0, 1.8, 190)
draw_blackhouse(85, 0, 1.4, 90)
draw_blackhouse(100, 0, 0.5, 200)

draw_blackcloud(-40, -10, 0.9, 30)
draw_blackcloud(20, 5, 0.8, 50)
draw_blackcloud(50, -15, 1, 15)
draw_blackcloud(140, 35, 0.5, 60)

rect(screen, [83, 108, 103], (0, 290, 320, 160))

draw_background(back_clouds_surface, screen, 120, 100, 0.7, 'backward')
draw_background(back_clouds_surface, screen, -50, 110, 0.7, 'forward')

draw_car(screen, 18, 344, 0.4, 'backward')
draw_car(screen, 119, 348, 0.4, 'backward')
draw_car(screen, 182, 345, 0.4, 'backward')
draw_car(screen, 252, 356, 0.4, 'backward')
draw_car(screen, 27, 372, 1, 'forward')
draw_car(screen, 164, 412, 1, 'backward')

draw_smoke(screen, 170, 170, 170, 150, 390, 1)
draw_smoke(screen, 170, 190, 190, 30, 200, 0.5)
draw_smoke(screen, 170, 190, 190, 300, 150, 0.5)
draw_smoke(screen, 250, 250, 250, -10, -10, 0.5)

screen.blit(front_clouds_surface, (0, 0))
###

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
