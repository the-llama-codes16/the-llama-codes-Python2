'''
Python Exercise 3.6
Written by: Iam Rasendi M. Saldua
Date: October 30, 2022

Using random.randint, selection, and a loop, develop a simple guessing
game. At start-up, the user enters the smallest number and the largest number in the
range. The computer then selects a number from this range. On each pass through the
loop, the user enters a number to attempt to guess the number selected by the computer.
The program responds by saying “You’ve got it,” “Too large, try again,” or “Too
small, try again.” When the user finally guesses the correct number, the program congratulates
him and tells him the total number of guesses.

Input:
(int) lower limit
(int) upper limit
(int) guess

Output:
(int) total number of guesses

'''

import random

#Introduce the program
print("This is a guessing game. You enter the smallest number and the largest number in a range. \
I will pick a random number within the smallest - largest range. You will guess what number I pick.")

#Get user input
while True:
    try:
        smallest = int(input("Enter smallest number: "))
        largest = int(input("Enter largest number: "))
        break
    except:
        print("Invalid input. Please try again.")

#Pick the number
print("\nPicking a number from %d to %d...\n" % (smallest, largest))
number = random.randint(smallest, largest)

#Guessing game
print("I have the number. Guess what it is? ")
count = 1
while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large! Try again.")
            count += 1
        elif guess < number:
            print("Too small! Try again.")
            count += 1
        else:
            print("You've got it! The number is %d!" % number)
            print("You guessed %d times. Congratulations!" % count)
            break
    except:
        print("Wrong! Try again.")
        count += 1
        continue
            
        











