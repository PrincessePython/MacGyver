# -*- coding : utf-8 -*-
# coding: utf-8
import sys
import pygame
from Settings import Settings
from Macgyver import Macgyver
from Maze import Maze

pygame.init()
pygame.display.set_caption("Mac Gyver Adventure")

window = Maze(15, 15, 32)
window.read_map()
window.place_objects()
player = Macgyver(window.start)
settings = Settings(window.width, window.height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-32, 0, window)  # Move 32px on the left, therefore it's -32 px
            elif event.key == pygame.K_RIGHT:
                player.move(+32, 0, window)  # Move 32px on the right, therefore it's +32 px
            elif event.key == pygame.K_UP:
                player.move(0, -32, window)  # Move 32px up, therefore -32px
            elif event.key == pygame.K_DOWN:
                player.move(0, +32, window)  # Move 32pn down, therefore +32px
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    settings.draw(Maze)
    pygame.display.update()
