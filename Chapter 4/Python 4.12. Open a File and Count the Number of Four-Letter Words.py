'''
Python Exercise 4.12
Written by: Iam Rasendi M. Saldua
Date: December 5, 2022

Write a code segment that opens a file for input and prints the number of
four-letter words in the file.

'''

#Introduce the program
print("This program opens a file and prints the number of four-letter words in that file")

#Perform task
fhand = open("myfile.txt", "r")
fourLetter = 0
for line in fhand:
    words = line.split()
    for word in words:
        if len(word) == 4:
            fourLetter += 1

fhand.close()

#Display results
print("Number of four-letter words: %d" % fourLetter)






