"""
Python Exercise 4.25
Written by: Iam Rasendi M. Saldua
Date: February 9, 2023

The Payroll Department keeps a list of employee information for each pay period
in a text file. The format of each line of the file is the following:
<last name> <hourly wage> <hours worked>
Write a program that inputs a filename from the user and prints to the terminal a
report of the wages paid to the employees for the given period. The report should
be in tabular format with the appropriate header. Each line should contain an
employee’s name, the hours worked, and the wages paid for that period.

"""

# Introduce the program
print("""This program prompts for the name of a payroll file and prints
the payroll table in a format.""")

# Get user input
payroll_file = input("Enter payroll file name: ")
if not(".txt" in payroll_file):
    payroll_file = payroll_file + ".txt"

# Open and read file
fhand = open(payroll_file, 'r')

# Print table
print("%10s  %s  %s" % ("Last Name", "Hours Worked", "Wages Paid"))
for line in fhand:
    clean_data = (line.rstrip()).split()
    name = clean_data[0]
    hourly_wage = float(clean_data[1])
    hours_worked = float(clean_data[2])
    wages_paid = hourly_wage * hours_worked
    print("%10s  %8.2f     %10.2f" % (name, hours_worked, wages_paid))
