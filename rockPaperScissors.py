import random
import time

computer = random.choice("rsp")
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

def whoWon(answer):
    if answer == computer:
        print("It's a Draw!!")
    elif answer == "r" and computer != "p":
        print("Congrats, You Win!!!")
    else:
        print("Sorry, You Lost!!!")

def computerPicked(x):
    if x == "r":
        print("The Computer picked Rock")
    elif x == "s":
        print("The Computer picked Scissors")
    else:
        print("The Computer picked Paper")

def gameTime():
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
        
        


gameTime()