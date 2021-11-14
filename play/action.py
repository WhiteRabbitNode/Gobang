import sys
from show import draw
from play import board
from source.util import music


def ExitGame():
    sys.exit()


def click(event, player):
    clicked = [event.pos[0] // 40, event.pos[1] // 40]
    if board.isAvailable(clicked):
        board.assign(clicked, player)
        music('./source/audio/click.wav')
        if player == 1:
            draw.drawBlack(clicked)
        elif player == -1:
            draw.drawWhite(clicked)
        return True
    else:
        return False


def restart():
    draw.init()
    board.clear()
    music('./source/audio/start.wav')
