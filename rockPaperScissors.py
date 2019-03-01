import random # Imports the Random Module
import time   #Imports the Time Module

#Checks to see if the user has given a correct choice for the game
def checker(stuff):
    error = 1
    alt = True
    if stuff == "r" or stuff == "s" or stuff == "p":
        alt = False
    while alt and error<3:
        print("Please pick one of the before mentioned options")
        time.sleep(.7)
        print("Rock (r), Paper (p) or Scissors (s)?")
        choice = input().lower()
        error+=1
        if choice == "r" or choice == "s" or choice == "p":
            alt = False
    if error == 3:
        print("Too many wrong answers. ")

#Checks to see who has won the game
def whoWon(answer, computer):
    score = 0  
    if answer == computer:
        print("It's a Draw!!")
    elif answer == "r" and computer != "p":
        print("Congrats, You Win!!!")
        score += 1
    elif answer == "p" and computer != "s":
        print("Congrats, You Win!!!")
        score += 1
    elif answer == "s" and computer != "r":
        print("Congrats, You Win!!!")
        score +=1
    else:
        print("Sorry, You Lost")
    return score

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
    rounds = 1
    print("Welcome to Rock, Paper Scissors...")
    time.sleep(.5)
    print("Good Luck... You will need it...")
    time.sleep(.8)
    print("How many rounds would you like (Pick 1-5)?")
    rounds = input()
    try:
        rounds = int(rounds)
        overallRounds = rounds
        if rounds <=5 and rounds > 0:
            i = 1
            score = 0
            while rounds >= 1:
                computer = random.choice("rsp") #Picks a Random Choice for the computer
                print("Round %d:" % i)
                print("Rock (r), Paper (p) or Scissors (s)?")
                result = input().lower()
                checker(result)
                if result == "r":
                    print("You picked Rock")
                    time.sleep(.3)
                    computerPicked(computer)
                    score+= whoWon(result, computer)
                elif result == "s":
                    print("You picked Scissors")
                    time.sleep(.3)
                    computerPicked(computer)
                    score+= whoWon(result, computer)
                elif result =="p":
                    print("You picked Paper")
                    time.sleep(.3)
                    computerPicked(computer)
                    score+= whoWon(result, computer)
                else:
                    print("GameOver")
                rounds -= 1
                i+= 1
        else:
            print("You must pick a number 1-5")
            gameTime()
        print("You won %s out of %s" % (score, overallRounds))
    except ValueError:
        print("Please type in a number!!!")

#This statement initiates the Game. It starts by prompting the User to enter their choice.
gameTime()