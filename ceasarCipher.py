from string import ascii_lowercase as lowercase

alphabet = lowercase 
message = input("Please enter a message you want to be encrypted \n")
newMessage = []

for letter in message:
    position = alphabet.find(letter)
    newPosition = (position + 13) % 26
    newMessage.append(alphabet[newPosition])

print("".join(newMessage))
# cipherKey = input()
