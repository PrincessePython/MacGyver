from constants import *
from random import sample


class Game_settings:
    def __init__(self, x_tile, y_tile, tile_size):
        self.x_tile = x_tile
        self.y_tile = y_tile
        self.tile_size = tile_size
        self.walls = []
        self.corridors = []

    @property
    def width(self):
        return self.x_tile * self.tile_size

    @property
    def height(self):
        return self.y_tile * self.tile_size

    def read_map(self, map_path):
        with open("laby.txt", "r") as map_path:
            for y_axe, line in enumerate(map_path):
                for x_axe, char in enumerate(line.strip('\n')):
                    coor = ((x_axe, y_axe))
                    if char == 'w':
                        self.WALLS_LIST.append(coord)
                    elif char == 's':
                        self.START.append(coord)
                    elif char == 'g':
                        self.GUARD.append(coord)
                    elif char == 'e':
                        self.EXIT.append(coord)
                    else:
                        self.corridors.append(coord)

    def Set_objects(self):
        objects = {}
        OBJECTS_LIST = sample(self.corridors, 3)
        for index, object in enumerate(OBJECTS_LIST):
            objects[object] = index
            setattr(self, 'objects', objects)
