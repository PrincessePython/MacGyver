
Openclassrooms project 3 : Help MacGyver to escape !

Coded in Python 3.8.6, using a PyGame 2.0.0 framework

Requirements:
fonttools==4.19.1 # To read the fonts
pygame==2.0.0	# Framework 
random2==1.0.1	# possibility to place objects randomly in maze
virtualenv==20.2.1	# Virtual environment 



This is a simple 2D maze game where MacGyver has to escape by passing through the guard who has to be killed first. In order to kill the guard, MacGyver has to collect 3 objects (needle, either, syringe)  that were placed randomly in the maze. Once all 3 objects are collected, MacGyver can create a deadly injection, and go towards the guard in order to pass through the exit door. However, if MacGyver has not able to collect 3 objects, MacGyver wont' be able to create a deadly injection and therefore, won't be able to pass through the guard. 

Game features:

Game has only 1 level. Once the game is over, player can press ESC to close the window in order to exit the game.
The game is over once MacGyver reached the exit (passing through the guard and having 3 objects collected), or, once MacGyver is in front of the guard without having collected 3 objects (MacGyver is killed by guard).

The size of the maze if 15 times 15 tiles. In my configuration, the size of each tile is 32 pixels. Those parameters could be modified by replacing my images with yours.

MacGyver is controlled with arrow keys on the keyboard. Player can move MacGyver up/down and left/right 1 case (tile) at once.

Maze is in laby.txt file. Walls, hallways, starting position, guard and exit, could be modified as long as the size of maze is respected: 15 x 15 tiles.
"w" = walls
" " = hallways
"s" = starting point
"g" = guard
"e" = exit

Objects are placed in the maze randomly and player can collect them by putting MacGyver over the objects. 


MacGyver is the only element that can be animated in the game. 




