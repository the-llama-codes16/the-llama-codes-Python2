'''
Python Exercise 3.19
Written by: Iam Rasendi M. Saldua
Date: November 13, 2022

In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7,
the player wins $4; otherwise, the player loses $1. Suppose that, to entice the gullible,
a casino tells players that there are lots of ways to win: (1, 6), (2, 5), and so
on. A little mathematical analysis reveals that there are not enough ways to win
to make the game worthwhile; however, because many people’s eyes glaze over
at the first mention of mathematics, your challenge is to write a program that
demonstrates the futility of playing the game. Your program should take as input
the amount of money that the player wants to put into the pot, and play the game
until the pot is empty. At that point, the program should print the number of
rolls it took to break the player, as well as maximum amount of money in the pot.

Input:
(int) initial - the amount of money that the player wants to put into the pot

Output:
(int) rolls - the number of rolls it took to break the player
(int) max_money - the maximum amount of money in the pot

'''

import random

#Introduce the program
print("""This program plays the game of Lucky Sevens until
the pot money runs out. It will then display the number of
rolls it took to break the player, and the maximum amount
of money in the pot.""")

#Get user input
initial = int(input("Enter the amount to put into the pot: "))
max_money = initial
rolls = 0

#Perform computation
while initial > 0:
    roll_results = random.sample([1, 2, 3, 4, 5, 6], 2)
    rolls += 1
    dice_1 = roll_results[0]
    dice_2 = roll_results[1]
    if dice_1 + dice_2 == 7:
        initial += 4
        if initial > max_money:
            max_money == initial
    else:
        initial -= 1
    #print("\nRoll no: %d\nDice rolls: %d %d\nTotal: %d\nCurrent pot money: %d" % (rolls, dice_1, dice_2, dice_1+dice_2, initial))

#Display results
print("Number of rolls: %d\nMaximum amount in the pot: %d" %(rolls, max_money))

    











