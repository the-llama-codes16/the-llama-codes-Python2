'''
Python Exercise 3.1
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

Request
Write a program that computes an investment report.

Analysis
The inputs to this program are the following:
•• An initial amount to be invested (a floating-point number)
•• A period of years (an integer)
•• An interest rate (a percentage expressed as an integer)

The program uses a simplified form of compound interest, in which the interest is
computed once each year and added to the total amount invested. The output of
the program is a report in tabular form that shows, for each year in the term of the
investment, the year number, the initial balance in the account for that year, the interest
earned for that year, and the ending balance for that year. The columns of the
table are suitably labeled with a header in the first row. Following the output of the
table, the program prints the total amount of the investment balance and the total
amount of interest earned for the period.

Design
The four principal parts of the program perform the following tasks:
1. Receive the user’s inputs and initialize data.
2. Display the table’s header.
3. Compute the results for each year, and display them as a row in the table.
4. Display the totals.

The third part of the program, which computes and displays the results, is a loop.

'''

#Introduce the program
print("This program displays an investment report given the initial investment amount\
,the investment period, and the interest rate.")

#Get user input
startAmount = float(input("\n\nInitial amount: "))
rate = float(input("Interest rate in percent: ")) / 100
period = int(input("Number of years: "))

#Print header
print("\nYear  Starting balance  Interest  Ending balance")

#Compute and print
for year in range(1, period + 1):
    interest = startAmount * rate
    endAmount = startAmount + interest
    print("%4d  %16.2f  %8.2f  %14.2f" % (year, startAmount, interest, endAmount))
    startAmount = endAmount










