# -*- coding: utf-8 -*-
# coding: utf-8

# Board file

from constants import *
from random import sample


class Maze:
    def __init__(self, x_tile, y_tile, tile_size):
        self.x_tile = x_tile
        self.y_tile = y_tile
        self.tile_size = tile_size
        self.walls = []
        self.corridors = []

    # Calculating the width and the height of a tile
    @property
    def width(self):
        return self.x_tile * self.tile_size

    @property
    def height(self):
        return self.y_tile * self.tile_size

    # Reading the .txt file
    def read_map(self, map_path):
        with open("laby.txt", "r") as map_path:
            for y_axe, line in enumerate(map_path):
                for x_axe, char in enumerate(line.strip('\n')):
                    coor = ((x_axe, y_axe))
                    if char == 'w':
                        self.walls.append(coord)
                    elif char == 's':
                        self.start.append(coord)
                    elif char == 'g':
                        self.guard.append(coord)
                    elif char == 'e':
                        self.exit.append(coord)
                    else:
                        self.corridors.append(coord)

    def Set_objects(self):
        objects = {}
        objects_list = sample(self.corridors, 3)
        for index, object in enumerate(objects_list):
            objects[object] = index
            setattr(self, 'objects', objects)
