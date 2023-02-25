'''
Python Exercise 2.1
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

This rogram calculates the surface area of a cube given the length of an edge.
Input: (float) edge
Returns: (float) surface area

'''
import math

print("This program calculates the total surface area of a cube.")
edge = float(input("Enter the length of one edge: "))

surfaceArea = 6 * (edge ** 2)

print("The total surface area is " + str(surfaceArea))

