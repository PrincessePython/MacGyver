# -*- coding: utf-8 -*-
# coding: utf-8

# According to the Python convention, all the variables in constants must be in capital letters

import pygame

# Window Size
WIDTH = 480
HEIGHT = 480
WINDOW_SIZE = WIDTH, HEIGHT
CENTER = (WIDTH //2 ), (HEIGHT // 2)
# Screen size in cases (15 x 15)
X = 15
Y = 15

""" Constants configuration for the game"""

# The maze in txt file
MAZE = "laby.txt"

# Start position coordinates
START = []

# Stock of maze coordinates
ZONE = []

# Stock of object positions coordinates
OBJECTS_LIST = []

# Stock of wall positions coordinates
WALLS_LIST = []

# Stock corridor positions coordinates
CORRIDORS_LIST = []

# Guard position coordinates
GUARD = []

# Exit position coordinates
EXIT = []


# Sprite size configuration
SPRITE = 1
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32
SPRITE_SIZE_WIDTH = int(WIDTH / SPRITE_WIDTH)
SPRITE_SIZE_HEIGHT = int(HEIGHT / SPRITE_HEIGHT)


""""***************************************************************

Resizing images to the new resolution with pygame.transform.scale()

****************************************************************"""

macGyver = pygame.transform.scale(pygame.image.load("MacGyver.png"), (SPRITE_SIZE, SPRITE_SIZE))
guard = pygame.transform.scale(pygame.image.load("Gardien.png"), (SPRITE_SIZE, SPRITE_SIZE))

wall = pygame.transform.scale(pygame.image.load("brick-wall.png"), (SPRITE_SIZE, SPRITE_SIZE))
floor = pygame.transform.scale(pygame.image.load("floor.png"), (SPRITE_SIZE, SPRITE_SIZE))

needle = pygame.transform.scale(pygame.image.load("needle.png"), (SPRITE_SIZE, SPRITE_SIZE))
syringe = pygame.transform.scale(pygame.image.load("seringue.png"), (SPRITE_SIZE, SPRITE_SIZE))
ether = pygame.transform.scale(pygame.image.load("ether.png"), (SPRITE_SIZE, SPRITE_SIZE))

win = pygame.transform.scale(pygame.image.load("winner.png"), (SPRITE_SIZE, SPRITE_SIZE))
loose = pygame.transform.scale(pygame.image.load("looser.png"), (SPRITE_SIZE, SPRITE_SIZE))
