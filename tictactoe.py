import pygame
from pygame.locals import *

XO   = "X"

grid = [ [ None, None, None ], 
         [ None, None, None ], 
         [ None, None, None ] ]

winner = None

def initBoard(ttt):

    # ttt : a properly initialized pyGame display variable

    # set up the background surface
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill ((250, 250, 250))

    # draw the grid lines
    # vertical lines...
    pygame.draw.line (background, (0,0,0), (100, 0), (100, 300), 2)
    pygame.draw.line (background, (0,0,0), (200, 0), (200, 300), 2)

    # horizontal lines...
    pygame.draw.line (background, (0,0,0), (0, 100), (300, 100), 2)
    pygame.draw.line (background, (0,0,0), (0, 200), (300, 200), 2)

    # return the board
    return background

def clickBoard(board):
    global grid, XO

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos(mouseX, mouseY)


    if ((grid[row][col] == "X") or (grid[row][col] == "O")):
        return

    drawMove (board, row, col, XO)

    
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"


pygame.init()
ttt = pygame.display.set_mode ((300, 325))
pygame.display.set_caption ('Tic-Tac-Toe by Ardy')

board = initBoard(ttt)

running = True


while running:
    for event in pygame.event.get():
        if event.type is QUIT:
            running = False
        elif event.type is MOUSEBUTTONDOWN:
            clickBoard(board)