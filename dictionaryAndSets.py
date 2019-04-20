fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "sweet fruit, that grows in bunches",
    "lime": "a sour, green citrus fruit"
}

bike = {
    "make": "Honda",
    "model": "250 dream"
}

fruit["pear"] = "an odd shaped apple"

print(fruit)
for name in fruit:
    print("{0} is the key.\n {1} is the value".format(name, fruit[name]))

del fruit["lemon"]
print(fruit)

# while True:
#     dictKey = input("Please enter a fruit:\n")
#     if dictKey == "quit":
#         break
#     description = fruit.get(dictKey, "We don't have a ")
#     print(description)

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print("-"*40)

# for keys in fruit.keys():
#     print(keys)

# print("*"*40)

# for values in fruit.values():
#     print(values)

# print(fruit.items())

# Join and how it can be used.

alph = ["a", "b", "c", "d"]

newStr = ", ".join(alph)
print(newStr)

from string import ascii_lowercase as letters
from string import digits as numbers


newStr = ", ".join(letters)
print(newStr)

newStr = " mississippi, ".join(numbers)
print(newStr)

# This is how you can turn a list into a dictionary

stuff = [1,2,3,4,5]

def listToDict(arr):
    dictionary = {}
    for item in arr:
        index = arr.index(item)
        dictionary[index] = item
    print(dictionary)

names = ["Ryan", "Jenelle", "Addie", "Jayel"]
listToDict(names)

directions = { "NORTH" : "N", "SOUTH" : "S", "EAST" : "E", "WEST": "W"}

# userStuff = input("Please type a direction...\n").upper()
# words = userStuff.split()

# for word in words:
#     if word in directions:
#         userStuff = directions[word]
# print(userStuff)

veg = {"cabbage" : "Every child's favorite",
        "sprouts": "mmmm lovely",
        "spinach": "More Fruits please"}

print(fruit, veg)
print("-*"*40)
# The update command allows the two dictionaries to be combined.
veg.update(fruit)

print(veg)

newDict = fruit.copy()
newDict.update(veg)

print(newDict)

# Learning Sets: Don't have duplicates and arent in order

farmAnimals = {"sheep", "cow","hen"}

print(farmAnimals)
for animal in farmAnimals:
    print(animal)

import random

arr = []
while len(arr) < 12:
    arr.append(random.choice(range(30)))

print(arr)
print(set(arr))

even = set(range(0,40,2))
odd = set(range(1,40,2))

# This adds some new numbers to the existing sets. 
even.add(1)
odd.add(2)
print(even & odd)
print(even.intersection(odd))

print("-"*40)
print(even - odd)
print(even.difference(odd))

print("-"*40)
print(even.symmetric_difference(odd))
print(even ^ odd)

print("-"*40)


