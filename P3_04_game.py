# -*- coding: utf-8 -*-
# -*- coding : utf-8 -*-

import sys
import pygame
from settings import Settings
from maze import Maze
from macgyver import Macgyver


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('MacGyver')

    def main(self):

        window = Maze(15, 15, 32)
        window.read_map('laby.txt')
        window.place_objects()
        mac = Macgyver(window.start)
        interface = Settings(window.width, window.height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if mac.status == 'alive':
                        if event.key == pygame.K_UP:
                            mac.move(0, -32, window)
                        elif event.key == pygame.K_LEFT:
                            mac.move(-32, 0, window)
                        elif event.key == pygame.K_DOWN:
                            mac.move(0, +32, window)
                        elif event.key == pygame.K_RIGHT:
                            mac.move(+32, 0, window)
                    else:
                        if event.key == pygame.K_RETURN:
                            return self.main()
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

            interface.draw(mac, window)
            pygame.display.update()


if __name__ == '__main__':
    Game().main()

