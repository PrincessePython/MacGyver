# -*- coding : utf-8 -*-
# coding: utf-8

import pygame

from Maze import Maze

class Settings:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

        self.wall_image = pygame.image.load('Images/brick-wall.png')
        self.floor_image = pygame.image.load('Images/floor.png')
        self.stairs_image = pygame.image.load('Images/door.png')
        self.stairs_image = pygame.image.load('Images/exit_door.png')
        self.guard_image = pygame.image.load('Images/guard.png')
        self.objects_image = [pygame.image.load('Images/needle.png'),
                              pygame.image.load('Images/syringe.png'),
                              pygame.image.load('Images/ether.png')]

    def draw(self, Maze):  # Draw images on the game window
        for coord in Maze.walls:
            self.screen.blit(self.wall_image, coord)
        for coord in Maze.corridors:
            self.screen.blit(self.floor_image, coord)
        self.screen.blit(self.floor_image, Maze.start)
        self.screen.blit(self.stairs_image, Maze.start)
        self.screen.blit(self.floor_image, Maze.end)
        self.screen.blit(self.stairs_image, Maze.end)
        for key, value in Maze.objects.items():
            self.screen.blit(self.objects_image[value], key)
        self.screen.blit(self.floor_image, Maze.guard)
