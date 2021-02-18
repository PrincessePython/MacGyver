## Openclassrooms project 3 : Help MacGyver to escape !

Coded in Python 3.8.6, using a PyGame 2.0.0 framework

### Installation
1. Go to Git terminal and position yourself in the directory where you want to have this project cloned.

2.  Clone this project by using the following command on Git terminal:  `git clone https://github.com/PrincessePython/MacGyver.git`

3. Install virtual environment by typing the following command (Windows) : pip install virtualenv`


4. Activate the virtual environment.
	- Windows: `env/Scripts/activate.bat`
	- Other: Please feel free to contribute as I don't use other OS
	
5. Install the project requirements by typing in terminal: `pip install -r requirements.txt`


5. Run the program by typing `python game.py` in terminal.

6. Have fun !


### Game

This is a simple 2D maze game where MacGyver has to escape by passing through the guard who has to be killed first.
In order to kill the guard, MacGyver has to collect 3 objects (needle, either, syringe)  that were placed randomly in the maze. Once all 3 objects are collected, MacGyver can create a deadly injection, and go towards the guard in order to pass through the exit door. However, if MacGyver has not able to collect 3 objects, MacGyver wont' be able to create a deadly injection and therefore, won't be able to pass through the guard.

### Game features

Game has only 1 level. Once the game is over, player can press ESC to close the window in order to exit the game.

The game is over once MacGyver reached the exit (passing through the guard and having 3 objects collected), or, once MacGyver is in front of the guard without having collected 3 objects (MacGyver is killed by guard).

The size of the maze if 15 times 15 tiles. In my configuration, the size of each tile is 32 pixels. Those parameters could be modified by replacing my images with yours.

MacGyver is controlled with arrow keys on the keyboard. Player can move MacGyver up/down and left/right 1 case (tile) at once.

Maze is in `laby.txt` file Walls, hallways, starting position, guard and exit, could be modified as long as the size of maze is respected: 15 x 15 tiles.

- "w" = walls
- " " = hallways
- "s" = starting point
- "g" = guard
- "e" = exit

Objects are placed in the maze randomly and player can collect them by putting MacGyver over the objects.

MacGyver is the only element that can be animated in the game.

### Images
Some of the images where taken from https://www.flaticon.com website. 

### Files
- **game** : This is the main file that allows you to start the game
- **macgyver** : Creation of MacGyver and managing his moves
- **maze** : Board object that regroups the coordinates of game's elements; reads the map path from .txt file; places objects randomly in the game
- **settings** : Contains all the visual recourses used in the game (images, text); draws the game interface.



