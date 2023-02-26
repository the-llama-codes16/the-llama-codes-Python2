'''
Python Exercise 5.06
Written by: Iam Rasendi M. Saldua
Date: February 26, 2023

Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.

This program calls the conversion module, which contains the decToRep function.

'''


# Introduce the program
print("""This program allows conversion of a decimal number to binary, octal,
and hexadecimal.""")

import conversion

# Get user input
to_conv = int(input("Enter decimal number to convert: "))
base = int(input("\n2: binary\n8: octal\n16: hexadecimal\nEnter the base of the desired conversion: "))

# Perform task
print("\nConverting...\n")
print("Equivalent:", conversion.decToRep(to_conv, base))
