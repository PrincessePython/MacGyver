from constants import *
import pygame
from random2 import randint

# Initializing the pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((600, 600))

# Title and Icon
pygame.display.set_caption("MacGyver Game")

# Changing an icon next to the caption
icon = pygame.image.load("MacGyver.png")
pygame.display.set_icon(icon)

# Window size
window = 600  # 15 * 40

# Number of cases
nb_cases = 15

# Sprits size
resize_decor = int(window / nb_cases)

# Setting up maze
maze = open("laby.txt", "r")
wall_image = pygame.image.load("brick-wall.png")
floor_image = pygame.image.load("floor.png")
start_mage = pygame.image.load("start.png")
exit_image = pygame.image.load("exit_door.png")
guard_image = pygame.image.load("Gardien.png")
walls = []
corridors = []
start = []
end = []
guard = []


def setup_maze():
    with open("laby.txt", 'r') as data:
        for y_index, line in enumerate(data):
            for x_index, char in enumerate(line.strip('\n')):
                coord = ((x_index * 40, y_index * 40))
                if char == 'w':
                    walls.append(coord)
                elif char == 's':
                    start_coord = coord
                elif char == 'e':
                    end_coord = coord
                elif char == 'g':
                    guard_coord = coord
                else:
                    corridors.append(coord)

    for coord in walls:
        screen.blit(wall_image, coord)

    for coord in corridors:
        screen.blit(floor_image, coord)

    for coord in start:
        screen.blit(start_image, start_coord)

    for coord in end:
        screen.blit(exit_image, end_coord)

    for coor in guard:
        screen.blit(guard_image, guard_coord)


def player(x, y):
    screen.blit(playerImg, (x, y))


# Setting a player image and his starting position
playerImg = pygame.image.load("MacGyver.png")
playerX = 50
playerY = 0
playerX_change = 0
playerY_change = 0

# Setting a condition for a game loop
playing = True
# Game loop
while playing:
    # RGB choise of the background color (black)
    screen.fill((0, 0, 0))

    # Creating a for loop for all the actions in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

            # Checking if any key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            elif event.key == pygame.K_UP:
                playerY_change = 0.1
            elif event.key == pygame.K_DOWN:
                playerY_change = -0.1

            # Checking if the key was released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

        playerX += playerX_change
        playerY -= playerY_change

    # Installing the boundaries for the player and the exit point that is on the bottom right corner
    if playerX <= 0:
        playerX = 0
    elif playerX >= 568:
        playerX = 568
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 557:
        playerY = 557
    elif playerX == 568 and playerY == 557:
        playerY = 600

    # Call the player function defined earlier
    player(playerX, playerY)

    # Call the wall function defined earlier
    # wall(0, 0)
    # Regular update of a Game window
    pygame.display.update()
setup_maze()
pygame.quit()
