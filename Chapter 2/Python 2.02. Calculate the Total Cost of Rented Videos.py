'''
Python Exercise 2.2
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who 
like to buy LP record albums. The store rents new videos for $3.00 a night, and 
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video 
can use to calculate the total charge for a customer’s video rentals. The program 
should prompt the user for the number of each type of video and output the total 
cost.

Input:
(int) newVideos
(int) oldies

Output:
(float) totalCost

'''

import math

print("""This program computes the total cost of rented videos.
New Videos = $3.00/night
Old Videos = $2.00/night """)

#User Input
newVideos = int(input("Number of new videos rented: "))
oldies = int(input("Number of old videos rented: "))

#Calculate Total Cost
totalCost = (newVideos * 3.00) + (oldies * 2.00)

#Display Total Cost
print("Total Cost: $" + str(totalCost))

