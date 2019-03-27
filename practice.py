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

        