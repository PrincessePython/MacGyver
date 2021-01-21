# -*- coding: utf-8 -*-
# coding: utf-8
# UI file
import pygame
from maze import *


class Game_settings:

    def __init__(self, width, height):
        self.screen = pygame.dosplay.set_mode((width, height))
        self.wall = pygame.image.load("Images/brick-wall.png")
        self.floor = pygame.image.load("Images/floor.png")
        self.start = pygame.image.load("Images/start.png")
        self.guard = pygame.image.load("Images/Gardien.png")
        self.objects = [pygame.image.load("Images/needle.png"),
                        pygame.image.load("Images/seringue.png"),
                        pygame.image.load("Images/ether.png")
                        ]
        self.MacGyver = pygame.image.load("Images/MacGyver.png")
        self.winner = pygame.image.load("Images/winner.png")
        self.looser = pygame.image.load("Images/looser.png")
        self.exit = pygame.image.load("Images/exit_door.png")

    def draw(self, MacGyver, maze):
        for coord in maze.walls:
            self.screen.blit(self.wall, coord)
        for coord in maze.corridors:
            self.screen.blit(self.floor, coord)
        self.screen.blit(self.floor, maze.start)
        self.screen.blit(self.start, maze.start)
        self.screen.blit(self.floor, maze.end)
        self.screen.blit(self.start, maze.end)

        for key, value in maze.objects.items():
            self.screen.blit(self.objects[value], key)
        self.screen.blit(self.floor, maze.guard)

        if MacGyver.drug:
            self.screen.blit(self.looser, maze.guard)
        else:
            self.screen.blit(self.guard, maze.guard)

        if MacGyver.status != "alilve":
            if MacGyver.status == "dead":
                self.screen.blit(self.looser, MacGyver.coord)
                self.display_text('YOU LOSE', 64, (180,60, 20), self.screen, 'center', 120)

            elif MacGyver.status == "escaped":
                self.screen.blit(self.MacGyver, MacGyver.coord)
                self.display_text('YOU WIN', 64, (20, 60, 180), self.screen, 'center', 120)

            self.display_texte('Press ESCAPE to QUIT'), 24, (25,25,25))

        else:
            self.screen.blit(self.MacGyver, MacGyver.coord)
            


"""
    # Setting a player image and his starting position
    playerImg = pygame.image.load("MacGyver.png")
    player_positionX = 50
    player_positionY = 0
    playerX_change = 0
    playerY_change = 0




    def player(x, y):
        screen.blit(playerImg, (x, y))

    def key_check(self):
        # Checking if any key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = 0.1
            if event.key == pygame.K_DOWN:
                playerY_change = -0.1

        # Checking if the key was released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0



# Kill the guard


# while all objects are not united and the guard is not killed:
# continue game

# if object_counter == 3:
# go kill the guard
# else:
# continue to search for objects

# if object counter =! 3:
# continue to search for objects
# else:
# go towards guard - game over
# game over
"""
