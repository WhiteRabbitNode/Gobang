import pygame
from config import config
from source import util
from source.util import music

pygame.init()
screen = pygame.display.set_mode(config.SIZE)
my_font = pygame.font.Font(None, 60)
text_surface1 = my_font.render("Game Over", True, (0, 0, 0), (255, 255, 255))
text_surface2 = my_font.render("Enter R to Restart!", True, (0, 0, 0), (255, 255, 255))


def init():
    music('./source/audio/superMarry.wav')
    screen.blit(util.BackGround, (0, 0))
    pygame.display.update()


def drawBlack(loc):
    x = loc[0] * 40 + config.Offset
    y = loc[1] * 40 + config.Offset
    screen.blit(util.Black, (x, y))
    pygame.display.update()


def drawWhite(loc):
    x = loc[0] * 40 + config.Offset
    y = loc[1] * 40 + config.Offset
    screen.blit(util.White, (x, y))
    pygame.display.update()


def gameOver():
    music('./source/audio/superMarry.wav')
    screen.blit(text_surface1, (200, 100))
    screen.blit(text_surface2, (140, 200))
    pygame.display.update()
