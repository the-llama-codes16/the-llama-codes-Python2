'''
Python Exercise 3.8
Written by: Iam Rasendi M. Saldua
Date: November 1, 2022

The log2 of a given number N is given by M in the equation N 5 2M. Using integer
arithmetic, the value of M is approximately equal to the number of times N can be
evenly divided by 2 until it becomes 0. Write a loop that computes this approximation
of the log2 of a given number N. You can check your code by importing the
math.log function and evaluating the expression round(math.log(N, 2)) (note
that the math.log function returns a floating-point value).

Input:
(int) N

Output:
(int) M

'''

import math

#Introduce the program
print("This program will compute the approximate value of a log2 of a given number.")

#Get user input
N = int(input("Please enter a number: "))

#Calculate using math.log function
P = math.log(N,2)

#Calculate the approximate value
M = 0
while N > 0:
    N = N // 2
    M = M + 1

#Print result and compare with math.log function
print("\nThe approximate value is: %d" % M)
print("Using math.log function: %d" % round(P))

