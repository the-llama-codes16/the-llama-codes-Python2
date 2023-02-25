'''
Python Exercise 3.11
Written by: Iam Rasendi M. Saldua
Date: November 1, 2022

Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle.

Input:
(float) three sides of a triangle: sideA, sideB, sideC

Output:
Indicate whether or not the triangle is a right triangle
'''

import math

#Introduce the program
print("This program determines if a given triangle is a right triangle.")

#Get user input
sideA = float(input("\nFirst side: "))
sideB = float(input("Second side: "))
sideC = float(input("Third side: "))

#Check if the triangle is a right triangle
if (sideA**2 + sideB**2 == sideC**2):
    right = True
elif (sideB**2 + sideC**2 == sideA**2):
    right = True
elif (sideA**2 + sideC**2 == sideB**2):
    right = True
else:
    right = False

#Display results
if (right == True):
    print("\nThe triangle is a right triangle.")
else:
    print("\nThe triangle is not a right triangle.")
    
    





