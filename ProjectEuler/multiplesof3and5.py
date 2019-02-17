# Problem ID: 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
# ----------------------------------------------------------------------------------------

def threeor5():

    # Have a variable you can add the numbers that are multiples of 3 or 5.
    answer = 0

    # Loop through the range of numbers and add them to above variable
    for number in range(1000):    
        if number%3==0 or number%5==0:
            answer+=number

    # Return the answer once all numbers have been looped through
    return answer

# Print the answer to the problem in the Console.
print(threeor5())