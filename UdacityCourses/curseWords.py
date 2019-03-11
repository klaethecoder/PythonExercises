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
    print(censored)

readText()