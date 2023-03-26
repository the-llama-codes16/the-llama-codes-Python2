'''
Python Exercise 6.04
Written by: Iam Rasendi M. Saldua
Date: March 19, 2023

Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function.

'''
# Introduce the program
print("""\nThis program uses the filter function with a lambda function
to pick out the positive numbers from a list of numbers.""")

# Perform task
numbers = [-1, 2, 3, -4, -5, -6, 7, -8, 9, 10]
print("\nThe original list:", numbers, "\n\nUsing filter function...\n")
pos_num = list(filter(lambda num: num >= 1, numbers))
print("The new list:", pos_num, "\n")

