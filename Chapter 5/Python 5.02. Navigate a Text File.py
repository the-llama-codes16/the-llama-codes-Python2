'''
Python Exercise 5.02
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.

'''

# Introduce the program
print("""This program allows you to navigate the lines inside a text file.""")

# Perform task
# Get user input
file_name = input("Please enter text file name: ")
if not(".txt" in file_name):
    file_name = file_name + ".txt"

# Open text file
fhand = open(file_name)

# Put the lines of the text to a list
lines = list()
for line in fhand:
    lines.append(line)
    
# Count the number of lines
length = len(lines)

#Prompt for line number to display
print("The total number of lines is ", length)
line_num = int(input("Please input line number: "))
if line_num == 0:
    print("Program stopping...")
else:
    print("Line number", line_num, "\n", lines[line_num - 1])


