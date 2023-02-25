'''
Python Exercise 3.10
Written by: Iam Rasendi M. Saldua
Date: November 1, 2022

Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.

Input:
(float) three sides of a triangle: sideA, sideB, sideC

Output:
Indicate whether or not the triangle is an equilateral triangle
'''

#Introduce the program
print("This program accepts three sides of a triangle and determines if it is an equilateral triangle.")

#Get user input 
sideA = float(input("\nFirst side: "))
sideB = float(input("Second side: "))
sideC = float(input("Third side: "))

#Determine if the triangle is an equilateral triangle
if (sideA == sideB and sideA == sideC):
    print("\nThe triangle is an equilateral triangle")
else:
    print("\nThe triangle is not an equilateral triangle.")
    






