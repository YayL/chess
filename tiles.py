import pygame
import math

from board import Board


class Tiles(Board):

    def __init__(self, win, width, height):
        super().__init__(win, self, width, height)
        self.list = [['' for i in range(8)] for j in range(8)]
        self.tileColors = [(235, 235, 208) , (119, 148, 85)] # 1) Light squares 2) Dark squares
        self.selectedTile = [-1, -1]

    def getTile(self, x, y):
        return 7 - math.floor(y/(int(self.height/8))), math.floor(x/int(self.width/8))

    def getCoords(self, row, col):
        return col*self.width/8, (7-row)*self.height/8

    def render(self):
        w, h, inc = int(self.width/8), int(self.height / 8), 0
        for x in range(0, self.width, w):
            inc += 1
            for y in range(0, self.height, h):
                if inc % 2 == 0:
                    pygame.draw.rect(self.win, self.tileColors[1], (x, y, w, h))
                else:
                    pygame.draw.rect(self.win, self.tileColors[0], (x, y, w, h))
                inc += 1
        self.renderBoard()

