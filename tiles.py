import pygame
import math

from board import Board


class Tiles(Board):

    def __init__(self, win, width, height):
        super().__init__(win, self, width, height)
        self.list = [['' for i in range(8)] for j in range(8)]
        self.tileColors = [(235, 235, 208) , (119, 148, 85)] # 1) Light squares 2) Dark squares
        self.selectedTile = [-1, -1]
        self.validMoves = [[False for j in range(8)] for i in range(8)]

    def getTile(self, x, y):
        if self.flipped:
            return math.floor(y / (int(self.height / 8))), 7 - math.floor(x / int(self.width / 8))
        else:
            return 7 - math.floor(y / (int(self.height / 8))), math.floor(x / int(self.width / 8))

    def getCoords(self, row, col):
        if self.flipped:
            return (7-col)*self.width/8, row*self.height/8
        else:
            return col*self.width/8, (7-row)*self.height/8

    def updateValidMoves(self, piece, col, row):
        for x in range(8):
            for y in range(8):
                if piece.isLegalMove(y, x):
                    if not (type(self.list[y][x]) is not str and piece.color == self.list[y][x].color):
                        self.validMoves[x][y] = True
        self.overlay = pygame.Surface((self.width,self.height))

    def renderValidMoves(self):
        self.overlay.set_colorkey((0,0,0))
        self.overlay.set_alpha(128)
        hasValidMoves = False
        for i, x in enumerate(self.validMoves):
            for j, y in enumerate(x):
                if y:
                    xCoord, yCoord = self.getCoords(j, i)
                    xCoord, yCoord = xCoord + (self.width/(8*2)), yCoord + (self.width/(8*2))-2
                    pygame.draw.circle(self.overlay, (255, 0, 0), (xCoord, yCoord), int(self.width / (8 * 6)))
                    hasValidMoves = True
        if hasValidMoves:
            self.win.blit(self.overlay, (0, 0))

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
        self.renderValidMoves()

