"""
Python Exercise 4.14
Written by: Iam Rasendi M. Saldua
Date: December 5, 2022

Write a code segment that prints the names of all of the items in the current
working directory.

"""
import os

#Introduce the program
print("""This program prints the names of all of the items in the current working
directory.""")

#Perform task
currentDir = os.getcwd()
contents = os.listdir(currentDir)

#Print results
for content in contents:
    print(content)
        




