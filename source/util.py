import pygame
from config import config

BackGroundImg = pygame.image.load('./source/img/board.png')
BlackImg = pygame.image.load('./source/img/black.gif')
WhiteImg = pygame.image.load('./source/img/white.gif')

BackGround = pygame.transform.scale(BackGroundImg, config.SIZE)
Black = pygame.transform.scale(BlackImg, config.PieceScale)
White = pygame.transform.scale(WhiteImg, config.PieceScale)


def music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
