'''
Python Exercise 3.15
Written by: Iam Rasendi M. Saldua
Date: November 2, 2022

The German mathematician Gottfried Leibniz developed the following method
to approximate the value of pi:

pi / 4 = 1 - 1/3 + 1/5  - 1/7 + ...

Write a program that allows the user to specify the number of iterations used in
this approximation and that displays the resulting value.

Input:
(int) iterations - the number of iterations to be used in the approximation

Output:
(float) estPi - the estimated value of pi calculated using the formula and with
the specified number of iterations

'''
import math

#Introduce the program
print('''This program provides the approximate value of pi
using the formula developed by Gottfried Leibniz. 

pi / 4 = 1 - 1/3 + 1/5  - 1/7 + ...

The user provides the number of iterations to be used.''')

#Get user input
iterations = int(input("\nNumber of iterations: "))

#Perform computation
denominator = 1
term = 1
estPi = 0
while (term <= iterations):
    if (term % 2 == 0):
        denominator = -denominator
        
    estPi += 1/denominator
    denominator = abs(denominator) + 2
    term += 1

estPi *= 4

#Display the result and compare with Python's built-in value of pi
print("\nPython's value of pi: %f" % math.pi)
print("Calculated value of pi using %d terms: %f\n" % (iterations, estPi))

















