# Programmer: Jason Mueller
# CS 1026A
# Assignment 2: Testing for Basic, Posiion and UPC Codes
# This file is the main file whcih will handle all input and output.

import code_check

basic = []          # defining the lists which will contain the codes that the program has run through
positional = []
upc = []
none = []

running = True # boolean for running the program continuously

def checker(string): # function for checking the incoming code
    global ans1     # global variables so I can use the answers (True / False) outside the function
    global ans2
    global ans3
    ans1 = code_check.basic_check(string)    # calling code check file and using the proper checks, passing in string
    ans2 = code_check.positional_check(string)
    ans3 = code_check.upc_check(string)
    
    if ans1 == True:            # determinging which is true or false and adding each to the respective list
        basic.append(string)
    if ans2 == True:
        positional.append(string)
    if ans3 == True:
        upc.append(string)
    if ans1 == False and ans2 == False and ans3 == False:
        none.append(string)


def summary(basic, positional, upc, none):  # function dealing with printing the summary when it is needed
    print("\nSummary")

    basic = str(basic)[1:-1] # this will remove the brackets off of the list after turning the list into a string.
    if basic == "":
        print("\nBasic : None")
    else:
        print("\nBasic : {}".format(basic))

    positional = str(positional)[1:-1]
    if positional == "":
        print("\nPosition : None")
    else:
        print("\nPosition : {}".format(positional))

    upc = str(upc)[1:-1]
    if upc == "":
        print("\nUPC : None")
    else:
        print("\nUPC : {}".format(upc))

    none = str(none)[1:-1]
    if none == "":
        print("\nNone : None")    
    else:
        print("\nNone : {}\n".format(none))

while running:
    code_input = int(input("\nPlease enter code (digits only) (enter 0 to quit) "))
    if code_input == 0:  # if the input is 0 run the summary function
        summary(basic, positional, upc, none)
        break # after running summary break from the loop
    ans = checker(code_input) # running the checker function to test input
    if ans1 == True: # printing the outcome for each input
        print("\n-- code: {} valid Basic code.".format(code_input))
    if ans2 == True:
        print("\n-- code: {} valid Position code.".format(code_input))
    if ans3 == True:
        print("\n-- code: {} valid UPC code.".format(code_input))
    if ans1 == False and ans2 == False and ans3 == False:
        print("\n-- code: {} not Basic, Position or UPC code.".format(code_input))