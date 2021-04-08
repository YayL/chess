import pygame

from pieces.pieces import Pieces
from pieces.queen import Queen

class Pawn(Pieces):

    def __init__(self, col, row, tiles, color):
        super().__init__(tiles.win)
        self.col = col
        self.row = row
        self.tiles = tiles
        self.color = color
        self.moveCount = 0
        self.longJump = False

    def promoting(self, yPos, xPos):
        self.tiles.list[yPos][xPos] = ''
        self.tiles.list[self.row][self.col] = Queen(xPos, yPos, self.tiles, self.color)
        print(self.tiles.list[self.row][self.col])
        print(self.row, self.col)
        return False

    def isLegalMove(self, y, x, isMovingPiece=False):
        xDiff = x-self.col
        yDiff = y-self.row
        target = self.tiles.list[y][x]
        retTrue = False
        if xDiff == 0:  # Moving normally
            if self.isBetween(y, x, self): return False
            if type(target) is str:
                if self.color == (-0.5*yDiff)+0.5: retTrue = True
                elif (yDiff == 2 and self.color == 0 and self.row == 1) or (yDiff == -2 and self.color == 1 and self.row == 6):
                    if isMovingPiece: self.longJump = True
                    retTrue = True
        elif xDiff == 1 or xDiff == -1:  # Diagonal taking
            if type(target) is not str and target.color != self.color:
                if yDiff == (-2*self.color)+1:
                    retTrue = True
            target = self.tiles.list[self.row][self.col+xDiff]
            if type(target) is not str and type(target).__name__ == 'Pawn' and target.color != self.color:
                if yDiff == (-2*self.color)+1 and target.moveCount == 1 and target.longJump:
                    if isMovingPiece: self.tiles.list[self.row][self.col+xDiff] = ''
                    retTrue = True

        if retTrue:
            if isMovingPiece:
                self.moveCount += 1
                if self.row + yDiff == 0 or self.row + yDiff == 7: return self.promoting(self.row + yDiff,
                                                                                         self.col + xDiff)
            return True
        return False

    def render(self, x, y):
        x, y = self.tiles.getCoords(x, y)

        rotImg = pygame.transform.rotate(self.pawn[self.color], 0)
        img = self.pawn[self.color].get_rect(center=self.pawn[self.color].get_rect(topleft=(x+2, y)).center)
        self.win.blit(rotImg, img.topleft)
