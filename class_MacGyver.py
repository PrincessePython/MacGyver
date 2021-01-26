# -*- coding: utf-8 -*-
# coding: utf-8
import pygame


class Macgyver:
    # Player class that will keep all the information of the MacGyver
    def __init__(self):
        self.position = start
        self.move_x = 0
        self.move_y = 0
        self.mac_image = pygame.image.load('Images/mac.png')
        self.inventory = 0
        self.status = 'alive'
        self.killed = False

    def control(self, x, y):
        # Control player movement
        self.move_x += x
        self.move_y += y

    def check_position(self):

        # Chacking the players position in the game

        if position == 'object':
            inventory += 1
        elif possition == 'guard':
            if inventory < 3:
                self.killed = True
            # display message : YOU LOOSE !
            else:
            # dispaly message: YOU WIN !
