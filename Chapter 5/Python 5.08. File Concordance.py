'''
Python Exercise 5.08
Written by: Iam Rasendi M. Saldua
Date: February 26, 2023

A file concordance tracks the unique words in a file and their frequencies. Write
a program that displays a concordance for a file. The program should output the
unique words and their frequencies in alphabetical order.

'''
import string

# Introduce the program
print("""This program asks for a file name and displays the frequencies of
all unique words in the file.""")

# Perform task
# Get user input
file_name = input("\nEnter file name: ")
if not(".txt" in file_name):
    file_name = file_name + ".txt"
fhand = open(file_name)
word_freq = dict()

# List all unique words and their frequencies, remove digits and punctuations
to_remove = string.punctuation + string.digits
for line in fhand:
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.translate(word.maketrans("","",to_remove))
        if word == "":
            continue
        current_count = word_freq.get(word, 0)
        current_count = current_count + 1
        word_freq[word] = current_count
fhand.close()

# Organize and print results
org_data = list()
for word,freq in word_freq.items():
    org_data.append((word,freq))
org_data.sort()
for word,freq in org_data:
    print(word, "-", freq)
