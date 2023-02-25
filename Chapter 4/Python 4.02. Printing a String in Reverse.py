'''
Python Exercise 4.02
Written by: Iam Rasendi M. Saldua
Date: November 18, 2022

Assume that the variable myString refers to a string. Write a code segment that
uses a loop to print the characters of the string in reverse order.

Input:
(str) input_string

Output:
Print the characters in reverse order
'''

#Introduce the program
print("This program will print the characters of a string in reverse order.")

#Get user input
input_string = input("\nEnter string: ")

#Print characters in reverse order
rev_count = len(input_string)
for i in range(rev_count - 1, -1, -1):
    print("%s" % (input_string[i]), end = "")










