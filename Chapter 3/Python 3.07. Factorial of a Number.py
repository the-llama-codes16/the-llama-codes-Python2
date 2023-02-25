'''
Python Exercise 3.7
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

The factorial of an integer N is the product of the integers between 1 and N, inclusive.
Write a while loop that computes the factorial of a given integer N.

Input:
(int) number

Output:
(int) factRes

'''

#Introduce the program
print("This program computes the factorial of a given integer.")

#Get user input
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except:
        print("Invalid input. Please try again.")

#Get the factorial of user input
factRes = 1
factor = 1
while factor <= number:
    factRes = factRes * factor
    factor += 1


#Print result
print("The factorial of %d is %d." % (number, factRes))
