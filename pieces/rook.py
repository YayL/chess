import pygame

from pieces.pieces import Pieces


class Rook(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color
        self.hasMoved = False

    def isLegalMove(self, y, x, isMovingPiece=False):
        if not self.isBetween(y, x, self) and (self.row == y or self.col == x): return True
        return False

    def render(self, x, y):
        x, y = self.tiles.getCoords(x, y)

        rotImg = pygame.transform.rotate(self.rook[self.color], 0)
        img = self.rook[self.color].get_rect(center=self.rook[self.color].get_rect(topleft=(x+1, y+1)).center)
        self.win.blit(rotImg, img.topleft)