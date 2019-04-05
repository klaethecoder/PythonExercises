fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "goof for making cider",
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

