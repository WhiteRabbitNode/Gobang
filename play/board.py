import numpy as np
from config import config

board = np.zeros(config.BoardSize)


def __std(a) -> int:
    return 0 if a < 0 else 14 if a > 14 else a


def isFull():
    for arr in board:
        for item in arr:
            if item == 0:
                return True
    return False


def isAvailable(loc):
    return board[loc[1]][loc[0]] == 0


def clear():
    board.fill(0)


def assign(loc, player):
    board[loc[1]][loc[0]] = player


def isGameOver():
    for x in range(0,15):
        for y in range(0,15):
            if board[x][y]!=0:
                if x+4<15 and board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] == board[x+4][y]:
                    return True
                if x-4>=0 and board[x][y] == board[x-1][y] == board[x-2][y] == board[x-3][y] == board[x-4][y]:
                    return True
                if y+4<15 and board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] == board[x][y+4]:
                    return True
                if y-4>=0 and board[x][y] == board[x][y-1] == board[x][y-2] == board[x][y-3] == board[x][y-4]:
                    return True
                if x+4<15 and y+4<15 and board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == board[x+4][y+4]:
                    return True
                if x+4<15 and y-4>=0 and board[x][y] == board[x+1][y-1] == board[x+2][y-2] == board[x+3][y-3] == board[x+4][y-4]:
                    return True
                if x-4>=0 and y+4<15 and board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] == board[x-4][y+4]:
                    return True
                if x-4>=0 and y-4>=0 and board[x][y] == board[x-1][y-1] == board[x-2][y-2] == board[x-3][y-3] == board[x-4][y-4]:
                    return True
    return False
