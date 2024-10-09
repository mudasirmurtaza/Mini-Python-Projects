# Rock Paper Scissors Game

This is a simple **Rock Paper Scissors** game implemented in Python. The player competes against the computer, which makes its choice randomly.

## How It Works

- The player is prompted to enter their move (either Rock, Paper, or Scissor).
- The computer randomly selects its move from the same options.
- The result of the match is determined based on the rules of Rock, Paper, Scissors:
  - **Rock** beats Scissors
  - **Paper** beats Rock
  - **Scissors** beats Paper
  - If both the player and the computer choose the same option, the match ends in a tie.

## Game Logic

- The player inputs their choice.
- The computer's choice is generated randomly using the `random.choice()` function.
- The winner is determined using a series of `if` and `elif` statements based on the combinations of user and computer choices.

## How to Run

1. Clone this repository or download the Python file.
2. Open a terminal or command prompt and navigate to the folder where the script is located.
3. Run the following command:
   ```bash
   python rps.py
   ```
4. Follow the on-screen prompts and enter either "Rock", "Paper", or "Scissor" as your move.

## Example Output

```
Enter your move: Rock
User choice = Rock, Computer Choice = Paper
Computer Won !!!
```

## Requirements

- Python 3.x
- No external libraries are required for this project.
