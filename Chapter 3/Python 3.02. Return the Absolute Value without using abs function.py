'''
Python Exercise 3.2
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

Assume that x refers to a number. Write a code segment that prints the number’s
absolute value without using Python’s abs function.

Input:
(int) number

Output:
(int) absolute

'''

#Introduce the program
print("This program returns the absolute value of a number without using the abs function.")

#Get user input
number = int(input("Enter a number: "))

#Process input
if number < 0:
    number = -number
print("The absolute value of your input is %d" % number)

