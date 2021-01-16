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

    drawMove(board, row, col, XO)

    
    if (XO == "X"):
        XO = "O"
    else:
        XO = "X"



def drawMove(board, row, col, Piece):
    centerX = ((col) * 100) + 50
    centerY = ((row) * 100) + 50


    if (Piece == "O"):
        pygame.draw.circle(board, (0,0,0), (centerX, centerY), 44, 2)
    else:
        pygame.draw.line(board, (0,0,0), (centerX - 22, centerY - 22), (centerX + 22, centerY + 22), 2)
        pygame.draw.line(board, (0,0,0), (centerX + 22, centerY - 22), (centerX - 22, centerY + 22), 2)

    grid[row][col] = Piece


def boardPos(mouseX, mouseY):
    if (mouseY < 100):
        row = 0
    elif (mouseY < 200):
        row = 1
    else:
        row = 2


    if (mouseX < 100):
        col = 0
    elif (mouseX < 200):
        col = 1
    else:
        col = 2

    return (row, col)




def showBoard(ttt, board):
    # drawStatus(board)
    ttt.blit(board, (0,0))
    pygame.display.flip()









pygame.init()
ttt = pygame.display.set_mode ((300, 325))
pygame.display.set_caption ('Tic-Tac-Toe by Ardy')

board = initBoard(ttt)

running = True


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            clickBoard(board)


        # gameWon()


        showBoard(ttt, board)