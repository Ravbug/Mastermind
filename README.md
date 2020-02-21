# Mastermind
In 2010 I wrote a version of Mastermind in Python and Pygame. I found it on an old computer and decided to publish it.

## How to play Mastermind
Mastermind is a code-breaking game. One player decides a secret code of four colors, and the other 
player has ten chances to crack the code. The board is arranged in ten rows of 8 pin-holes. The codebreaker uses the larger
holes while the codemaker uses the smaller holes. In this version, the computer plays the role of the codemaker, and you play the role of the codebreaker.

The codemaker chooses a four-color code out of any of the following colors: red, orange, yellow, green, blue, and purple. 
The codemaker may optionally use a blank space as one of the items in the code, and can re-use the same color multiple times. 
In this version of the game, a dialog box allows the player to choose if they want to allow the computer to include blank spaces
in its code.

Once the codemaker has selected the code, the codebreaker attempts to figure it out. 
The codebreaker places the large colored pegs into the large holes (see controls below). 
Once the codebreaker is satisfied with their guess, the codemaker "grades" them by filling the smaller holes with 
pegs of two colors.

- Red peg: One color is correct and is in the correct location.
- White peg: One color is correct but is not in the correct location.
- Red stripe across holes: None of the colors are correct.

The order of the pegs in the grading circles is not necessariliy the same as the pegs in your guess. 
The codebreaker wins if they can guess the correct code (signified with all red in the grading area) within 10 guesses. 

## Controls
This game has very simple keyboard controls. 
- `Left arrow`: Move the selection box left one space
- `Right arrow`: Move the selection box right one space
- `Enter`: Commit your guess
- `R`: Place a red peg in the selected space
- `O`: Place an orange peg in the selected space
- `Y`: Place a yellow peg in the selected space
- `G`: Place a green peg in the selected space
- `P`: Place a purple peg in the selected space
- `B`: Place a blue peg in the selected space
- `Space`: Remove a peg from a space (set it to blank)

## How to run the game on your computer
This game works in both Python 2 and Python 3. It relies on the following pypi libraries:
- Pygame
- Easygui

Additionaly, these libraries have external dependencies:
- SDL (for Pygame)
- Tkinter (For easygui)
Both of these dependencies can be installed on Linux/Mac using the system package manager (homebrew on Mac).

Setup instructions:
1. Clone or download the repository
2. Create a virtual environment: `python -m venv env`
3. Enter the virtual environment
   - Mac/Linux: `source env/bin/activate`
   - Windows: 
4. Install Pygame and Tkinter's dependency libraries (see above)
5. Install the pypi requirements: `pip install -r requirements.txt`
6. Run the game: `python Mastermind.py`

To uninstall the game, simply delete the virtual environment folder and the script. Then uninstsall the external dependencies.
