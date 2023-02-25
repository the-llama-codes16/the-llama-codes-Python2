'''
Python Exercise 4.11
Written by: Iam Rasendi M. Saldua
Date: December 5, 2022

Write a code segment that opens a file named myfile.txt for input and prints the
number of lines in the file.

'''

#Introduce the program
print("This program opens a file and prints the number of lines in that file.")

#Perform task
fhand = open("myfile.txt", "r")
lines = 0
for line in fhand:
    lines += 1
fhand.close()

#Print result
print("\nNumber of lines: %d\n" % lines)

        






