'''
Python Exercise 6.06
Written by: Iam Rasendi M. Saldua
Date: March 19, 2023

Modify the summation function presented in Section 6.2 so that it includes default
arguments for a step value and a function. The step value is used to move to the
next value in the range. The function is applied to each number visited, and the
function’s returned value is added to the running total. The default step value is 1,
and the default function is lambda that returns its argument (essentially an identity
function). An example call of this function is summation(l, 100, 2, math.sqrt),
which returns the sum of the square roots of every other number between 1 and
100. The function can also be called as usual, with just the bounds of the range.
'''

# Introduce the program
print("""This program creates a modified summation function.""")

# Define the function
def summation(lower:int, upper:int, step = 1, func = lambda x: x):
    """Returns the sum of the numbers from lower through upper, with
    optional step and function arguments"""
    if lower > upper:
        return 0
    else:
        result = func(lower) + summation(lower + step, upper, step, func)
        return result


# Call the function with all arguments provided
def main():
    print("""\nCalling the summation function with the following input:
    lower = 1
    upper = 10
    step = 2
    func = lambda x: pow(x, 2)
    RESULT: """, end="")
    print(summation(1, 10, 2, lambda x: pow(x,2)))


# Entry point for main function
if __name__ == "__main__":
    main()

