'''
Python Exercise 3.13
Written by: Iam Rasendi M. Saldua
Date: November 2, 2022

A standard science experiment is to drop a ball and see how high it bounces.
Once the “bounciness” of the ball has been determined, the ratio gives a bounciness
index. For example, if a ball dropped from a height of 10 feet bounces 6 feet
high, the index is 0.6, and the total distance traveled by the ball is 16 feet after
one bounce. If the ball were to continue bouncing, the distance after two bounceswould be
10 ft + 6 ft + 6 ft + 3.6 ft = 25.6 ft. Note that the distance traveled for
each successive bounce is the distance to the floor plus 0.6 of that distance as the
ball comes back up. Write a program that lets the user enter the initial height
from which the ball is dropped and the number of times the ball is allowed to
continue bouncing. Output should be the total distance traveled by the ball.

Input:
(float) height - the initial height
(int) numBounces

Output:
(float) height - the total distance travelled by the ball

'''

#Introduce the program
print(''' This program gets the initial height a ball is dropped from and the number of
bounces to calculate the total distance the ball travels. The bounciness index is 0.6.
Note: Minimum number of bounces is 1. ''')

#Get user input
height = float(input("\nEnter initial height: "))
numBounces = int(input("Enter number of bounces: "))

#Perform computation
#Minimum number of bounces is 1
if (numBounces < 1):
    numBounces = 1

totalDis = height * 1.6
bounceCount = 1
while (bounceCount < numBounces):
    height *= 0.6
    totalDis += (height * 1.6)
    bounceCount += 1

#Display result
print("Total distance travelled: %.2f" % totalDis)
print("Last height: %.2f\n" % (height * 0.6))









