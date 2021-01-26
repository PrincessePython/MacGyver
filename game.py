# -*- coding : utf-8 -*-
# coding: utf-8

import pygame
from class_Settings import Settings
from class_Maze import Maze
from class_Macgyver import Macgyver

pygame.init()

screen = pygame.display.set_mode([480, 480])  # 15 steps by 32px


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x -= 1
            # move left
            # check position
            elif event.key == pygame.K_RIGHT:
                move_x += 1
            # move right
            # check position
            elif event.key == pygame.K_UP:
                move_y -= 1
            # move up
            # check position
            elif event.key == pygame.K_DOWN:
                move_y += 1
            # move down
            # check position

    screen.fill((255, 255, 255))    # Fill the screen with white color

    # Draw maze on the window

    pygame.display.flip()

