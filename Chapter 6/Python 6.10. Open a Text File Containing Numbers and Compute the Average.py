'''
Python Exercise 6.10
Written by: Iam Rasendi M. Saldua
Date: March 26, 2023

Write a program that computes and prints the average of the numbers in a text
file. You should make use of two higher-order functions to simplify the design.
'''
import functools

# Introduce the program
print("""This program computes and prints the average of the numbers in a text
file.""")

# Get user input
fname = input("Enter file name: ")
if not(".txt" in fname):
    fname = fname+ ".txt"

# Open file and read contents
fhand = open(fname)
numbers = list()
for line in fhand:
    numbers.append(int(line))

# Compute and display the average
average = functools.reduce(lambda x, y: x + y, numbers)
average = average / len(numbers)
print("Average:", average)
    
