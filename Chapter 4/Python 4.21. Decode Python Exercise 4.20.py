"""
Python Exercise 4.21
Written by: Iam Rasendi M. Saldua
Date: February 2, 2023

Write a script that decrypts a message coded by the method used in Exercise 4.20.

Pseudocode
Get input
for each character,
    get the equivalent ASCII value
    add 1 to the ASCII value
    convert it to bits
    concatenate these bits to the resulting string
    add the delimiter character
for each item in the resulting string,
    shift each to the left

Input: (str) encoded message in binary digits
Output: (str) decoded message in alphanumeric characters

Pseudocode
Get input
for each character in the input:
    shift each to the right
split the string with the space as delimiter
for each item in the list: (each item is a series of binary digits)
    get the equivalent decimal value
    subtract 1
    get the equivalent alphanumeric character
    add to the output string
    
    

"""
import math

# Introduce the program
print("""This program decodes the resulting encoded message produced by Exercise 4.20""")

# Get user input
encoded = input("Enter encoded message: ")

# Perform character shift to the right
decoded = ""
length = len(encoded)
last_char = encoded[length - 1]
for i in range(0, length - 1):
    decoded = decoded + encoded[i]
decoded = last_char + decoded

# Decode
char_list = decoded.split()
decoded_final = ""
for char in char_list:
    decimal = 0
    max_exp = len(char) - 1
    for bit in char:
        decimal = decimal + (int(bit) * pow(2, max_exp))
        max_exp = max_exp - 1
    decimal = decimal - 1
    char_msg = chr(decimal)
    decoded_final = decoded_final + char_msg

# Print result
print("The secret message is: %s" % decoded_final)
        
        
    


    
