'''
Python Exercise 2.8
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.
Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and 
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North 
Pole and the equator.
• A nautical mile is 1 minute of an arc.

Input:
(float) kilometer

Output:
(float) nautMiles

'''

import math

print("This program calculates the equivalent nautical miles of a given distance in kilometers.")

#User Input
kilometer = float(input("\nEnter a distance in kilometers: "))

#Calculate equivalent nautical miles
nautMile = kilometer * (1/10000) * 90 * 60

#Display Output
print("\nEquivalent distance in nautical miles: " + str(nautMile))
