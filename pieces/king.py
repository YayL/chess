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

    def castle(self, y, x, diff):
        if diff == 2:  # Short castle
            for i in range(1,3):
                if self.tiles.list[self.row][self.col+i] != '': return False
            if type(self.tiles.list[self.row][7]).__name__ == 'Rook' and not self.tiles.list[self.row][7].hasMoved:
                return True
        else:  # Long castle
            for i in range(1,4):
                if self.tiles.list[self.row][self.col-i] != '': return False
            if type(self.tiles.list[self.row][0]).__name__ == 'Rook' and not self.tiles.list[self.row][0].hasMoved:
                return True
        return False

    def isLegalMove(self, y, x, isMovingPiece=False):
        xDiff, yDiff = x-self.col, y-self.row
        if abs(xDiff) <= 1 and abs(yDiff) <= 1:
            if self.row == y or self.col == x: return True
            if yDiff == xDiff or yDiff == -1 * xDiff: return True
        elif (xDiff == 2 or xDiff == -2) and yDiff == 0 and not self.hasMoved:
            return self.castle(y, x, xDiff)
        return False

    def render(self, x, y):
        x, y = self.tiles.getCoords(x, y)

        rotImg = pygame.transform.rotate(self.king[self.color], 0)
        img = self.king[self.color].get_rect(center=self.king[self.color].get_rect(topleft=(x+3, y)).center)
        self.win.blit(rotImg, img.topleft)
