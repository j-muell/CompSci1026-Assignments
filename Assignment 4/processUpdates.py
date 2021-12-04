# Programmer: Jason Mueller
# Date: Dec 6
# CS 1026
# Assignment 4
# File Uses:

from catalogue import CountryCatalogue

def processUpdates(cntryFileName):
    runCat = CountryCatalogue(cntryFileName)
    print(runCat.printCountryCatalogue())

processUpdates('testWriting.txt')