"""
Workflow / Logic
    Input from user (Rock, Paper, Scissor)
    Computer choice using randomly not using any conditional statement
    Output Result 
    
    
Cases:
A Rock:
    Rock + Rock = Tie
    Rock + Paper = Paper wins
    Rock + Scissor = RocK wins
    
B Paper   
    Paper + Paper = Tie
    Paper + Rock = Paper wins
    Paper + Scissor = Scissor  wins
    
C Scissor
    Scissor + Scissor = Tie
    Scissor + Rock = Rock wins
    PScissor + Paper = Scissor  wins
"""

import random

Options_List = ["Rock", "Paper", "Scissor"]


user_choice = input("Enter your move: ")
computer_choice = random.choice(Options_List)

print ( f"User choice = {user_choice}, Computer Choice = {computer_choice}" )



if user_choice == computer_choice:
    print("Both players chose the same: = Match Tie")
    
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Computer Won !!!")
    else:
        print("Computer Won !!!")
        
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Computer won !!!")
    else:
        print("You won !!!")
        
elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("You won !!!")
    else:
        print("Computer Won !!!")
