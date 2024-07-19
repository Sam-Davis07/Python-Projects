
#   Rock... Paper... Scissor... Game

#   In this game Rock = 0, Paper = 1 and Scissor = 2

#   Importing modules

import random
from ASCII_images import rock,paper,scissors

print("Welcome! Let's a play a game...\n")
print("Rock... Paper... Scissor...\n")

l1 = [rock, paper, scissors]  #  List l1 containing ASCII images of rock, paper, sccissor from module 

comp_ch = random.randint(0,2)  # Taking computer's choice by using random module

user_ch = int(input("Enter '0' for Rock , '1' for Paper , '2' for scissors :")) # Taking user's choice 
print(l1[user_ch])  # Displaying user's choice in ASCII image

print("Computer's Choice:") 
print(l1[comp_ch])  # Displaying computer's choice in ASCII image

# Let's see who wins 

if user_ch == 0 : # Rock

    if comp_ch == 0 : # Rock
        print("Draw!")

    elif comp_ch == 1 : # Paper
        print("Computer won!")

    else : # Scissors
        print("You won!")

elif user_ch == 1 : # Paper

    if comp_ch == 0 : # Rock
        print("You won!")

    elif comp_ch == 1 : # Paper
        print("Draw!")

    else : # Scissors 
        print("Computer won!")

elif user_ch == 2 : # Scissors

    if comp_ch == 0 : # Rock
        print("Computer won!")

    elif comp_ch == 1 : # Paper
        print("You won!")

    else : # Scissors 
        print("Draw!")

else:
    print("Please Enter a valid input!")
