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