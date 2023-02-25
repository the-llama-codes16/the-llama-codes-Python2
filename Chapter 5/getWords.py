'''
Python Exercise 5.03 - getWords.py
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

Modify the sentence-generator program of Case Study 5.3 so that it inputs its
vocabulary from a set of text files at startup. The filenames are nouns.txt, verbs.
txt, articles.txt, and prepositions.txt. (Hint: Define a single new function,
getWords. This function should expect a filename as an argument. The function
should open an input file with this name, define a temporary list, read words
from the file, and add them to the list. The function should then convert the list
to a tuple and return this tuple. Call the function with an actual filename to initialize
each of the four variables for the vocabulary.)

'''

def getWords(file_name:str):
    """Opens a file, puts the words into a list, then returns that list"""
    if not(".txt" in file_name):
        file_name = file_name + ".txt"
    fhand = open(file_name)
    
    # Create a list to put the words in
    word_list = list()
    
    # Each word occupies one line
    for line in fhand:
        word_list.append(line.strip())
    return (tuple(word_list))


