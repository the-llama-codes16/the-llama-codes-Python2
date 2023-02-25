'''
Python Exercise 4.05
Written by: Iam Rasendi M. Saldua
Date: November 20, 2022

A program that decrypts an encrypted message using the Caesar cipher, assuming that
the user knows the key.

Caesar cipher - This encryption strategy replaces each character in the plaintext
with the character that occurs a given distance away in the sequence. For positive
distances, the method wraps around to the beginning of the sequence to locate the
replacement characters for those characters near its end. For example, if the
distance value of a Caesar cipher equals three characters, the string "invaders"
would be encrypted as "lqydghuv".

Input:
(str) encrypted_string
(int) key

Output:
(str) encrypted
'''
import string

#Introduce the program
print("""This program decrypts an encrypted message using the Caesar cipher
under the assumption that the user knows the encryption key.""")

#Get user input
encrypted_string = input("Enter encrypted string: ")
key = int(input("Enter distance key: "))

#Perform decryption
decrypted = ""

for char in encrypted_string:
    #Determine the reference string
    if char.isupper():
        ref_string = string.ascii_uppercase
    elif char.islower():
        ref_string = string.ascii_lowercase
    elif char.isdigit():
        ref_string = string.digits
    else:
        ref_string = string.punctuation + " "

    #Get the location of the character
    loc = ref_string.index(char)

    #Get the decrypted character and attach to decrypted string
    last_index = len(ref_string) - 1
    new_loc = loc - key
    while new_loc < 0:
        new_loc += last_index + 1
    decrypted_char = ref_string[new_loc]
    decrypted += decrypted_char

#Print result
print("\nEncrypted message: %s\nDecrypted message: %s\n" % (encrypted_string, decrypted))
        






