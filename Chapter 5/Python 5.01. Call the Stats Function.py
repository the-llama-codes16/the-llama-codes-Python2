'''
Python Exercise 5.01
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.

This is the function that will call Stats.py

'''
import string
import Stats

# Introduce the program
print("""This program will call Stats.py and use the functions defined inside
that module.""")

# Perform task
num_list = list()
print("""\nYou will need to enter the numbers you wish to include in the list.
Please enter "done" if you are finished.""")

# Get user input
while True:
    entry = input(">>>")
    if entry.lower() == "done":
        break
    num_list.append(int(entry))
    
# Compute 
print("\nYour list is", num_list)
median_res = Stats.median(num_list)
mode_res = Stats.mode(num_list)
mean_res = Stats.mean(num_list)
print("The results are:\nMedian: ", median_res,"\nMode: ", mode_res, "\nMean: ", mean_res)

