'''
Python Exercise 5.05
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

In Chapter 4, we developed an algorithm for converting from binary to decimal.
You can generalize this algorithm to work for a representation in any base.
Instead of using a power of 2, this time you use a power of the base. Also, you use
digits greater than 9, such as A . . . F, when they occur. Define a function named
repToDecimal that expects two arguments, a string, and an integer. The second
argument should be the base. For example, repToDecimal("10", 8) returns
8, whereas repToDecimal("10", 16) returns 16. The function should use a
lookup table to find the value of any digit. Make sure that this table (it is actually
a dictionary) is initialized before the function is defined. For its keys, use the 10
decimal digits (all strings) and the letters A . . . F (all uppercase). The value stored
with each key should be the integer that the digit represents. (The letter 'A' associates
with the integer value 10, and so on.) The main loop of the function should
convert each digit to uppercase, look up its value in the table, and use this value
in the computation. Include a main function that tests the conversion function
with numbers in several bases.

This program calls the conversion module, which contains the repToDec function.

'''

import conversion

# Introduce the program
print("""This program allows conversion of a binary, octal, or hexadecimal number
to decimal.""")

# Get user input
base = int(input("\n2: binary\n8: octal\n16: hexadecimal\nEnter the base of the number to convert: "))
to_conv = input("Enter number to convert: ")

# Perform task
print("\nConverting...\n")
print("Equivalent decimal number:", conversion.repToDec(to_conv, base))
