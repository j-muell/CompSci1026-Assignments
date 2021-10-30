# Programmer: Jason Mueller
# Date: September 23rd 2021
# Class: CS 1026A

flag = 1 # variable which will be used to continue running the program.

while flag == 1:

    off_peak = float(input("Enter kwh during Off Peak period: "))
    if off_peak == 0.0 or off_peak == 0: # checking if the value entered is either 0.0 or 0. If it is, break out of the loop.
        break
    on_peak = float(input("Enter kwh during On Peak period: "))
    mid_peak = float(input("Enter kwh during Mid Peak period: "))
    senior = input("Is owner senior (y,n):")
    
    off_peak_kwh = off_peak # defining new variables for further clarity.
    on_peak_kwh = on_peak 
    mid_peak_kwh = mid_peak

    total_kwh = off_peak_kwh + on_peak_kwh + mid_peak_kwh # total kwh.

    off_peak_cost = 0.085 * off_peak # finding the exact cost for each time slot.
    on_peak_cost = 0.176 * on_peak
    mid_peak_cost = 0.119 * mid_peak

    total_cost = off_peak_cost + on_peak_cost + mid_peak_cost # finding total cost and definting it

    usage_discount = 0 # variable to be used in order to detect if one discount has already been used.

    if total_kwh < 400:
        total_cost = total_cost - (total_cost * 0.04) # removing 4% from the bill prior to tax.
        usage_discount += 1 # add 1 to our usage_discount to know we have used a discount.

    
    if usage_discount == 0: # test if a discount has already been used.
        if on_peak_kwh < 150:
            on_peak_cost = on_peak_cost - (on_peak_cost * 0.05) # removing 5% from specifically on peak cost prior to tax.
            total_cost = off_peak_cost + on_peak_cost + mid_peak_cost # defining our new total cost.

    
    if senior == "y" or senior == "Y": # checking if user is a senior.
        total_cost = total_cost - (total_cost * 0.11) # removing the 11%
    
    final_cost = total_cost + (total_cost * 0.13) # adding the 13% tax

    print("\nElectricity cost: ${0:.2f}".format(final_cost)) # printing the ending cost with formatting of 2 dedimal places.