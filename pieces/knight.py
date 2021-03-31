import pygame

from pieces.pieces import Pieces


class Knight(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color

    def isLegalMove(self, y, x):
        yDiff = abs(y-self.row)
        xDiff = abs(x-self.col)
        if yDiff == 2 and xDiff == 1: return True
        if yDiff == 1 and xDiff == 2: return True
        return False

    def render(self):
        x, y = self.tiles.getCoords(self.row, self.col)

        rotImg = pygame.transform.rotate(self.knight[self.color], 0)
        img = self.knight[self.color].get_rect(center=self.knight[self.color].get_rect(topleft=(x+1, y)).center)
        self.win.blit(rotImg, img.topleft)
