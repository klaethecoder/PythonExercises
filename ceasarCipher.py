from string import ascii_lowercase as lowercase

usersKey = int(input("What cipher key would you like? (Pick a number 1-26)"))
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

cipherEncryption(usersKey-1)