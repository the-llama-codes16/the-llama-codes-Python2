"""
Python Exercise 4.20
Written by: Iam Rasendi M. Saldua
Date: January 12, 2023

Use the strategy of the decimal to binary conversion and the bit shift left
operation defined in Exercise 4.19 to code a new encryption algorithm. The algorithm
should add 1 to each character’s numeric ASCII value, convert it to a bit string,
and shift the bits of this string one place to the left. A single-space character in
the encrypted string separates the resulting bit strings.

Pseudocode
Get input
for each character,
    get the equivalent ASCII value
    add 1 to the ASCII value
    convert it to bits
    concatenate these bits to the resulting string
    add the delimiter character
for each item in the resulting string,
    shift each to the left

"""

# Introduce the program
print("This program encodes your input message.")

# The function to convert decimal to binary
def dec_to_binary(decimal:int):
    binary = ""
    while decimal > 0:
        bit = decimal % 2
        decimal //= 2
        binary = str(bit) + binary
    return binary

# Get user input
message = input("Please enter your message: ")

# Encode
bit_message = ""
for char in message:
    ascii_equiv = ord(char)
    bit_string = dec_to_binary(ascii_equiv + 1)
    bit_message += (bit_string + ' ')
    
# Shifting characters to the left
encoded_message = ""
first_char = bit_message[0]
length = len(bit_message)
for i in range(1, length):
    encoded_message += bit_message[i]
encoded_message += first_char

# Print results
print("Encoded message: %s\n" % encoded_message)


    
