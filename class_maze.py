# -*- coding: utf-8 -*-
# coding: utf-8

from random import sample


class Maze:
    # Regrouping coordinates of game elements like walls, start, end, guard ans objects
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
                    coord = ((x_axe, y_axe))
                    if char == 'w':
                        self.walls.append(coord)
                    elif char == 's':
                        setattr(self, "start", coord)
                    elif char == 'g':
                        setattr(self, "guard", coord)
                    elif char == 'e':
                        setattr(self, "end", coord)
                    else:
                        self.corridors.append(coord)

    # Randomly selecting coordinates of the available tiles and putting them in dictionary
    def Set_objects(self):
        objects = {}
        objects_list = sample(self.corridors, 3)
        for index, object in enumerate(objects_list):
            objects[object] = index
            setattr(self, 'objects', objects)
