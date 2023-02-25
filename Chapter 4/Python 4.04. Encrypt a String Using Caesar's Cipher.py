'''
Python Exercise 4.04
Written by: Iam Rasendi M. Saldua
Date: November 20, 2022

A program that encrypts a message using the Caesar cipher.

Caesar cipher - This encryption strategy replaces each character in the plaintext
with the character that occurs a given distance away in the sequence. For positive
distances, the method wraps around to the beginning of the sequence to locate the
replacement characters for those characters near its end. For example, if the
distance value of a Caesar cipher equals three characters, the string "invaders"
would be encrypted as "lqydghuv".

Input:
(str) raw_string
(int) key

Output:
(str) encrypted
'''
import string

#Introduce the program
print("This program encrypts a message using the Caesar cipher.")

#Get user input
raw_string = input("Enter your message: ")
key = int(input("Enter the distance count: "))

#Encrypt the message
encrypted = ""

for char in raw_string:
    #Determine the reference string
    if char.isupper():
        ref_string = string.ascii_uppercase
    elif char.islower():
        ref_string = string.ascii_lowercase
    elif char.isdigit():
        ref_string = string.digits
    else:
        ref_string = string.punctuation + " "
        
    #Determine the location of the character in the ref_string
    loc = ref_string.index(char)

    #Determine the encrypted character and attach to encrypted string
    last_index = len(ref_string) - 1
    new_loc = loc + key
    while new_loc > last_index:
        new_loc -= (last_index + 1)
    encrypted_char = ref_string[new_loc]
    encrypted += encrypted_char
    
#Print results
print("\nOriginal message: %s\nEncrypted message: %s\n" % (raw_string, encrypted))







