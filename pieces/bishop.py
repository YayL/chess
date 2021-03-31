import pygame

from pieces.pieces import Pieces


class Bishop(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color

    def isLegalMove(self, y, x):
        if y - self.row == x - self.col or y - self.row == -1*(x - self.col): return True
        return False

    def render(self):
        x, y = self.tiles.getCoords(self.row, self.col)

        rotImg = pygame.transform.rotate(self.bishop[self.color], 0)
        img = self.bishop[self.color].get_rect(center=self.bishop[self.color].get_rect(topleft=(x+2, y)).center)
        self.win.blit(rotImg, img.topleft)
