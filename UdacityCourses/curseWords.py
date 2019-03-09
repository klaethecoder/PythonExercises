import os
import urllib.request as url
import profanity

from profanity_filter import ProfanityFilter

pf = ProfanityFilter()
out = pf.censor("That's bullshit!")
print(out)

def readText():
    here = os.getcwd()
    quotes = open("./quotes.txt")
    contents = quotes.read()
    quotes.close()
    checkProfanity(contents)

def checkProfanity(text):
   connection =  url.urlopen("http://www.wdylike.appspot.com/?q="+ text)
   output = connection.read()
   print(output)
   connection.close()



# readText()