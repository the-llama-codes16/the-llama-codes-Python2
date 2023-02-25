'''
Python Exercise 2.7
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

Light travels at 3 * 10**8 meters per second. A light-year is the distance a light beam 
travels in one year. Write a program that calculates and displays the value of a 
light-year.

Input:
None

Output:
(float) lightYearDistance

'''

import math

print("This program displays the value of a light year, or the distance traveled by light in one year")

#Calculate lightYearDistance
secondsInAYear = 365 * 24 * 60 * 60
lightYearDistance = secondsInAYear * 3 * 10 ** 8

#Display Output
print("\nValue of 1 light-year in meters: " + str(lightYearDistance))
