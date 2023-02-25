'''
Python Exercise 3.17
Written by: Iam Rasendi M. Saldua
Date: November 3, 2022

The greatest common divisor of two positive integers, A and B, is the largest
number that can be evenly divided into both of them. Euclid’s algorithm can be
used to find the greatest common divisor (GCD) of two positive integers. You
can use this algorithm in the following manner:
a. Compute the remainder of dividing the larger number by the smaller
number.
b. Replace the larger number with the smaller number and the smaller number
with the remainder.
c. Repeat this process until the smaller number is zero.

The larger number at this point is the GCD of A and B. Write a program that lets
the user enter two integers and then prints each step in the process of using the
Euclidean algorithm to find their GCD.

Input:
(int) A and B

Output:
(int) GCD

'''

#Introduce the program
print('''This program calculates the GCD of two given numbers using
Euclid's algorithm.\n''')

#Get user input
A = int(input("Enter first number: "))
B = int(input("Enter 2nd number: "))

#Store the smaller number in A
if (A > B):
    temp = A
    A = B
    B = temp

#Perform computation
while (A != 0):
    remainder = B % A
    B = A
    A = remainder
GCD = B

#Display result
print("\nThe GCD is %d.\n" % (GCD))

    











