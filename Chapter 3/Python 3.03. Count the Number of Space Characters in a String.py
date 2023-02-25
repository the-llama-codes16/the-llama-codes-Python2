'''
Python Exercise 3.3
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

Write a loop that counts the number of space characters in a string. Recall that the
space character is represented as ' '.

Input:
(string) userInput

Output:
(int) numSpace
'''

#Introduce the program
print("This program counts the number of space characters in a string.")

#Get user input
userInput = input("Enter a string: ")

#Count the number of spaces
numSpace = 0
for char in userInput:
    if char == " ":
        numSpace += 1

#Print result
print("There are %d space characters in your entry." % numSpace)
