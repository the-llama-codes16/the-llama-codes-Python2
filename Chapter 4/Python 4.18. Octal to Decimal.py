"""
Python Exercise 4.18
Written by: Iam Rasendi M. Saldua
Date: December 27, 2022

Octal numbers have a base of eight and the digits 0–7. Write the scripts octalTo-
Decimal.py which converts numbers between the octal
and decimal representations of integers. 

"""

# Introduce the program
print("""This program converts an Octal number to its Decimal representation.""")

# Get user input
octal = int(input("Enter Octal number: "))

# Perform task
power = 0
decimal = 0
while octal > 0:
    digit = octal % 10
    octal //= 10
    decimal += digit * (8 ** power)
    power += 1

# Display result
print("Equivalent Decimal: %d\n" % decimal)
    



    
