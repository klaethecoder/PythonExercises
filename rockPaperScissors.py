import random # Imports the Random Module
import time   #Imports the Time Module

computer = random.choice("rsp") #Picks a Random Choice for the computer

#Checks to see if the user has given a correct choice for the game
def checker(stuff):
    alt = True
    if stuff == "r" or stuff == "s" or stuff == "p":
        alt = False
    while alt:
        print("Please pick one of the before mentioned options")
        time.sleep(.7)
        print("Rock (r), Paper (p) or Scissors (s)?")
        choice = input().lower()
        if choice == "r" or choice == "s" or choice == "p":
            alt = False

#Checks to see who has won the game
def whoWon(answer):
    if answer == computer:
        print("It's a Draw!!")
    elif answer == "r" and computer != "p":
        print("Congrats, You Win!!!")
    else:
        print("Sorry, You Lost!!!")

#Prints out a statement of what the computer picked.
def computerPicked(x):
    if x == "r":
        print("The Computer picked Rock")
    elif x == "s":
        print("The Computer picked Scissors")
    else:
        print("The Computer picked Paper")

#This is the Game itself. It uses the above mentioned methods to run the game. 
def gameTime():
    print("Welcome to Rock, Paper Scissors...")
    time.sleep(.5)
    print("Good Luck... You will need it...")
    time.sleep(.8)
    print("Rock (r), Paper (p) or Scissors (s)?")
    result = input().lower()
    checker(result)
    if result == "r":
        print("You picked Rock")
        time.sleep(.3)
        computerPicked(computer)
        whoWon(result)
    elif result == "s":
        print("You picked Scissors")
        time.sleep(.3)
        computerPicked(computer)
        whoWon(result)
    else:
        print("You picked Paper")
        time.sleep(.3)
        computerPicked(computer)
        whoWon(result)

#This statement initiates the Game. It starts by prompting the User to enter their choice.
gameTime()