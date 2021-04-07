import os
import pygame


class Pieces:

    codes = {
        'pawn': 'P',
        'bishop': 'B',
        'knight': 'Kn',
        'rook': 'R',
        'queen': 'Q',
        'king': 'K'
    }

    c_keys = list(codes.keys())
    c_values = list(codes.values())

    def __init__(self, win):
        self.win = win
        self.pawn = [pygame.image.load(os.path.join('imgs', 'wP.png')),
                     pygame.image.load(os.path.join('imgs', 'bP.png'))]

        self.bishop = [pygame.image.load(os.path.join('imgs', 'wB.png')),
                       pygame.image.load(os.path.join('imgs', 'bB.png'))]

        self.knight = [pygame.image.load(os.path.join('imgs', 'wKn.png')),
                      pygame.image.load(os.path.join('imgs', 'bKn.png'))]

        self.rook = [pygame.image.load(os.path.join('imgs', 'wR.png')),
                     pygame.image.load(os.path.join('imgs', 'bR.png'))]

        self.queen = [pygame.image.load(os.path.join('imgs', 'wQ.png')),
                      pygame.image.load(os.path.join('imgs', 'bQ.png'))]

        self.king = [pygame.image.load(os.path.join('imgs', 'wK.png')),
                     pygame.image.load(os.path.join('imgs', 'bK.png'))]

    def isBetween(self, y, x, p):
        yDiff, xDiff, isBetween = y - p.row, x - p.col, False
        p_yInc = int(yDiff / abs(yDiff)) if yDiff != 0 else 0
        p_xInc = int(xDiff / abs(xDiff)) if xDiff != 0 else 0
        yInc, xInc = p_yInc, p_xInc
        diff = yDiff if xDiff == 0 else xDiff if yDiff == 0 else yDiff
        for i in range(abs(diff) - 1):
            if y-yInc > 7 or x-xInc > 7: break
            isBetween = bool(p.tiles.list[abs(y - yInc)][abs(x - xInc)] != '')
            if isBetween: break
            yInc, xInc = yInc + p_yInc, xInc + p_xInc
        return isBetween

    xCoords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def pieceToName(self, piece):
        if type(piece) is not str:
            return type(piece).__name__[0:1] if type(piece).__name__ != 'Knight' else 'N'
        return ''

    def movePiece(self, board, piece, col, row, retVal = False):
        board[piece.row][piece.col] = ''  # Clear old tile
        board[col][row] = piece  # Set selected piece to the new tile
        board[col][row].row, board[col][row].col = col, row  # Set the piece's col and row of the new tile
        if retVal: return board

    def checkIfInCheck(self, piece, xPos, yPos, tiles, king):
        copiedBoard = [tiles.list[i].copy() for i in range(8)]
        copiedBoard = self.movePiece(copiedBoard, piece, xPos, yPos, True)
        for y, val in enumerate(copiedBoard):
            for x, piece in enumerate(val):
                if type(piece) is not str and piece.color != king.color and piece.isLegalMove(king.row, king.col):
                    return True
        return False

    def notation(self, piece, y, x, isTaking):
        returnValue = type(piece).__name__[0:1] if type(piece).__name__ != 'Knight' else 'N'
        if returnValue == 'K':
            if x-piece.col == 2:
                self.movePiece(piece.tiles, piece.tiles.list[piece.row][7], piece.row, 5)
                return 'O-O'
            elif x-piece.col == -2:
                self.movePiece(piece.tiles, piece.tiles.list[piece.row][0], piece.row, 3)
                return 'O-O-O'
        if returnValue == 'P': returnValue = ''
        if returnValue == '' and isTaking: returnValue += self.xCoords[piece.col]
        if isTaking: returnValue += 'x'
        returnValue += self.xCoords[x]+str(y+1)
        return returnValue
