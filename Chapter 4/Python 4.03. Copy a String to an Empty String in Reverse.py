'''
Python Exercise 4.03
Written by: Iam Rasendi M. Saldua
Date: November 18, 2022

Assume that the variable myString refers to a string, and the variable
reversedString refers to an empty string. Write a loop that adds the characters
from myString to reversedString in reverse order.

Input:
(str) my_string

Output:
Print reversed_string
'''

#Introduce the program
print("""This program will add the characters of a string to an empty string
in reverse order.\n""")

#Get user input
my_string = input("Enter string: ")

#Perform task
reversed_string = ""
my_str_len = len(my_string)
for i in range(my_str_len - 1, -1, -1):
    reversed_string += my_string[i]

#Print results
print(reversed_string)








