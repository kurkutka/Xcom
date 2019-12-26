import pygame
from pytmx.util_pygame import load_pygame
import os
import math
from move import Move

pygame.init()
size = width, height = 1200, 960
screen = pygame.display.set_mode(size)
running = True
global s, flag, choice_hero, hero, error_tail, way, choice_hero1, choice_hero2, choice_hero3, flag_turn, flag_turn1, \
    flag_turn2, flag_turn3, turn_enemy
s = [[2, 4], [2, 5], [2, 3], [3, 3], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2],
     [13, 2], [14, 2], [15, 2], [16, 2], [16, 3], [16, 5], [16, 6], [15, 6], [14, 6], [13, 6], [12, 6], [11, 6],
     [10, 6], [8, 6], [9, 6], [7, 6], [6, 6], [5, 6], [4, 6], [3, 6], [2, 5], [3, 5], [7, 6], [9, 9], [9, 10], [9, 11],
     [18, 14], [18, 15], [18, 16], [15, 12], [14, 12], [13, 12], [13, 11], [13, 10], [14, 10], [15, 10], [14, 19],
     [15, 19], [16, 19], [17, 19], [18, 19], [18, 20], [18, 21], [18, 22], [18, 22], [18, 23], [18, 24], [18, 25],
     [17, 25], [16, 25], [15, 25], [14, 25], [14, 24], [14, 23], [14, 21], [14, 21], [14, 20], [14, 19], [7, 26],
     [6, 26], [6, 27], [5, 27], [4, 27], [4, 26], [3, 26], [3, 25], [3, 24], [3, 23], [3, 22], [3, 21], [3, 20],
     [3, 19], [3, 18], [3, 17], [3, 16], [3, 15], [4, 15], [4, 14], [5, 14], [6, 14], [6, 15], [7, 15], [7, 16],
     [7, 17], [7, 19], [7, 20], [7, 21], [7, 21], [7, 22], [7, 23], [7, 24], [7, 25], [7, 25], [18, 14], [18, 15],
     [18, 16], [24, 19], [25, 19], [25, 18], [24, 18], [22, 7], [23, 7], [23, 6], [22, 6]]
flag = [2000, 2000]
hero = 0
error_tail = 0
way = 0
choice_hero = [26, 11]  # саппорт
choice_hero1 = [26, 10]  # штурмовик
choice_hero2 = [27, 9]   # снайпер
choice_hero3 = [27, 12]  # медик
flag_turn = 0  # флаг хода саппорта
flag_turn1 = 0  # флаг хода штурмовика
flag_turn2 = 0  # флаг хода снайпера
flag_turn3 = 0  # флаг хода медика
turn_enemy = 0  # флаг хода клятых алиенов

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
                screen.blit(support, (choice_hero[1] * 32, choice_hero[0] * 32))
                screen.blit(eng, (choice_hero1[1] * 32, choice_hero1[0] * 32))
                screen.blit(sniper, (choice_hero2[1] * 32, choice_hero2[0] * 32))
                screen.blit(medic, (choice_hero3[1] * 32, choice_hero3[0] * 32))
                if hero == 1:
                    screen.blit(menu, (960, 0))
                elif hero == 2:
                    screen.blit(menu, (960, 0))
                elif hero == 3:
                    screen.blit(menu, (960, 0))
                elif hero == 4:
                    screen.blit(menu, (960, 0))
                if x == flag[1] and y == flag[0]:
                    screen.blit((tmxdata1.get_tile_image(0, 0, 0)), (flag[1] * 32, flag[0] * 32))
                else:
                    screen.blit((tmxdata.get_tile_image(x, y, 0)), (x * 32, y * 32))
                if error_tail == 1:
                    screen.blit((tmxdata1.get_tile_image(0, 0, 0)), (s1[1] * 32, s1[0] * 32))

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.width * self.cell_size and \
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
            pass


def load_image1(name):
    fullname = os.path.join('data/Текстуры', name)
    image = pygame.image.load(fullname).convert()
    return image


def load_image(name):
    fullname = os.path.join('data/Текстуры', name)
    image = pygame.image.load(fullname)
    return image


board = XCOM(30, 30)
running = True
clock = pygame.time.Clock()
global_menu = load_image1('global_menu.png')
menu = load_image1('menut.png')
support = load_image('Heavy_support.png')
eng = load_image('Engeniiiiiier.png')
sniper = load_image('sniper.png')
medic = load_image('medic.png')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
                if event.pos[0] <= 1024 and event.pos[1] <= 1024:
                    s1 = [board.get_cell(event.pos)[0], board.get_cell(event.pos)[1]]
                if s1 in s:
                    flag = s1
                if s1 == choice_hero:  # support
                    if s1 not in s:
                        hero = 1
                        error_tail = 0
                        choice_hero = s1
                if s1 != choice_hero and hero == 1:
                    if s1 not in s and Move.way(Move(), s, choice_hero[1], choice_hero[0], s1[1], s1[0]) \
                            and flag_turn != 2 and s1 != choice_hero2 and s1 != choice_hero3 and s1 != choice_hero1:
                        choice_hero = s1
                        hero = 0
                        flag_turn += 1
                        error_tail = 0
                        flag[0] = flag[0] + 1000
                    else:
                        error_tail = 1
                if s1 == choice_hero1:  # eng
                    if s1 not in s:
                        hero = 2
                        error_tail = 0
                        choice_hero1 = s1
                if s1 != choice_hero1 and hero == 2:
                    if s1 not in s and Move.way(Move(), s, choice_hero1[1], choice_hero1[0], s1[1], s1[0]) \
                            and flag_turn1 != 2 and s1 != choice_hero2 and s1 != choice_hero and s1 != choice_hero3:
                        choice_hero1 = s1
                        hero = 0
                        flag_turn1 += 1
                        error_tail = 0
                        flag[0] = flag[0] + 1000
                    else:
                        error_tail = 1

                if s1 == choice_hero2:  # sniper
                    if s1 not in s:
                        hero = 3
                        error_tail = 0
                        choice_hero2 = s1
                if s1 != choice_hero2 and hero == 3:
                    if s1 not in s and Move.way(Move(), s, choice_hero2[1], choice_hero2[0], s1[1], s1[0]) \
                            and flag_turn2 != 2 and s1 != choice_hero3 and s1 != choice_hero and s1 != choice_hero1:
                        choice_hero2 = s1
                        hero = 0
                        error_tail = 0
                        flag_turn2 += 1
                        flag[0] = flag[0] + 1000
                    else:
                        error_tail = 1

                if s1 == choice_hero3:  # medic
                    if s1 not in s:
                        hero = 4
                        error_tail = 0
                        choice_hero3 = s1
                if s1 != choice_hero3 and hero == 4:
                    if s1 not in s and Move.way(Move(), s, choice_hero3[1], choice_hero3[0], s1[1], s1[0]) \
                            and flag_turn3 != 2 and s1 != choice_hero2 and s1 != choice_hero and s1 != choice_hero1:
                        choice_hero3 = s1
                        hero = 0
                        error_tail = 0
                        flag_turn3 += 1
                        flag[0] = flag[0] + 1000
                    else:
                        error_tail = 1
                if event.pos[0] > 1100 and event.pos[1] > 870:
                    flag_turn = 0
                    flag_turn1 = 0
                    flag_turn2 = 0
                    flag_turn3 = 0
                    turn_enemy = 0

    screen.fill((0, 0, 0))
    board.render()
    clock.tick(10)
    pygame.display.flip()
