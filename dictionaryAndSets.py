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
for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print("-"*40)

for keys in fruit.keys():
    print(keys)

print("*"*40)

for values in fruit.values():
    print(values)

print(fruit.items())

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

