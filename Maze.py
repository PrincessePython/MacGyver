# -*- coding : utf-8 -*-
# coding: utf-8

from random import sample


class Maze:
    # Class that will contain the coordinates of objects like walls, exit, guard, etc
    # It will allow to read the map and to place 3 objects randomly in the maze

    def __init__(self, leng, ht, tile_size):
        self.leng = leng  # Length of the maze in tiles
        self.ht = ht  # Height of the maze in tiles
        self.tile_size = tile_size  # Tile dimensions modifiable
        self.walls = []
        self.start = []
        self.exit = []
        self.guard = []
        self.corridors = []
        self.objects = []

    @property
    def width(self):    # Width of the maze on the screen (15 * 32)
        return self.leng * self.tile_size

    @property
    def height(self):   # Height of the maze on the screen (15 * 32)
        return self.ht * self.tile_size

    def read_map(self):
        with open('laby.txt', 'r') as map_path:
            for y_index, line in enumerate(map_path):
                for x_index, char in enumerate(line.strip('\n')):
                    coord = ((x_index * self.tile_size), (y_index * self.tile_size))
                    if char == 'w':
                        self.walls.append(coord)
                    elif char == 's':
                        self.start.append(coord)
                    elif char == 'e':
                        self.exit.append(coord)
                    elif char == 'g':
                        self.guard.append(coord)
                    elif char == ' ':
                        self.corridors.append(coord)

    def place_objects(self):
        # Randomly place 3 objects in the maze
        items = {}
        items_list = sample(self.corridors, 3)  # Module sample is used to randomly place 3 objects in the maze
        for index, object in enumerate(items_list):
            items[object] = index
        setattr(self, 'objects', items)
