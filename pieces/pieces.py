import os
import pygame
import re


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

    xCoords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def moveToPiece(self, piece, y, x, isTaking):
        returnValue = type(piece).__name__[0:1] if type(piece).__name__ != 'Knight' else 'N'
        if returnValue == 'P': returnValue = ''
        if returnValue == '' and isTaking: returnValue += self.xCoords[piece.col]
        if isTaking: returnValue += 'x'
        returnValue += self.xCoords[x]+str(y+1)
        return returnValue
