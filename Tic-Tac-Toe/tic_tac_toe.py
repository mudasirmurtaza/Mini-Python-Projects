import tkinter as tk
from tkinter import messagebox

def check_winner():
    # list to check who won
    global winner
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green") #Highlight the wining combination
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True  # Mark the game as finished
            return

def button_click(index):
    # this function will handle button click actions
    if buttons[index]["text"] == "" and not winner:  # only allow move if button is empty and no winner yet
        buttons[index]["text"] = current_player
        buttons[index].config(fg="blue" if current_player == "X" else "red")  # Set color for X and O
        check_winner()
        if not winner:  # Only toggle player if no one has won yet
            toggle_player()

def toggle_player():
    global current_player  # used global so that it allows us to modify this variable inside a function
    current_player = "X" if current_player == "0" else "0"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg="light blue")

# List comprehension: a Python trick to make a list in one line
# Lambda is an anonymous function written in a single line, here it will call the button_click function and gives it the index of the button
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,  bg="white", fg="black", command=lambda i=i: button_click(i)) for i in range(9)]

# Grid method to set buttons in row and column
# enumerate function which will give us index of each button
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"  # Set starting player
winner = False  # Initialize winner as False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16),  bg="light blue", fg="dark blue")
label.grid(row=3, column=0, columnspan=3)  # Place label below the game grid

root.mainloop()
