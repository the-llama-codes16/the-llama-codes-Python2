'''
Python Exercise 4.10
Written by: Iam Rasendi M. Saldua
Date: November 27, 2022

Playing with file pathnames.

Structure:
parent:
    current:
        myfile.txt
    sibling:
        myfile.txt
    myfile.txt

'''

#Introduce the program
print("""This program plays with file pathnames and opening the text files in them.
Structure:
parent:
    current:
        myfile.txt
    sibling:
        myfile.txt
    myfile.txt """)

#Vamos!
print("Opening text file in current...")
fhand = open("myfile.txt", "r")
print(fhand)

print("\nOpening text file in sibling...")
fhand = open("..\sibling\myfile.txt", "r")
print(fhand)

print("\nOpening text file in parent...")
fhand = open("..\myfile.txt", "r")
print(fhand)




        






