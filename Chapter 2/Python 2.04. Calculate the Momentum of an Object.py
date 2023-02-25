'''
Python Exercise 2.4
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

An object’s momentum is its mass multiplied by its velocity. Write a program 
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as 
inputs and then outputs its momentum.

Input:
(float) mass
(float) velocity

Output:
(float) momentum

'''

import math

print("This program calculates an object's momentum")

#User Input
mass = float(input("\nMass (in kg): "))
velocity = float(input("Velocity (in m/s): "))

#Calculate momentum
momentum = round((mass * velocity), 2)

#Display Output
print("\nMomentum: " + str(momentum))
