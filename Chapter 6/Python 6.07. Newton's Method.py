'''
Python Exercise 6.07
Written by: Iam Rasendi M. Saldua
Date: March 25, 2023

Package Newton’s method for approximating square roots (Case Study 3.6) in a
function named newton. This function expects the input number as an argument
and returns the estimate of its square root. The script should also include a main
function that allows the user to compute square roots of inputs until she presses
the enter/return key.
'''
# Define the function
def NewtonMethod(num):
    """This function takes a number and returns its squareroot using Newton's
    method."""
    # Ensure that input is positive
    if (num < 0):
        num = abs(num)
    # Set initial guess
    z = 1
    # This chapter is about recursion, so we do this the recursive way
    def NewtonMethodRecursive(num, z):
        if (num - pow(z,2) > 0.001):
            z = (z + num/z)/2
            NewtonMethodRecursive(num, z)
        else:
            return z
        return z
    # Go!
    return NewtonMethodRecursive(num, z)

# The main function
def main():
    print("""This program allows you to estimate the square root of a number
    using Newton's Method.\n""")
    while True:
        try:
            num = int(input("Enter a number or press the enter key to quit: "))
        except:
            print("Thank you!\n")
            break
        print(NewtonMethod(num))

# The entry point for the main function
if __name__ == "__main__":
    main()

        

            
            
            
            
        
    
