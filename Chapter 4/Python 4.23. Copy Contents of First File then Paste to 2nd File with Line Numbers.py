"""
Python Exercise 4.23
Written by: Iam Rasendi M. Saldua
Date: February 6, 2023

Write a script that creates a program listing from a
source program. This script should prompt the user for the names of two files.
The input filename could be the name of the script itself,
but be careful to use a different output filename!
The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
1> This is the first line of text.

"""

# Introduce the program
print("""This program asks you for 2 file names. It will then copy the
contents of the first file to write to the 2nd file, with the addition
of line numbers right-justified in 4 columns.
Example:
1> This is the first line of text.""")

# Get user input
first_file = input("\nFirst file: ")
second_file = input("Second file: ")

# Perform Task
# Append ".txt" if missing
if not(".txt" in first_file):
    first_file = first_file + ".txt"
if not(".txt" in second_file):
    second_file = second_file + ".txt"
    
# Open files
fhand1 = open(first_file, 'r')
fhand2 = open(second_file, 'w')

# Read first file contents and write to second file
line_num = 1
to_write = ""
for line in fhand1:
    fhand2.write("%4d> %s" % (line_num, line))
    line_num = line_num + 1

# Finish everything
fhand1.close()
fhand2.close()
print("\nReading and writing complete. Please check the files.\n")



        
        
    


    
