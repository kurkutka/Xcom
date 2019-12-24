from pytmx.util_pyglet import pyglet_image_loader
from pytmx.util_pygame import load_pygame
import pygame

pygame.init()
size = width, height = 960, 960
screen = pygame.display.set_mode(size)

tmxdata = load_pygame("main.tmx")


class Board:
    def render(self):
        for x in range(30):
            for y in range(30):
                screen.blit((tmxdata.get_tile_image(x, y, 0)), (x * 32, y * 32))


board = Board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()