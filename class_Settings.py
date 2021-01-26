# -*- coding : utf-8 -*-
# coding: utf-8

# Former class UI
import pygame


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
        self.grave_image = pygame.image.load('Images/dead.png')
        self.zzz_image = pygame.image.load('Images/winner.png')

    def draw(self):
        for coord in maze.walls:
            self.screen.blit(self.wall_image, coord)
        for coord in maze.corridors:
            self.screen.blit(self.floor_image, coord)
        self.screen.blit(self.floor_image, board.start)
        self.screen.blit(self.stairs_image, board.start)
        self.screen.blit(self.floor_image, board.end)
        self.screen.blit(self.stairs_image, board.end)
        for key, value in maze.objects.items():
            self.screen.blit(self.objects_image[value], key)
        self.screen.blit(self.floor_image, board.guard)
