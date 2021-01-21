
from constants import *


class Maze:
    def __init__(self):
        self.WALLS_LIST = []
        self.CORRIDORS_LIST = []
        self.START = []
        self.GUARD = []
        self.EXIT = []

        with open("laby.txt", "r") as laby:
            for y_axe, line in enumerate(laby):
                str = ""
                for x_axe, char in enumerate(line.strip('\n')):
                    coor = ((x_axe, y_axe))
                    if char == 'w':
                        # self.walls.append(coor) (as a possibility?)
                        self.WALLS_LIST.append(coor)
                    elif char == "p":
                        self.CORRIDORS_LIST.append(coor)
                    elif char == 's':
                        self.START.append(coor)
                    elif char == 'g':
                        self.GUARD.append(coor)
                    elif char == 'e':
                        self.EXIT.append(coor)

                    str = str + char
                print(str)

    def show(self):
        print(self.WALLS_LIST)


laby = Maze()
# laby.show()
