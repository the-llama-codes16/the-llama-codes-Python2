'''
Python Exercise 2.5
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

The kinetic energy of a moving object is given by the formula KE = 0.5 *(m*v)**2
where m is the object’s mass and v is its velocity. Modify the program you created 
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Input:
(float) mass
(float) velocity

Output:
(float) momentum
(Float) kineticEnergy

'''

import math

print("This program calculates an object's momentum and Kinetic energy.")

#User Input
mass = float(input("\nMass (in kg): "))
velocity = float(input("Velocity (in m/s): "))

#Calculate momentum and Kinetic Energy
momentum = round((mass * velocity), 2)
kineticEnergy = round((0.5 * mass * (velocity ** 2)), 2)

#Display Output
print("\nMomentum: " + str(momentum))
print("Kinetic Energy: " + str(kineticEnergy))

