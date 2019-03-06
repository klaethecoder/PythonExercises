from string import ascii_lowercase as lowercase

alphabet = lowercase
message = input("Please enter a message you want to be encrypted \n")
newMessage = ""

for letter in message:
    if letter in alphabet:
        position = alphabet.find(letter)
        newPosition = (position + 13) % 26
        newMessage += alphabet[newPosition]
    else:
        newMessage += letter

print(newMessage)
