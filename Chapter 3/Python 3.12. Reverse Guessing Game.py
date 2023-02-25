'''
Python Exercise 3.12
Written by: Iam Rasendi M. Saldua
Date: November 1, 2022

Modify the guessing-game program so that the user thinks of a
number that the computer must guess. It must prevent the user from cheating by
entering misleading hints.

Input:
(int) upper
(int) lower
(char) ans

Output:
(int) guess

'''

import random

#Introduce the program
print('''
Pick a range of numbers. Give me the biggest and the smallest in the range, pick a number in that range (including the limits),
and I will guess the number. ''')

#Get user input
lower = int(input("\nEnter the smallest number: "))
upper = int(input("\nEnter the largest number: "))

#Instruct the user
print('''
Pick a number within the range. I will guess that number, and you can enter the following symbols as hints:
< for "Too small"
> for "Too big"
= for "You got it!" \n''')

#Start the guessing game
guess = random.randint(lower, upper)

while True:
    ans = input("Is it %d? " % guess)
    if (ans == "<"):
        #Safeguard against incorrect hints
        if (guess + 1 > upper):
            print("Your hint is invalid and results to a range of %d to %d.\nPlease try again." % (guess + 1, upper))
            continue
        lower = guess + 1
    elif (ans == ">"):
        #Safeguard against incorrect hints
        if (guess - 1 < lower):
            print("Your hint is invalid and results to a range of %d to %d.\nPlease try again." % (lower, guess - 1))
            continue
        upper = guess - 1
    elif (ans == "="):
        print("Yey! So it's %d!" % guess)
        break
    else:
        print('''Invalid input. Please enter
        > for "Too small"
        < for "Too big"
        = for "You got it!"''')
        continue
    #Safeguard against consecutive repetitive guesses
    prevGuess = guess
    guess = random.randint(lower, upper)
    while (guess == prevGuess):
        guess = random.randint(lower, upper)
        

        









