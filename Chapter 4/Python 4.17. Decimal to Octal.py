"""
Python Exercise 4.17
Written by: Iam Rasendi M. Saldua
Date: December 27, 2022

Octal numbers have a base of eight and the digits 0–7. Write the scripts decimalToOctal.py
which converts numbers between the octal and decimal representations of integers. 

"""

# Introduce the program
print("""This program converts a Decimal number to its Octal equivalent.""")

# Get user input
decimal = int(input("Enter Decimal number: "))

# Perform task
octal = ""
while decimal > 0:
    remainder = decimal % 8
    decimal //= 8
    octal = str(remainder) + octal

# Display result
print("Equivalent Octal number: %s\n" % octal)


    
