# Programmer: Jason Mueller
# CS 1026A
# Assignment 2: Testing for UPC, Basic, and Poisition Codes.
# This is the function file which contains the proper functions to test incoming strings.

def positional_check(string):
    sum = 0 # defines sum as 0
    string = str(string) # forces the variable passed in to become a string
    test_string = string[:-1] # uses string splicing to take off the last character of the string
    num_to_get = string[len(string)-1] # splices everything off the string except the final character
    for index, value in enumerate(test_string): # using enumerate to access both index and value at once, assigning the first value as index (called index) and second as value.                                       
        sum = ((int(index)+1) * int(value)) + sum # the sum = index + 1 times the value. gives us incredmental numbers x value
    if (sum % 10) == int(num_to_get): # if the sum modulo 10 == final number of the original code, return True.
        return True
    else:
        return False


def basic_check(string):
    sum = 0 
    string = str(string) # same function as above 
    test_string = string[:-1]
    num_to_get = string[len(string)-1]
    for value in test_string: # here we don't need to access the index and value, so enumerate is not needed.
        x = int(value)   # x is assigned as the value we are getting but as an integer, so it can be evaluated
        sum = sum + x
    if (sum % 10) == int(num_to_get): # same as above
        return True
    else:
        return False


def upc_check(string):
    sum = 0
    string = str(string)
    check_digit = 0     # we need a check digit variable since we have to test if it is 0 or above.
    test_string = string[:-1] # same as above
    num_to_get = string[len(string)-1]
    for index, value in enumerate(test_string): # same as position code
        if (int(index) + 1) % 2 != 0: # if the index % 2 does not equal 0, then it is an odd index value
            sum = sum + (3 * int(value))
        elif (int(index) + 1) % 2 == 0: # if the index % 2 does equal 0, then it is an even index value.
            sum = sum + (1 * int(value))
    check_digit = sum % 10 # assign check digit as the sum modulo 10.
    if check_digit == 0: 
        if check_digit == int(num_to_get): # if the digit is 0, then check if its the number we need.
            return True
    elif check_digit > 0: # if greater than 0
        if (10 - check_digit) == int(num_to_get): # check 10 - the check digit, and if its the number we need, return True
            return True
        else:
            return False