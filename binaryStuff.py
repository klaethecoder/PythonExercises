# Binary gots from 2^0 - 2^8; You also dont have to import binary(base 2).
for i in range(17):
    print("{0:>2} in binary is {0:08b}".format(i))


for i in range(17):
    print("{0:>2} in hex is {0:02x}".format(i))

# How to make sure the computer knows we are writing in hexadecimal (base 16)
x = 0x20
y = 0x0a

print(x)
print(y)
print(x*y)

# Subtracting in hexadecimal
print(0x8a - 0x4e)

# Octal is base 8 that goes from 8^0 - 8^3

# ---------------------------------------------------------
# CHALLENGE:
# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.

powers = []
for power in range(15, -1, -1):
    # Changing this from 2 to 8 will make it an octal
    powers.append(2**power)

print(powers)

x = int(input("Please enter a number...\n"))

for power in powers:
    bit = x//power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit//power, end = '')
    x %= power