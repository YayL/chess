import pygame

from pieces.pieces import Pieces


class King(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color
        self.hasMoved = False

    def isLegalMove(self, y, x):
        if x-self.col <= 1 and y-self.row <= 1:
            if self.row == y or self.col == x: return True
            if y - self.row == x - self.col or y - self.row == -1 * (x - self.col): return True
        return False

    def render(self):
        x, y = self.tiles.getCoords(self.row, self.col)

        rotImg = pygame.transform.rotate(self.king[self.color], 0)
        img = self.king[self.color].get_rect(center=self.king[self.color].get_rect(topleft=(x+3, y)).center)
        self.win.blit(rotImg, img.topleft)
