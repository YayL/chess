import pygame

from pieces.pieces import Pieces


class Pawn(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color

    def isLegalMove(self, y, x):
        xDiff = x-self.col
        yDiff = y-self.row
        target = self.tiles.list[y][x]
        if xDiff == 0:  # Moving normally
            if self.isBetween(y, x, self): return False
            if type(target) is str:
                if self.color == (-0.5*yDiff)+0.5: return True
                elif (yDiff == 2 and self.color == 0 and self.row == 1) or (yDiff == -2 and self.color == 1 and self.row == 6): return True
        elif xDiff == 1 or xDiff == -1:  # Diagonal taking
            if type(target) is not str and target.color != self.color:
                if yDiff == (-2*self.color)+1: return True
        return False

    def render(self):
        x, y = self.tiles.getCoords(self.row, self.col)

        rotImg = pygame.transform.rotate(self.pawn[self.color], 0)
        img = self.pawn[self.color].get_rect(center=self.pawn[self.color].get_rect(topleft=(x+2, y)).center)
        self.win.blit(rotImg, img.topleft)