import random
rand = random.randint(1,10)


def isCorrect(stuff):
     if stuff == rand:
        print("Great Job, you guessed it.")

print("Please guess a number from 1 - 10 (You have 3 tries)")
guess = int(input())
count = 1
while count < 3:

    if guess < rand:
        print("Please guess higher")
        guess = int(input())
        isCorrect(guess)

    elif guess > rand:
        print("Please guess lower")
        guess = int(input())
        isCorrect(guess)
    else:
        print("You got it the first try")
    count +=1

print("Sorry, You have not guessed correctly.\nThe correct number was {}".format(rand))