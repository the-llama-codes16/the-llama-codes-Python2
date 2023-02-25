'''
Python Exercise 4.08
Written by: Iam Rasendi M. Saldua
Date: November 26, 2022

A program that converts a decimal number to a bit string

Input:
(int) decimal

Output:
(str) bit
'''

#Introduce the program
print("This program converts a decimal number to a bit string.")

#Get user input
decimal = int(input("Please enter a decimal number: "))

#Perform conversion
bit = ""
while decimal > 0:
    digit = decimal % 2
    decimal //= 2
    bit = str(digit) + bit

#Print result
print("Equivalent binary string: %s" % bit)
    



        






