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
#     description = fruit.get(dictKey)
#     print(description)
