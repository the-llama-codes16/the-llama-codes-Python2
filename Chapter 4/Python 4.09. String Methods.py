'''
Python Exercise 4.09
Written by: Iam Rasendi M. Saldua
Date: November 27, 2022

Assume that the variable data refers to the string "Python rules!". Use a string
method to perform the following tasks:
a. Obtain a list of the words in the string.
b. Convert the string to uppercase.
c. Locate the position of the string "rules".
d. Replace the exclamation point with a question mark.

Input:
(str) string
'''

import string

#Introduce the program
print("""This program uses string methods to perform the required operations.
The string: \"Python rules!\"""")

#Perform operations
string = "Python rules!"

print("a. Obtain a list of the words in the string.")
print(string.split())

print("b. Convert the string to uppercase.")
print(string.upper())

print("c. Locate the position of the string \"rules\".")
print(string.find("rules"))

print("d. Replace the exclamation point with a question mark.")
newStr = ""
for char in string:
    if char == "!":
        newStr += "?"
    else:
        newStr += char
print(newStr)



        






