'''
Python Exercise 5.01 - Stats.py
Written by: Iam Rasendi M. Saldua
Date: February 25, 2023

A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list.

'''
# Defining the functions
# Median
def median(num_list:list):
    """ Computes the median of a list of numbers.
        parameter: list of numbers
        returns: int/float """ 
    length = len(num_list)
    if length == 0:
        return 0
    else:
        num_list.sort()
        if not(length % 2 == 0):
            a = (length // 2 + 1) - 1
            return num_list[a]
        else:
            a = (length // 2) - 1
            b = a + 1
            c = num_list[a] + num_list[b]
            return (c / 2)

# Mode
def mode(num_list:list):
    """ Computes the mode of a list of numbers.
        parameter: list of numbers
        returns: int/float """
    if len(num_list) == 0:
        return 0
    else:
        counter = dict()
        for digit in num_list:
            value = counter.get(digit, None)
            if value == None:
                # The digit is not yet in the dictionary
                counter[digit] = 1
            else:
                # The digit is already in the dictionary
                value = value + 1
                counter[digit] = value
        pairs = list()
        for key, value in counter.items():
            pairs.append((value, key))
        pairs.sort(reverse = True)
        return pairs[0][1]


# Mean
def mean(num_list:list):
    """ Computes the mean of a list of numbers.
        parameter: list of numbers
        returns: float/int """
    length = len(num_list)
    if length == 0:
        return 0
    else:
        total_sum = 0
        for digit in num_list:
            total_sum = total_sum + digit
        return ((total_sum * 1.0) / length)


def main():
    """ Tests the three statistical functions in Stats Module.py:
        Median, Mode, Mean """
    test_list = [12, 16, 19, 11, 5, 19, 10, 25, 19]
    print("The test list is", test_list)
    median_res = median(test_list)
    mode_res = mode(test_list)
    mean_res = mean(test_list)
    print("The results are:\nMedian: ", median_res,"\nMode: ", mode_res, "\nMean: ", mean_res)


# The entry point for program execution
if __name__ == "__main__":
    main()






