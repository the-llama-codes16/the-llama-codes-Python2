'''
Python Exercise 3.5
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

The variables x and y refer to numbers. Write a code segment that prompts the user for
an arithmetic operator and prints the value obtained by applying that operator to x and y.

Input:
(int) digitA
(int) digitB
(string) operator

Output:
(int) result when the operator is applied to the 2 digits

'''

#Introduce the program
print("This program takes 2 digits and an operator from the user and returns the result of the operation applied to the 2 numbers.")

#Get user input
digitA = int(input("Enter first digit: "))
digitB = int(input("Enter second digit: "))
operator = input("Enter operator (+, -, /, or *): ")

#Process the inputs
if operator == "+":
    result = digitA + digitB
    print("Answer: %d" % result)
elif operator == "-":
    result = digitA - digitB
    print("Answer: %d" % result)
elif operator == "/":
    result = digitA / digitB
    print("Answer: %d" % result)
elif operator == "*":
    result = digitA * digitB
    print("Answer: %d" % result)
else:
    print("Operator invalid. Please try again.")

