'''
Python Exercise 5.07
Written by: Iam Rasendi M. Saldua
Date: February 26, 2023

Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.

'''
import string

# Introduce the program
print("""This program will ask for the name of a text file and print out
the unique words in the file in alphabetical order.""")

# Perform task
# Get user input
file_name = input("\nEnter file name: ")
if not(".txt" in file_name):
    file_name = file_name + ".txt"
fhand = open(file_name)
unique_words = list()

# List all unique words, remove digits and punctuations
to_remove = string.punctuation + string.digits
for line in fhand:
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.translate(word.maketrans("","",to_remove))
        if (word in unique_words) or (word == ""):
            continue
        unique_words.append(word)
fhand.close()

# Sort
unique_words.sort()

# Display results
print("\nUnique words:")
for word in unique_words:
    print(word)
    
