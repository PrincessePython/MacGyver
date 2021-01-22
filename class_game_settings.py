# -*- coding: utf-8 -*-
# coding: utf-8

import pygame


class Game_settings:

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.wall_img = pygame.image.load("Images/brick-wall.png")
        self.floor = pygame.image.load("Images/floor.png")
        self.start = pygame.image.load("Images/door.png")
        self.guard = pygame.image.load("Images/guard.png")
        self.objects = [pygame.image.load("Images/needle.png"),
                        pygame.image.load("Images/syringe.png"),
                        pygame.image.load("Images/ether.png")
                        ]
        self.MacGyver = pygame.image.load("Images/mac.png")
        self.exit = pygame.image.load("Images/exit_door.png")

    def draw(self, MacGyver, maze):
        for coord in maze.walls:
            self.screen.blit(self.wall_img, coord)
        for coord in maze.corridors:
            self.screen.blit(self.floor, coord)
        self.screen.blit(self.floor, maze.start)
        self.screen.blit(self.start, maze.start)
        self.screen.blit(self.floor, maze.end)
        self.screen.blit(self.start, maze.end)

        for key, value in maze.objects.items():
            self.screen.blit(self.objects[value], key)
        self.screen.blit(self.floor, maze.guard)




