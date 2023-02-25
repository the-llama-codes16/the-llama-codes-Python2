'''
Python Exercise 4.07
Written by: Iam Rasendi M. Saldua
Date: November 26, 2022

A program that converts a bit string to a decimal number.

Input:
(str) bit

Output:
(int) decimal
'''

#Introduce the program
print("This program converts a bit string to a decimal number.")

#Get user input
bit = input("Enter a binary string (0s and 1s): ")

#Perform conversion
count = len(bit)
decimal = 0

for char in bit:
    decimal += int(char) * 2**(count - 1)
    count -= 1

#Display result
print("Equivalent decimal number: %d\n" % decimal)





        






