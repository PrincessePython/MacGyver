import sys
import pygame
from class_maze import Maze
from class_game_settings import Game_settings
from class_MacGyver import MacGyver


def run_game():
    pygame.init()

    # Giving a title of the game
    pygame.display.set_caption("MacGyver Game")

    # Changing an icon next to the caption
    icon = pygame.image.load("Images/MacGyver.png")
    pygame.display.set_icon(icon)

    # Setting a game board
    board = Maze(15, 15, 32)
    board.read_map("Images/laby.txt")
    board.Set_objects()
    player = MacGyver(board.start)
    ui = Maze(board.width, board.height, 32)


    while True:
        # Creating a for loop for all the actions in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

                # Checking if any key is pressed
            if event.type == pygame.KEYDOWN:
                if player.status == "alive":
                    if event.key == pygame.K_LEFT:
                        player.move(-32, 0, board)
                    elif event.key == pygame.K_RIGHT:
                        player.move(+32, 0, board)
                    elif event.key == pygame.K_UP:
                        player.move(0, -32, board)
                    elif event.key == pygame.K_DOWN:
                        player.move(0, +32, board)


    Game_settings.update()


def exit_game():
    sys.exit()


if __name__ == "__main__":
    run_game()

"""
class Game:
    def __init__(self):
        pygame.init()

    # Giving a title of the game
        pygame.display.set_caption("MacGyver Game")

    # Changing an icon next to the caption
        icon = pygame.image.load("Images/MacGyver.png")
        pygame.display.set_icon(icon)

    def main(self):
    # Setting a screen
        window = Maze(15, 15, 32)
        window.read_map("Images/laby.txt")
        window.Set_objects()
        mac = MacGyver(Maze.start)
        ui = Game_settings(maze.width, maze.height)


        while True:
            # Creating a for loop for all the actions in the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False

                    # Checking if any key is pressed
                if event.type == pygame.KEYDOWN:
                    if mac.status == "alive":
                        if event.key == pygame.K_LEFT:
                            mac.move(-32, 0, window)
                        elif event.key == pygame.K_RIGHT:
                            mac.move(+32, 0, window)
                        elif event.key == pygame.K_UP:
                            mac.move(0, -32, window)
                        elif event.key == pygame.K_DOWN:
                            mac.move(0, +32, window)

    Game_settings.draw(mac, window)
    pygame.display.update()
pygame.quit()
sys.exit

"""
