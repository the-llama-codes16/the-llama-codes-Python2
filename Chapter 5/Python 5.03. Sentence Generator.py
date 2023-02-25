'''
Python Exercise 5.03
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

import random
import getWords

# Introduce the program
print("""This is a sentence self-generator program that accepts an input of
file names containing the list of nouns, verbs, articles,
and prepositions to be used.""")

# Perform task
# Get user input
print("Please enter the file names to get the words from.")
noun_file = input("Nouns: ")
verb_file = input("Verbs: ")
article_file = input("Articles: ")
preposition_file = input("Prepositions: ")

# Open the files and get all words
nouns = getWords.getWords(noun_file)
verbs = getWords.getWords(verb_file)
articles = getWords.getWords(article_file)
prepositions = getWords.getWords(preposition_file)

# Prepare the set of letters
vowels = "AEIOU"

# Define the functions
def nounPhrase():
    """Returns a randomly generated noun phrase"""
    noun = random.choice(nouns)
    article = random.choice(articles)

    # Correct for "A" and "AN" compatibility, depending on the next word
    if noun[0] in vowels:
        if article == "A":
            article = "AN"
    else:
        if article == "AN":
            article = "A"
    return (article + " " + noun)

def prepositionalPhrase():
    """Returns a randomly generated prepositional phrase"""
    return (random.choice(prepositions) + " " + nounPhrase())

def verbPhrase():
    """Returns a randomly generated verb phrase"""
    return (random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase())

def sentence():
    """Returns a randomly generated sentence"""
    return (nounPhrase() + " " + verbPhrase())

# Continue task
sen_count = int(input("Enter the number of sentences: "))
for i in range(sen_count):
    print(sentence())
    

