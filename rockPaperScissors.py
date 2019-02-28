def checker(stuff):
    alt = True
    if stuff == "r" or stuff == "s" or stuff == "p":
        alt = False
    while alt:
        print("Please pick one of the before mentioned options")
        print("Rock (r), Paper (p) or Scissors (s)?")
        choice = input().lower()
        if choice == "r" or choice == "s" or choice == "p":
            alt = False



def gameTime():
    print("Rock (r), Paper (p) or Scissors (s)?")
    result = input().lower()
    checker(result)
    if result == "r":
        print("You picked Rock")
    elif result == "s":
        print("You picked Scissors")
    else:
        print("You picked Paper")
        
        


gameTime()