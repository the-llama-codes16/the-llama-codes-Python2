"""
Python Exercise 4.19
Written by: Iam Rasendi M. Saldua
Date: December 27, 2022

A bit shift is a procedure whereby the bits in a bit string are moved to the left or
to the right. For example, we can shift the bits in the string 1011 two places to
the left to produce the string 1110. Note that the leftmost two bits are wrapped
around to the right side of the string in this operation.

Define a script, shiftLeft.py, that expects a bit string as an input.
The script shifts the bits in its input one place to the left,
wrapping the leftmost bit to the rightmost position.

"""

# Introduce program
print("""This program accepts a bit string as an input. It shifts
the bits one place to the left, wrapping the leftmost bit to the rightmost position""")

# Get user input
user_string = input("Enter string: ")

# Perform task
length = len(user_string)
first_char = user_string[0]
new_string = ""
for i in range(1, length):
    new_string += user_string[i]
new_string += first_char

# Print result
print("Shifted string: %s\n" % new_string)




    
