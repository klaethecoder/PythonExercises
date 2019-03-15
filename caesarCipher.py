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


answer = input("Press 1 to encrypt a message or 2 to dycrypt a message... \n")

try:
    answer = int(answer)
    if answer == 1 or answer == 2:
        if answer == 1:
            key = int(input("What is the key that you used? \n"))-1
            cipherEncryption(key)
        else:
            message = input("What is kind of message do you need to decode? \n")
            key = int(input("What is the key that you used? \n"))-1
            decoderRing(message, key)

    else:
        print("Please choose the numbers listed")


except ValueError:
    print("Please choose the numbers listed")