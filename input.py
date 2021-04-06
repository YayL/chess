import copy

import pygame
import math


def movePiece(tiles, selected, col, row):
    toAppend = [tiles.list[i].copy() for i in range(8)]
    tiles.previousBoards.append(toAppend)
    tiles.moves.append(tiles.pieces.notation(tiles.list[tiles.selectedTile[0]][tiles.selectedTile[1]], col, row, type(tiles.list[col][row]) is not str))
    tiles.pieces.movePiece(selected, tiles, col, row)

    tiles.colorToMove = tiles.colorToMove*-1 + 1
    if tiles.flipOnEveryMove: tiles.flipped = bool(-1 * tiles.flipped + 1)


def mousePressed(tiles):
    pos = pygame.mouse.get_pos()
    col, row = tiles.getTile(pos[0], pos[1])
    if tiles.list[col][row] != '' and tiles.list[col][row].color == tiles.colorToMove:
        tiles.selectedTile = [col, row]
        tiles.validMoves = [[False for j in range(8)] for i in range(8)]
        if tiles.list[col][row] != '': tiles.updateValidMoves(tiles.list[col][row], col, row)


def mouseReleased(tiles):
    pos = pygame.mouse.get_pos()  # Pos of mouse
    col, row = tiles.getTile(pos[0], pos[1])  # Coords of selected tile
    selected = tiles.list[tiles.selectedTile[0]][tiles.selectedTile[1]]  # Selected tile

    if type(selected) is not str and (col,row) != (tiles.selectedTile[0], tiles.selectedTile[1]) and selected.color == tiles.colorToMove:
        # Check if selected tile is clear AND check if dropped on the same tile
        tiles.validMoves = [[False for j in range(8)] for i in range(8)]  # Reset validmoves
        if type(tiles.list[col][row]) is not str and selected.color == tiles.list[col][row].color: return
        if not selected.isLegalMove(col, row, True): return  # Check if legal move
        if hasattr(selected, 'hasMoved'): selected.hasMoved = True  # Check if piece has the hasMoved property

        movePiece(tiles, selected, col, row)

def eventCheck(tiles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If trying to exit game
            pygame.quit()
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed(tiles)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseReleased(tiles)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                print(tiles.moves)
                print(f'Moves: {math.floor(len(tiles.moves)/2)}')
            elif event.key == pygame.K_f:
                tiles.flipOnEveryMove = bool(-1*(tiles.flipped-1))
                tiles.flipped = tiles.colorToMove
            elif event.key == pygame.K_s:
                table = [[tiles.pieces.pieceToName(x) for i,x in enumerate(tiles.list[j])] for j in range(8)]
                for x in table:
                    print(x)
            elif event.key == pygame.K_LEFT:
                tiles.list = tiles.previousBoards.pop()
                tiles.colorToMove = tiles.colorToMove * -1 + 1
                updatePieces(tiles)

    return True


def updatePieces(tiles):
    for i, y in enumerate(tiles.list):
        for j, x in enumerate(y):
            if x != '':
                x.col, x.row = j, i
