# -*- coding: utf-8 -*-
# coding: utf-8
class MacGyver:

    def __init__(self, start):
        self.coord = start
        self.counter = 0
        self.status = "alive"
        self.drug = False

    def move(self, axe_x, axe_y, maze):
        # Move the main character
        x, y = self.coord
        next_step = (x + axe_x, y + axe_y)
        if next_step in maze.corridors:
            self.coord = next_step
            if next_step in maze.objects:
                del maze.objects[next_step]
                self.counter += 1
            elif next_step == maze.guard:
                if self.counter < 3:
                    self.status = "dead"
                else:
                    self.coord = next_step
                    self.drug = True
            elif next_step == maze.exit:
                self.coord = next_step
                self.status = "escaped"
