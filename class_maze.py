# -*- coding : utf-8 -*-
# coding: utf-8

from random import sample


class Maze:
    # Class that will contain the coordinates of objects like walls, exit, guard, etc
    def __init__(self):
        self.tile_size = 32
        self.walls = []
        self.start = []
        self.exit = []
        self.guard = []
        self.corridors = []
        self.objects = []



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

    def placing_objects(self):
        # Randomly place 3 objects in the maze
        objects = {}
        object_list = sample(self.corridors, 3)
        for index, object in enumerate(object_list):
            objects[object] = index

