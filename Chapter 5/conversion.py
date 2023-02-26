'''
Python Exercise 5.05 - conversion
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

In Chapter 4, we developed an algorithm for converting from binary to decimal.
You can generalize this algorithm to work for a representation in any base.
Instead of using a power of 2, this time you use a power of the base. Also, you use
digits greater than 9, such as A . . . F, when they occur. Define a function named
repToDecimal that expects two arguments, a string, and an integer. The second
argument should be the base. For example, repToDecimal("10", 8) returns
8, whereas repToDecimal("10", 16) returns 16. The function should use a
lookup table to find the value of any digit. Make sure that this table (it is actually
a dictionary) is initialized before the function is defined. For its keys, use the 10
decimal digits (all strings) and the letters A . . . F (all uppercase). The value stored
with each key should be the integer that the digit represents. (The letter 'A' associates
with the integer value 10, and so on.) The main loop of the function should
convert each digit to uppercase, look up its value in the table, and use this value
in the computation. Include a main function that tests the conversion function
with numbers in several bases.


Python Exercise 5.06 - conversion
Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.

'''


# Initialize the lookup tables
lookup = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
lookup_rev = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

# Define the conversion functions
def repToDec(to_conv:str, base:int):
    decimal = 0
    highest_exp = len(to_conv) - 1
    current_exp = highest_exp
    for char in to_conv:
        value = lookup[char]
        decimal = decimal + ((base ** current_exp) * value)
        current_exp = current_exp - 1
    return decimal

def decToRep(to_conv:int, base:int):
    converted = ""
    while to_conv > 0:
        remainder = to_conv % base
        # Use the lookup_rev table
        to_join = lookup_rev[remainder]
        converted = to_join + converted
        to_conv = to_conv // base
    return converted
        
# Define the main function which includes testing
def main():
    # Introduce the program
    print("""This program allows conversion of binary, octal, and hexadecimal
numbers to decimal, and vice versa.""")
    test_bit = "101001111000"
    test_octal = "5170"
    test_hex = "A78"
    print("\n======= Testing repToDec =======")
    print("Test strings:\nBinary: " + test_bit + "\nOctal: " + test_octal + "\nHexadecimal: " + test_hex)
    print("\nConverting all strings to decimal...\n")
    print("Binary to Decimal:", repToDec(test_bit, 2))
    print("Octal to Decimal:", repToDec(test_octal, 8))
    print("Hexadecimal to Decimal:", repToDec(test_hex, 16))
    test_dec = 2680
    print("\n\n======= Testing decToRep =======")
    print("Test decimal:", test_dec)
    print("\nConverting test decimal to binary, octal, and hexadecimal...\n")
    print("Decimal to Binary:", decToRep(test_dec, 2))
    print("Decimal to Octal:", decToRep(test_dec, 8))
    print("Decimal to Hexadecimal:", decToRep(test_dec, 16))
    print("\n")

# Entry point to the program
if __name__ == "__main__":
    main()
    

