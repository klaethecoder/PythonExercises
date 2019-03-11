import os
from profanityfilter import ProfanityFilter

pf = ProfanityFilter()

def readText():
    here = os.getcwd()
    quotes = open("./quotes.txt")
    contents = quotes.read()
    quotes.close()
    checkProfanity(contents)

def checkProfanity(text):
    censored = pf.censor(text)
    if "*" in censored:
        print("There is at lease one curse word in the text")
    else:
        print("No curse words found in the text.")

readText()