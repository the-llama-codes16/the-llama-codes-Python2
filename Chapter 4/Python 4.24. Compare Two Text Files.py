"""
Python Exercise 4.24
Written by: Iam Rasendi M. Saldua
Date: February 9, 2023

Write a script that prompts the user for the names
of two text files and compare the contents of the two files
to see if they are the same. If they are, the script
should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file
that differ from eachother. The input loop should read
and compare lines from each file. The loop
should break as soon as a pair of different lines is found.

"""

# Introduce the program
print("This program will ask for 2 file names and compare their contents.")

# Get user input
first_file = input("\nFirst file: ")
second_file = input("Second file: ")
print("\nAre the two files the same? ")

# Perform task
# Append ".txt" if missing
if not(".txt" in first_file):
    first_file = first_file + ".txt"
if not(".txt" in second_file):
    second_file = second_file + ".txt"

# Open files
fhand1 = open(first_file, 'r')
fhand2 = open(second_file, 'r')

# Compare
# Read each file
result = "Yes"
first_file_contents = fhand1.read()
second_file_contents = fhand2.read()

# Split the contents of the file into sentences
first_file_lines = first_file_contents.split("\n")
second_file_lines = second_file_contents.split("\n")

# Use the greater length between the two as upper limit
first_file_len = len(first_file_lines)
second_file_len = len(second_file_lines)
max_len = first_file_len
if second_file_len > max_len:
    max_len = second_file_len

# Compare both lists of sentences 
for i in range(max_len):
    if first_file_lines[i] != second_file_lines[i]:
        result = "No"
        break

print("%s" % result)
if result == "No":
    print("Line %d\n%s: %s\n%s: %s\n" % (i + 1, first_file, first_file_lines[i], second_file, second_file_lines[i]))


    
