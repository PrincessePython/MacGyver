# -*- coding : utf-8 -*-
# coding: utf-8

import pygame


class Settings:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

        self.wall_image = pygame.image.load('Images/brick-wall.png')
        self.floor_image = pygame.image.load('Images/floor.png')
        self.stairs_image = pygame.image.load('Images/door.png')
        self.stairs_image = pygame.image.load('Images/exit_door.png')
        self.guard_image = pygame.image.load('Images/guard.png')
        self.components_image = [pygame.image.load('Images/needle.png'),
                                 pygame.image.load('Images/syringe.png'),
                                 pygame.image.load('Images/ether.png')]
        self.mac_image = pygame.image.load('Images/mac.png')
        self.grave_image = pygame.image.load('Images/dead.png')
        self.winner_image = pygame.image.load('Images/winner.png')

    def draw(self, mac, maze):
        for coord in maze.walls:
            self.screen.blit(self.wall_image, coord)
        for coord in maze.corridors:
            self.screen.blit(self.floor_image, coord)
        self.screen.blit(self.floor_image, maze.start)
        self.screen.blit(self.stairs_image, maze.start)
        self.screen.blit(self.floor_image, maze.end)
        self.screen.blit(self.stairs_image, maze.end)
        for key, value in maze.objects.items():
            self.screen.blit(self.components_image[value], key)
        self.screen.blit(self.floor_image, maze.guard)
        if mac.drug:
            self.screen.blit(self.grave_image, maze.guard)
        else:
            self.screen.blit(self.guard_image, maze.guard)
        if mac.status != 'alive':
            if mac.status == 'dead':
                self.screen.blit(self.grave_image, mac.coord)
                self.display_txt('YOU LOSE !', 64, (29, 0, 255), self.screen,
                                 'center', 120)
            elif mac.status == 'escaped':
                self.screen.blit(self.mac_image, mac.coord)
                self.display_txt('YOU WIN !', 64, (29, 0, 255), self.screen,
                                 'center', 120)
            self.display_txt('Press ESCAPE to Quit', 24, (29, 0, 255),
                             self.screen, 'center', 240)
        else:
            self.screen.blit(self.mac_image, mac.coord)

    def display_txt(self, txt, size, color, surface, x='center', y='center'):
        """display the text in a middle of a surface with pygame
           """
        txt = str(txt)
        font = pygame.font.Font('images/baxoe.ttf', size)
        img_txt = font.render(txt, True, color)
        if x == 'center':
            x = int((surface.get_width() - font.size(txt)[0]) / 2)
        if y == 'center':
            y = int((surface.get_height() - font.size(txt)[1]) / 2)
        return surface.blit(img_txt, (x, y))
