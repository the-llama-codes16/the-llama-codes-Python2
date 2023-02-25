'''
Python Exercise 3.4
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

Assume that the variables x and y refer to strings. Write a code segment that prints
these strings in alphabetical order. You should assume that they are not equal.

Input:
(string) stringA
(string) stringB

Output:
(string) both strings in alphabetical order

'''

#Introduce the program
print("This program prints the strings you input in alphabetical order.")

#Get user input
stringA = input("Enter first string: ")
stringB = input("Enter second string: ")

#Arrange the strings alphabetically
if stringA.lower() < stringB.lower():
    print("%s\n%s" % (stringA, stringB))
else:
    print("%s\n%s" % (stringB, stringA))
    
