'''
Python Exercise 3.18
Written by: Iam Rasendi M. Saldua
Date: November 13, 2022

Write a program that receives a series of numbers from the user and allows the
user to press the enter key to indicate that he or she is finished providing inputs.
After the user presses the enter key, the program should print the sum of the
numbers and their average.

Input:
(int) num - series of numbers

Output:
(int) num_sum
(float) average

'''

#Introduce the program
print("""This program allows you to enter a series of numbers. You must
press the enter key to indicate that you are finished. This program will
provide the sum and average of the numbers.""")

#Get user input and perform computation
count = 0
num_sum = 0

print("Enter a series of numbers, press Enter key to end: ")

while True:
    num = input(">> ")
    if (num == ""):
        average = num_sum / count
        break
    num = int(num)
    count += 1
    num_sum += num

print("Sum: %d \nAverage: %.2f" % (num_sum, average)) 

    











