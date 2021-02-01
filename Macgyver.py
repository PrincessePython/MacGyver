# -*- coding: utf-8 -*-
# coding: utf-8


class Macgyver:
    # Player class MacGyver
    inventory = 0

    def __init__(self, start):
        self.coord = start  # Starting position of the player MG
        self.inventory = 0
        self.status = 'alive'
        self.killed = False

    def move (self, axe_x, axe_y, window):
        x, y = self.coord
        next_step = (x + axe_x, y + axe_y)
        if next_step in window.corridors:
            self.coord = next_step
            if next_step in window.items:
                del window.items[next_step]
                self.inventory += 1
            elif next_step == window.guard:
                if self.inventory < 3:
                    self.status = 'dead'
                    self.drug = True  # MG is dead as he has not 3 items collected
                else:
                    self.coord = next_step
            elif next_step == window.end:
                self.coord = next_step
                self.drug = False

