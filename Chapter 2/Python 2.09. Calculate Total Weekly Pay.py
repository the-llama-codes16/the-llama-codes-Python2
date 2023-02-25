'''
Python Exercise 2.9
Written by: Iam Rasendi M. Saldua
Date: October 16, 2022

An employee’s total weekly pay equals the hourly wage multiplied by the total 
number of regular hours plus any overtime pay. Overtime pay equals the total 
overtime hours multiplied by 1.5 times the hourly wage. Write a program that 
takes as inputs the hourly wage, total regular hours, and total overtime hours and 
displays an employee’s total weekly pay.

Input:
(float) hourWage
(float) totalRegHours
(float) totalOvertimeHours

Output:
(float) totalWeeklyPay

'''

import math

print("""This program calculates the total weekly pay given the following:
Hourly Wage
Total Regular Hours
Total Overtime Hours""")

#User Input
hourWage = float(input("\nEnter hourly wage: "))
totalRegHours = float(input("Enter total regular hours: "))
totalOvertimeHours = float(input("Enter total overtime hours: "))

#Calculate weekly pay
regularPay = hourWage * totalRegHours
overtimePay = hourWage * 1.5 * totalOvertimeHours
totalWeeklyPay = regularPay + overtimePay

#Display Results
print("\nTotal weekly pay: " + str(round(totalWeeklyPay, 2)))
