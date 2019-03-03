import time, webbrowser

def hours2secs(hours):
    return(hours*60)*60

print(hours2secs(2))

def takeABreak():
    print("The program has started")
    rest = 1
    while rest <= 3:
        time.sleep(2)
        webbrowser.open("https://www.google.com")
        rest +=1
    print("Program Completed Successfully")
takeABreak()