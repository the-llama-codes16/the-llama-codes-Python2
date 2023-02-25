"""
Python Exercise 4.13
Written by: Iam Rasendi M. Saldua
Date: December 5, 2022

Assume that a file contains integers separated by newlines. Write a code segment
that opens the file and prints the average value of the integers.

"""

#Introduce the program
print("""This program opens a file that contains integers separated by newlines.
This program will return the average value of the integers.""")

#Perform task
fhand = open("integerFile.txt", "r")
totalSum = 0
count = 0
for line in fhand:
    numbers = line.split()
    for number in numbers:
        totalSum += int(number)
        count += 1
fhand.close()

#Display result
print("Average: %.2f" % (totalSum / count))
        
        




