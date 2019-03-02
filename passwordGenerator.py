import random as ran
import string as str

passLength = 12
strongPass = []

while passLength > 0:
    strongPass.append(ran.choice(str.printable))
    passLength -= 1

print(''.join(strongPass))