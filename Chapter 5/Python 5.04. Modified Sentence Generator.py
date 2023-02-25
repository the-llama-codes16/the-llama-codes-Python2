'''
Python Exercise 5.04
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

Make the following modifications to the original sentence-generator program:
a. The prepositional phrase is optional. (It can appear with a certain
probability.)
b. A conjunction and a second independent clause are optional: The boy took a
drink and the girl played baseball.
c. An adjective is optional: The girl kicked the red ball with a sore foot.
You should add new variables for the sets of adjectives and conjunctions.

'''

import random
import getWords

# Introduce the program
print("""This is a modified version of Exercise 5.03, a sentence self-generator program
that accepts an input of file names containing the list of nouns, verbs, articles,
prepositions, conjunctions, and adjectives to be used. The prepositional phrase,
conjunctions, second independent clauses, and adjectives are optional.""")

# Perform task
# Get user input
print("\nPlease enter the file names to get the words from.")
noun_file = input("Nouns: ")
verb_file = input("Verbs: ")
article_file = input("Articles: ")
preposition_file = input("Prepositions: ")
conjunction_file = input("Conjunctions: ")
adjective_file = input("Adjectives: ")

# Open the files and get all words
nouns = getWords.getWords(noun_file)
verbs = getWords.getWords(verb_file)
articles = getWords.getWords(article_file)
prepositions = getWords.getWords(preposition_file)
conjunctions = getWords.getWords(conjunction_file)
adjectives = getWords.getWords(adjective_file)

# Prepare the set of letters
vowels = "AEIOU"

# Define the functions
def nounPhrase():
    """Returns a randomly generated noun phrase. It may have an adjective, which is subject to probability."""
    article = random.choice(articles)
    noun = random.choice(nouns)
    
    # If num is 1, include an adjective
    num = random.choice([0, 1])
    if num == 1:
        adjective = random.choice(adjectives)
    else:
        adjective = None

    # Correct for "A" and "AN" compatibility, depending on the next word
    if adjective == None:
        if (noun[0] in vowels) and (article == "A"):
            article = "AN"
        elif ((not(noun[0] in vowels)) and (article == "AN")):
            article = "A"
        return (article + " " + noun)
    else:
        if (adjective[0] in vowels) and (article == "A"):
            article = "AN"
        elif ((not(adjective[0] in vowels)) and (article == "AN")):
            article = "A"
        return (article + " " + adjective + " " + noun)

def prepositionalPhrase():
    """Returns a randomly generated prepositional phrase"""
    return (random.choice(prepositions) + " " + nounPhrase())

def verbPhrase():
    """Returns a randomly generated verb phrase. The prepositional phrase is optional."""
    # If num is 1, include a prepositional phrase
    num = random.choice([0, 1])
    if num == 1:
        return (random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase())
    else:
        return (random.choice(verbs) + " " + nounPhrase())

def sentence():
    """Returns a randomly generated sentence. It can have a conjunction and a second
    independent clause, which is subject to probability."""
    # If num is 1, include a conjunction + second independent clause
    num = random.choice([0, 1])
    if num == 1:
        return (nounPhrase() + " " + verbPhrase() + " " + random.choice(conjunctions) + " " + nounPhrase() + " " + verbPhrase())
    else:
        return (nounPhrase() + " " + verbPhrase())

# Continue task
sen_count = int(input("Enter the number of sentences: "))
print("\n")
for i in range(sen_count):
    print(sentence())
    

