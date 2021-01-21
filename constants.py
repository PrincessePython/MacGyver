# -*- coding: utf-8 -*-
# coding: utf-8

# According to the Python convention, all the variables in constants must be in capital letters

import pygame

# Window size
WINDOW = 600

# Number of cases
NB_CASES = 15

""" Constants configuration for the game"""

# The maze in txt file
MAZE = "laby.txt"

# Start position coordinates
START = []

# Stock of maze coordinates
ZONE = []

# Stock of object positions coordinates
OBJECT_LIST = []

# Stock of wall positions coordinates
WALLS_LIST = []

# Stock corridor positions coordinates
CORRIDORS_LIST = []

# Guard position coordinates
GUARD = []

# Exit position coordinates
EXIT = []

# Sprits size
SPRITE_SIZE = int(WINDOW / NB_CASES)
# SPRITE_WIDTH = 40
# SPRITE_HEIGHT = 40


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
