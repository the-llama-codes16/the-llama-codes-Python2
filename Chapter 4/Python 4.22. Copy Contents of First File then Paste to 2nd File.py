"""
Python Exercise 4.22
Written by: Iam Rasendi M. Saldua
Date: February 6, 2023

Write a script that prompts the user for the
names of two text files. The contents of the first file should be input
and written to the second file.
"""

# Introduce the program
print("""This program takes 2 inputs, which are the names of 2 text files.
The contents of the first file will be written to the second file.""")

# Get user input
first_file = input("\nFirst file: ")
second_file = input("Second file: ")

# Perform task
# Open first file and read it
if not(".txt" in first_file):
    first_file = first_file + ".txt"
fhand1 = open(first_file, 'r')
file_1_contents = fhand1.read()
fhand1.close()

# Open second file to write contents
if not(".txt" in second_file):
    second_file = second_file + ".txt"
fhand2 = open(second_file, 'a')
fhand2.write(file_1_contents)
fhand2.close()

# Display success message
print("\nReading and writing finished. Please check the files.\n")
