import pygame

from tiles import Tiles
import input

width, height = 520, 480


def render(tiles):
    pygame.display.update()
    tiles.render()


def start(tiles):
    running = True
    tiles.setupBoard()
    while running:
        render(tiles)
        running = input.eventCheck(tiles)


def init():
    win = pygame.display.set_mode((width, height))
    tiles = Tiles(win, width, height)
    start(tiles)


if __name__ == '__main__':
    init()
