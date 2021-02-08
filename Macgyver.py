# -*- coding: utf-8 -*-
# coding: utf-8

class Macgyver:

    def __init__(self, start):
        self.coord = start
        self.backpack = 0
        self.status = 'alive'
        self.drug = False

    def move(self, vector_x, vector_y, maze):
        """move mac to the next square"""
        x, y = self.coord
        next_step = (x + vector_x, y + vector_y)
        if next_step in maze.corridors:
            self.coord = next_step
            if next_step in maze.objects:
                del maze.objects[next_step]
                self.backpack += 1
        elif next_step == maze.guard:
            if self.backpack < 3:
                self.status = 'dead'
            else:
                self.coord = next_step
                self.drug = True
        elif next_step == maze.end:
            self.coord = next_step
            self.status = 'escaped'