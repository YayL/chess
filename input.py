import pygame
import math


def movePiece(tiles, selected, col, row):
    taking = False
    if type(tiles.list[col][row]) is not str: taking = True
    tiles.moves.append(tiles.pieces.moveToPiece(tiles.list[tiles.selectedTile[0]][tiles.selectedTile[1]], col, row, taking))
    tiles.list[col][row] = selected  # Set selected piece to the new tile
    tiles.list[col][row].row, tiles.list[col][row].col = col, row  # Set the piece's col and row of the new tile
    tiles.list[tiles.selectedTile[0]][tiles.selectedTile[1]] = ''  # Clear old tile
    tiles.colorToMove = tiles.colorToMove*-1 + 1


def mousePressed(tiles):
    pos = pygame.mouse.get_pos()
    col, row = tiles.getTile(pos[0], pos[1])
    tiles.selectedTile = [col, row]


def mouseReleased(tiles):
    pos = pygame.mouse.get_pos()  # Pos of mouse
    col, row = tiles.getTile(pos[0], pos[1])  # Coords of selected tile
    selected = tiles.list[tiles.selectedTile[0]][tiles.selectedTile[1]]  # Selected tile
    if type(selected) is not str and (col,row) != (tiles.selectedTile[0], tiles.selectedTile[1]) and selected.color == tiles.colorToMove:
        # Check if selected tile is clear AND check if dropped on the same tile
        if type(tiles.list[col][row]) is not str and selected.color == tiles.list[col][row].color: return
        if not selected.isLegalMove(col, row): return  # Check if legal move
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

    return True
