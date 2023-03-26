'''
Python Exercise 6.05
Written by: Iam Rasendi M. Saldua
Date: March 19, 2023

Write the code for a reducing that creates a single string from a list of strings named
words.
'''
import functools

# Introduce the program
print("""\nThis program uses the reducing function to create a single string
from a list of strings.\n""")

# Perform task
words = ["Can", "I", "go", "where", "you", "go?"]
print("The list:", words, "\n\nUsing reducing function...\n")
result_string = functools.reduce(lambda word_1, word_2: word_1 + " " + word_2, words)
print("The resulting string:", result_string)



