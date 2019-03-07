from string import ascii_lowercase as lowercase


def cipherEncryption(key):
    alphabet = lowercase
    message = input("Please enter a message you want to be encrypted \n").lower()
    newMessage = ""

    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            newPosition = (position + key) % 26
            newMessage += alphabet[newPosition]
        else:
            newMessage += letter

    print(newMessage)

# try:
#     usersKey = int(input("What cipher key would you like? (Pick a number 1-26)"))
#     cipherEncryption(usersKey-1)

# except ValueError:
#     print("Please choose a number between 1-26")

def decoderRing(message,key):
    alphabet = lowercase
    newMessage = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.find(letter)
            newPosition = (position - key) % 26
            newMessage += alphabet[newPosition]
        else:
            newMessage += letter
    print(newMessage)

stuff = input("What is kind of message do you need to decode? \n")
key = int(input("What is the key that you used? \n"))-1
decoderRing(stuff, key)