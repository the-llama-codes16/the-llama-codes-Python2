'''
Python Exercise 3.9
Written by: Iam Rasendi M. Saldua
Date: November 1, 2022

Approximating Square Roots

Input:
(int or float) a positive number: num

Output:
(float) program's estimate: progAns
(float) Python's estimate: pyAns

'''

import math

#Introduce the program
print("This program attempts to approximate the square root of a given number following Newton's algorithm. The result will be compared with Python's built-in function math.sqrt")

#Get user input
num = float(input("Enter a positive number: "))
if num < 0:
    num = -num

#Calculate the estimated square root
x1 = (1 + num / 1) / 2
x2 = (x1 + num / x1) / 2
while x1 - x2 > 0.000001:
    x1 = x2
    x2 = (x1 + num / x1) / 2

#Display results
print("The program's estimate: %f" % x2)
print("Python's estimate: %f" % math.sqrt(num))


    








