import pygame
from show import draw
from play import action
from play import board

pygame.init()
draw.init()
player = 1
gameOver = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            action.ExitGame()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            if action.click(event, player):
                gameOver = board.isGameOver()
                if gameOver:
                    draw.gameOver()
                player = -player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                action.restart()
                gameOver = False
                player = 1
    pygame.display.update()
