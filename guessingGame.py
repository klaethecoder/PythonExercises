# Import of the module Random to the file.
import random

# Randomly chooses the computer's guess for the game
computer = random.choice(range(1,11))
# Starts off the game having one guess on the counter.
guesses = 1
# Gets the user input and makes it an Integer
userGuess = int(input("Guess a number from 1 - 10\n"))

# While loop checks to see if there has been 5 guess or that the user hasn't guessed the computer's number yet
while guesses < 5 and userGuess != computer:
    # if the loop is re-ran, then it will allow the user to guess again.
    userGuess = int(input("Guess a number from 1 - 10\n"))
    # if statment that will check and see if the user has guessed the computer's answer
    if userGuess == computer:
        print("You won !!!!")
        # Breaks out of the loop
        break
    # Adds a count to the guess variable that was initialized outside of the loop
    guesses += 1
# Checks to see if the guesses variable is greater than or equal to 5 and prints a statment
if guesses >= 5:
    print("Game Over... Sorry, You Lost")
