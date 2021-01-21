# -*- coding: utf-8 -*-

class Player:

    def __init__(self):
        self.name = "MacGyver"

    # Setting a player image and his starting position
    playerImg = pygame.image.load("MacGyver.png")
    player_positionX = 50
    player_positionY = 0
    playerX_change = 0
    playerY_change = 0

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def key_check(self):
        # Checking if any key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = 0.1
            if event.key == pygame.K_DOWN:
                playerY_change = -0.1

        # Checking if the key was released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0



# Kill the guard


# while all objects are not united and the guard is not killed:
# continue game

# if object_counter == 3:
# go kill the guard
# else:
# continue to search for objects

# if object counter =! 3:
# continue to search for objects
# else:
# go towards guard - game over
# game over
