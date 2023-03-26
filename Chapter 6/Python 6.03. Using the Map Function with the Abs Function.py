'''
Python Exercise 6.03
Written by: Iam Rasendi M. Saldua
Date: March 19, 2023

Write the code for a mapping that generates a list of the absolute values of the numbers
in a list named numbers.

'''
import math

# Introduce the program
print("""\nThis progran uses the mapping function to generate a list
      of the absolute values of a list of numbers.""")
numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
print("The list:", numbers)

# Perform task
print("\nUsing map function...")
abs_list = list(map(abs, numbers))
print("\nNew list:", abs_list, "\n")

