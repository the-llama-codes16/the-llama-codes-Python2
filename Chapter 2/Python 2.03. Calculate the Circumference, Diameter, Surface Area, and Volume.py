'''
Python Exercise 2.3
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

Write a program that takes the radius of a sphere (a floating-point number) as 
input and then outputs the sphere’s diameter, circumference, surface area, and 
volume.

Input:
(float) radius

Output:
(float) diameter
(float) circumference
(float) surface area
(float) volume

'''
import math

print("""This program takes a radius as an input and gives the following:
diameter
circumference
surface area
volume""")

#User Input
radius = float(input("\nRadius: "))

#for Diameter
diameter = round((2 * radius), 2)

#for Circumference
circum = round((math.pi * (radius ** 2)), 2)

#for surface area
surfaceArea = round((4 * math.pi * (radius ** 2)), 2)

#for volume
volume = round(((4 / 3) * math.pi * (radius ** 3)), 2)

#display output
print("\nDiameter: " + str(diameter))
print("Circumference: " + str(circum))
print("Surface Area: " + str(surfaceArea))
print("Volume: " + str(volume))
