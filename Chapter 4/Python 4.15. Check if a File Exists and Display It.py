"""
Python Exercise 4.15
Written by: Iam Rasendi M. Saldua
Date: December 12, 2022

Write a code segment that prompts the user for a filename. If the file exists,
the program should print its contents on the terminal. Otherwise, it should print an
error message.

"""

import os

#Introduce the program
print("""This program allows you to enter a filename and
determines if the file exists.""")

#Perform task
file_name = input("\nEnter file name including the file extension: ")
current = os.getcwd()
dir_list = os.listdir(current)

if file_name in dir_list:
    print("The file exists.\nContents:")
    fhand = open(file_name, "r")
    for line in fhand:
        print(line, end = "")
    fhand.close()
else:
    print("The file does not exist.\n")
