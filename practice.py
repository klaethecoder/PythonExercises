from string import digits
def reverseString(phrase):
    str = ""
    for letter in phrase:
        str = letter + str
    print(str)

def sayHello(name="User"):
    print("Hello "+ name)



reverseString("Ryan")
sayHello()
sayHello("Ryan")

number = "0,123,456,2324,678,345,667"
for i in number:
    if i in digits:
        print("The number is: {}".format(i))

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
numbers.sort()
print(numbers)

numbers = sorted(even + odd, reverse=True)
print(numbers)

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "sausage", "bacon", "cheese"])
menu.append(["egg", "sausage", "bacon", "cheese", "potatoes"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam","egg", "bacon", "spam"])
menu.append(["spam","egg", "spam", "spam","bacon"])

# for meal in menu:
#     if not "spam" in meal:
#         print(meal)

for meal in menu:
    if not "spam" in meal:
        for item in meal:
            print(item)
        print("-"*20)

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

def looper(el):
    times = len(el)
    myIter = iter(el)
    while times >= 1:
        print(next(myIter))
        times -= 1

# looper("1234567890")
# print("*"*20)
# looper([1,2,3,4,5,6,7,8,9,0])

element = [1,2,3,4,5,6,7,8,9,0]
times = len(element)
myIter = iter(element)
for item in range(times):
    print(next(myIter))

for i in range(9,1000,9):
    print(i)

print(list(range(9,1000,9)))

# Tuples are immutable.
t = "a", "b", "c"

print(t)

# Python reads things from right to left and that is why there is no errors with the variables below

a = b = c = d = 12

print(c)

# Multiple variable assignments
e,f = 13,14

print(e)
print(f)

# Swapping the variable values

e,f = f,e

print(e)
print(f)
