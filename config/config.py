import configparser

parser = configparser.ConfigParser()
parser.read('./config/config.ini', 'utf-8')

__WIDTH = parser.getint('board', 'width')
__HEIGHT = parser.getint('board', 'height')
__BoardRow = parser.getint('board', 'row')
__BoardCol = parser.getint('board', 'col')
__Scale = parser.getint('pieces', 'scale')

FPS = parser.getint('game', 'fps')
SIZE = (__WIDTH, __HEIGHT)
PieceScale = (__Scale, __Scale)
BoardSize = (__BoardRow, __BoardCol)
Offset = parser.getint('pieces', 'offset')
