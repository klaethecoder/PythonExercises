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