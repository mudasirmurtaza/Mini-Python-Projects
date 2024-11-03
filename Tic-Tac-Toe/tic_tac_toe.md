# Tic-Tac-Toe Game

A simple and interactive **Tic-Tac-Toe** game built using Python's `tkinter` library for GUI. 

## Overview

This Tic-Tac-Toe game provides a basic 3x3 grid where two players (X and O) take turns. The game automatically checks for a winner and highlights the winning combination. It's an easy and fun way to understand GUI development in Python.

![screenshot or gif if available]

## Features

- **Interactive GUI**: Uses the `tkinter` library for a user-friendly graphical interface.
- **Turn Display**: Shows the current player's turn at the bottom of the grid.
- **Winner Announcement**: Highlights the winning combination and announces the winner.
- **Aesthetic Colors**: Customized background and button colors for a visually pleasing experience.

## How to Run

### Prerequisites

- Python 3.x
- `tkinter` (included with most Python installations)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/mudasirmurtaza/Mini-Python-Projects.git
   ```

2. Navigate to the Tic-Tac-Toe project directory:
   ```bash
   cd Mini-Python-Projects/Tic-Tac-Toe
   ```

3. Run the script:
   ```bash
   python tic_tac_toe.py
   ```

## How to Play

1. The game starts with **Player X**. Players take turns clicking on the buttons in the 3x3 grid.
2. The current player's symbol (X or O) is displayed on the button.
3. The game checks for a winning combination after each move. When a player wins, the winning buttons turn green, and a message box announces the winner.
4. To play again, simply restart the script.

## Code Highlights

- **Game Logic**: The code checks for winning combinations after each move using a list of possible winning button indices.
- **Toggle Player**: The function `toggle_player()` switches between players X and O after each turn.
- **GUI Layout**: The buttons are arranged in a 3x3 grid, and the current player's turn is displayed with a `Label` widget at the bottom of the grid.


##Contribution
Feel free to contribute by submitting pull requests or suggesting improvements!

---

