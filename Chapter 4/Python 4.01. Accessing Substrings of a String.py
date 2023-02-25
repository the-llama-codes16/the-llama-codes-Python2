'''
Python Exercise 4.01
Written by: Iam Rasendi M. Saldua
Date: November 18, 2022

In the string "myprogram.exe", Write the
expressions that perform the following tasks:
a. Extract the substring "gram" from data.
b. Truncate the extension ".exe" from data.
c. Extract the character at the middle position from data.


'''

#Introduce the program
print("In the string \"myprogram.exe\", substrings will be extracted.")

#Perform task
sample_string = "myprogram.exe"
print("\na. Extract the substring \"gram\" from the string.")
print("%s" % (sample_string[5:9]))
print("b. Truncate the extension \".exe\" from the string.")
print("%s" % (sample_string[:-4]))
print("c. Extract the character at the middle position from the string.")
mid_index = len(sample_string) // 2
print("%s" % (sample_string[mid_index]))










