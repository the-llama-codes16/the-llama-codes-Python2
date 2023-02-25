'''
Python Exercise 3.14
Written by: Iam Rasendi M. Saldua
Date: November 2, 2022

A local biologist needs a program to predict population growth. The inputs
would be the initial number of organisms, the rate of growth (a real number
greater than 0), the number of hours it takes to achieve this rate, and a number
of hours during which the population grows. For example, one might start with a
population of 500 organisms, a growth rate of 2, and a growth period to achieve
this rate of 6 hours. Assuming that none of the organisms die, this would imply
that this population would double in size every 6 hours. Thus, after allowing
6 hours for growth, we would have 1000 organisms, and after 12 hours, we would
have 2000 organisms. Write a program that takes these inputs and displays a prediction
of the total population.

Input:
(int) iniNum - the initial number of organisms
(float) rate - the rate of growth
(float) rateTime - the time in hours needed to achieve the growth rate
(float) growthTime - the time in hours the population is left to grow

Output:
(float) totalPop - the predicted total population after the given time

'''

#Introduce the program
print('''This program predicts the population growth of an organism given the following:
The initial number of organisms (whole number only)
The rate of growth (must be greater than 0)
The time in hours needed to achieve the growth rate
The time in hours the population is left to grow\n''')

#Get user input
iniNum = int(input("Initial number of organisms: "))
rate = float(input("Growth rate: "))
if (rate < 0):
    rate = 1.0
rateTime = float(input("Hours to achieve growth rate: "))
growthTime = float(input("Hours the population is left to grow: "))

#Perform computation
totalPop = iniNum * growthTime * rate / rateTime

#Display results
print('''
Values used:
Initial number of organisms: %d
Growth rate: %.2f
Hours to achieve growth rate: %.2f
Hours the population is left to grow: %.2f

Predicted population after %.2f hours: %.2f''' % (iniNum, rate, rateTime, growthTime, growthTime, totalPop))








