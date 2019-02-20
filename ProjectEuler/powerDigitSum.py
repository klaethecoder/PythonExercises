# Problem 16:
# 2 to the 15th power = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2 to the 1000th power?

# Create a function for the problem
def sumOfPower(n):
# return the Sum of each digit in the List that was created by the number 2 to the nth power
    return sum([int(i) for i in str(2**n)])

# Print the results of the function to the 1000th Power
print(sumOfPower(1000))