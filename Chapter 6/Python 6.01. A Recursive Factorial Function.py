'''
Python Exercise 6.01
Written by: Iam Rasendi M. Saldua
Date: March 14, 2023

The factorial of a positive integer n, fact(n), is defined recursively as follows:
fact(n) = 1, when n = 1
fact(n) = n * fact(n - 1), otherwise
Define a recursive function fact that returns the factorial of a given positive
integer.

'''

# Introduce the program
print("""This program calculates the factorial of a positive integer
using a recursive design.""")

# Get user input
n = int(input("\nEnter a positive number: "))

# Perform task
def fact (num:int):
    if num == 1:
        return 1
    else:
        return (num * fact(num - 1))

print("\nFactorial of %d is %d" % (n, fact(n)))    
