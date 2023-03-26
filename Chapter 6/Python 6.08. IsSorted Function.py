'''
Python Exercise 6.08
Written by: Iam Rasendi M. Saldua
Date: March 25, 2023

A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.

'''

# Introduce the program
print("""This program checks if a list of numbers is sorted in ascending order.""")

# Define the function
def isSorted(num_list: list):
    length = len(num_list)
    for i in range(length - 1):
        if (num_list[i] > num_list[i+1]):
            return False
    return True

# Show the function at work
sample1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
sample2 = [2, 4, 5, 1, 42, 0]
sample3 = [12, 16, 19, 22, 27]
print("\nThe inputs:\n", sample1, "\n", sample2, "\n", sample3, "\n")
print("sample1 is sorted:", isSorted(sample1))
print("sample2 is sorted:", isSorted(sample2))
print("sample3 is sorted:", isSorted(sample3))


        

            
            
            
            
        
    
