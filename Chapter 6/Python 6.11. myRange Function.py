'''
Python Exercise 6.11
Written by: Iam Rasendi M. Saldua
Date: March 26, 2023

Define and test a function myRange. This function should behave like Python’s
standard range function, with the required and optional arguments, but it should
return a list. Do not use the range function in your implementation! (Hints:
Study Python’s help on range to determine the names, positions, and what to do
with your function’s parameters. Use a default value of None for the two optional
parameters. If these parameters both equal None, then the function has been
called with just the stop value. If just the third parameter equals None, then the
function has been called with a start value as well. Thus, the first part of the function’s
code establishes what the values of the parameters are or should be. The
rest of the code uses those values to build a list by counting up or down.)
'''

# Introduce the program
print("""This program attempts to create a function called myRange,
which behaves like the range function, but returns a list instead.

Sample result:
myRange(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
myRange(1, 10) = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myRange(1, 10, 2) = [1, 3, 5, 7, 9]""")

# Define the function
def myRange(*arguments):
    if len(arguments) == 1:
        start = 0
        stop = arguments[0]
        step = 1
    elif len(arguments) == 2:
        start = arguments[0]
        stop = arguments[1]
        step = 1
    elif len(arguments) == 3:
        start = arguments[0]
        stop = arguments[1]
        step = arguments[2]
    else:
        print("Invalid input. Please enter 1 - 3 int arguments.")
        return
    
    numbers = list()
    num = start
    if start < stop:
        while num < stop:
            numbers.append(num)
            num = num + step
        return numbers
    else:
        while num > stop:
            numbers.append(num)
            num = num + step
        return numbers
    
# Get user input
print("The myRange function has been defined and is ready for use. We test the samples above.")
print(myRange(10))
print(myRange(1, 10))
print(myRange(1, 10, 2))
    
