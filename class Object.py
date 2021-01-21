#! /user/bin/env python3
# coding: utf-8

import pygame
import random2

from constants import *


# Creating an Object class that will be used to build objects and place them randomly
class Object():
    # Initializing the class
    def __init__(self, object):
        # Creating an object
        self.size =
        self.item_rect = item.get_rect()  # Creating this object
        self.position = (0,0)   # Initializing the position
        self.generate_position()   # Automatically generating the object
        self.x, self.y = self.position   # Separating x and y coordinates for blit

    def generate_position(self):
            # Generate the random position of the objects from CORRIDORS_LIST
            self.position = random.choice(CORRIDORS_LIST)
            return self.position

""" 

********** Version 1 *************

# Setting a counter
counter = 0

# Defining needle object
needleImg = pygame.image.load("needle.png")
needle_collect = True
if needle_collect == True:
    counter = counter + 1

# Defining ether object
etherImg = pygame.image.load("ether.png")
ether_collect = True
if ether_collect == True:
    counter = counter + 1

# Defining seringue object
seringueImg = pygame.image.load("seringue.png")
seringue_collect = True
if seringue_collect == True:
    counter = counter + 1


def needle():
    screen.blit(needleImg, (needleX, needleY))


def either():
    screen.blit(eitherImg, (eitherX, eitherY))

def seringue():
    screen.blit(seringueImg, (seringueX, seringueY))
"""





"""
*********** Version 2 *************
I am hesitating to use blocks..

# Creating an image of the block and then filling it with a color
self.image = pygame.Surface([width, height])
self.image.fill(color)
# Drowing the rect around the object
self.rect = self.image.get_rect()

needle = Object((255, 255, 0), 40, 40))

object_Group = pygame.sprite.Group()
object_Group.add(needle)
"""
