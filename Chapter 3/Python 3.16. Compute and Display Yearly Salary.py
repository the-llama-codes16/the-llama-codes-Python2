'''
Python Exercise 3.16
Written by: Iam Rasendi M. Saldua
Date: November 3, 2022

Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years of teaching experience.

For example, a beginning
teacher in the Lexington School District might be paid $30,000 the first year.
For each year of experience after this first year, up to 10 years, the teacher
receives a 2% increase over the preceding value.

Write a program that displays a salary schedule, in tabular format, for teachers
in a school district. The inputs are the starting salary, the percentage increase,
and the number of years in the schedule. Each row in the schedule should contain
the year number and the salary for that year.

Input:
(float) startPay - the starting salary
(float) percentIncrease
(int) totalYears

Output:
a table containing the:
(int) year
(float) equivPay

'''

#Introduce the program
print('''This program displays the salary schedule of a teacher, which increases for each
year of experience.''')

#Get user input
startPay = float(input("Enter starting salary: "))
percentIncrease = float(input("Enter the percentage increase (%): "))
totalYears = int(input("Enter number of years: "))

#Compute and display result
equivPay = startPay
year = 1
print('''
SALARY SCHEDULE
Year     Salary
%3d     %9.2f''' % (year, equivPay))
year += 1

while (year <= totalYears):
    equivPay += equivPay * percentIncrease / 100
    print("%3d     %9.2f" % (year, equivPay))
    year += 1














