import pygame

from pieces.pieces import Pieces
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King


class Board:

    def __init__(self, win, tiles, width, height):
        self.win = win
        self.overlay = pygame.Surface((width,height))
        self.tiles = tiles
        self.pieces = Pieces(win)
        self.width = width
        self.height = height
        self.colorToMove = 0
        self.flipped = False
        self.flipOnEveryMove = False
        self.tempBoard = []
        self.kings = [King(4, 0, self.tiles, 0), King(4, 7, self.tiles, 1)]
        self.previousBoards = []
        self.moves = []

    def setupBoard(self):
        self.tiles.list = [
            [Rook(0, 0, self.tiles, 0), Knight(1, 0, self.tiles, 0), Bishop(2, 0, self.tiles, 0), Queen(3, 0, self.tiles, 0), self.kings[0], Bishop(5, 0, self.tiles, 0), Knight(6, 0, self.tiles, 0), Rook(7, 0, self.tiles, 0)],
            [Pawn(x, 1, self.tiles, 0) for x in range(8)],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            [Pawn(x, 6, self.tiles, 1) for x in range(8)],
            [Rook(0, 7, self.tiles, 1), Knight(1, 7, self.tiles, 1), Bishop(2, 7, self.tiles, 1), Queen(3, 7, self.tiles, 1), self.kings[1], Bishop(5, 7, self.tiles, 1), Knight(6, 7, self.tiles, 1), Rook(7, 7, self.tiles, 1)],
        ]

    def renderBoard(self):
        for x, arr in enumerate(self.tiles.list):
            for y, val in enumerate(arr):
                if type(val) is not str:
                    val.render(x, y)

