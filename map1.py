import pygame
from pytmx.util_pygame import load_pygame
import os
import math

pygame.init()
size = width, height = 1200, 960
screen = pygame.display.set_mode(size)
running = True
global s, flag, choice_hero, hero, error_tail, way
s = [[2, 4], [3, 3], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2], [13, 2], [14, 2],
     [15, 2], [16, 3], [16, 5], [15, 6], [14, 6], [13, 6], [12, 6], [11, 6], [10, 6], [9, 6], [8, 6], [7, 6], [6, 6],
     [5, 6], [4, 6], [3, 5], [5, 14], [6, 15], [7, 16], [7, 17], [7, 19], [7, 20], [7, 21], [7, 22], [7, 23], [7, 24],
     [7, 25], [6, 26], [5, 27], [4, 26], [3, 25], [3, 24], [3, 23], [3, 22], [3, 21], [3, 20], [3, 19], [3, 18],
     [3, 17], [3, 16], [4, 15], [5, 14], [9, 11], [9, 10], [9, 9], [13, 10], [13, 11], [13, 12], [14, 12], [15, 12],
     [14, 10], [15, 10], [18, 14], [18, 15], [18, 16], [17, 19], [16, 19], [15, 19], [14, 20], [14, 21], [14, 23],
     [14, 24], [15, 25], [16, 25], [17, 25], [18, 24], [18, 23], [18, 22], [18, 21], [18, 20], [22, 6], [22, 7],
     [23, 7], [23, 6], [24, 18], [24, 19], [25, 19], [25, 18]]
flag = [2000, 2000]
choice_hero = [26, 11]
hero = 0
error_tail = 0
way = 0

tmxdata = load_pygame("data/map1.tmx")
tmxdata1 = load_pygame("data/Текстуры/red.tmx")


class XCOM:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = 32

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(30):
            for y in range(30):
                if hero == 1:
                    screen.blit(menu, (960, 0))
                    screen.blit(support, (choice_hero[1] * 32, choice_hero[0] * 32))
                else:
                    screen.blit(support, (choice_hero[1] * 32, choice_hero[0] * 32))
                if x == flag[1] and y == flag[0]:
                    screen.blit((tmxdata1.get_tile_image(0, 0, 0)), (flag[1] * 32, flag[0] * 32))
                else:
                    screen.blit((tmxdata.get_tile_image(x, y, 0)), (x * 32, y * 32))
                if error_tail == 1:
                    screen.blit((tmxdata1.get_tile_image(0, 0, 0)), (s1[1] * 32, s1[0] * 32))

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.width * self.cell_size and\
                mouse_pos[1] < self.height * self.cell_size:
            x = (mouse_pos[0]) // self.cell_size
            y = (mouse_pos[1]) // self.cell_size
            return y, x
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        if cell != None:
            print(cell[0], cell[1])


def load_image1(name):
    fullname = os.path.join('data/Текстуры', name)
    image = pygame.image.load(fullname).convert()
    return image


def load_image(name):
    fullname = os.path.join('data/Текстуры', name)
    image = pygame.image.load(fullname)
    return image


def way(x, y, x1, y1, s):
    if x != x1 and y != y1:
        f = 0
        for l in range(abs(y - y1)):
            for k in range(abs(x - x1)):
                if [l, k] in s:
                    f = 1
            if f == 0:
                return math.sqrt((x - x1)**2 + (y - y1)**2)
    else:
        g = 0
        for l in range(abs(y - y1)):
            for k in range(abs(x - x1)):
                if [l, k] in s:
                    g = 1
            if g == 0:
                if x == x1:
                    return abs(y - y1)
                elif y == y1:
                    return abs(x - x1)


board = XCOM(30, 30)
running = True
clock = pygame.time.Clock()
menu = load_image1('menut.png')
support = load_image('Heavy_support.png')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
                s1 = [board.get_cell(event.pos)[0], board.get_cell(event.pos)[1]]
                if s1 in s:
                    flag = s1
                if s1 == choice_hero:
                    if s1 not in s:
                        hero = 1
                        error_tail = 0
                        choice_hero = s1
                if s1 != choice_hero and hero == 1:
                    if s1 not in s and way():
                        choice_hero = s1
                        hero = 0
                        error_tail = 0
                        flag[0] = flag[0] + 1000
                    else:
                        print(1)
                        error_tail = 1

    screen.fill((0, 0, 0))
    board.render()
    clock.tick(10)
    pygame.display.flip()

