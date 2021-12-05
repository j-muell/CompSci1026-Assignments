# Programmer: Jason Mueller
# Date: Dec 6
# CS 1026
# Assignment 4
# File Uses:

from catalogue import CountryCatalogue

def fileNameCheck(fileName):
    # this will check the file to see if .txt is in the name, if its not, add it.
    if ".txt" in fileName:
        return fileName
    else:
        fileName = fileName + ".txt"
        return fileName


def validityChecker(fileName, fileType):
    
    isValid = True
    #flag = True

    try:
        file = fileNameCheck(fileName) # check the filename (useful for recursion after)
        check = open(file, 'r', encoding='utf-8') # try to open and close file. if there is an error, handle it below. If it goes through, it runs the return
        check.close()
    except FileNotFoundError:
        print("The file entered does not exist. It is of type + " + fileType + ".")
        choice = input("Do you wish to quit? (Y for yes, N for no): ")

        if choice.lower() == 'n':
            newFileName = input("Please enter the new file name for file type " + fileType + ":")
            newFileName = fileNameCheck(newFileName) # take in the new file name and run it through this function again
            validityChecker(newFileName, fileType)
        else:
            updateFailed() # if they want to exit, throw back the updateFailed and make isValid false for the return.
            isValid = False

    return [isValid, fileName]


def updateFailed():
    with open("output.txt", 'w') as file:
        file.write("Update Unsucessful.\n")

def fileAnalysis(updateFile):
    pass

def processUpdates(cntryFileName, updateFileName, badUpdateFile):

    cntryFileName = fileNameCheck(cntryFileName)
    updateFileName = fileNameCheck(updateFileName)

    isFileValid, cntryFileName = validityChecker(cntryFileName, "Country")
    if isFileValid: 
        pass
    else:
        tupleReturn = (False, None)
        return tupleReturn

    logObj = CountryCatalogue(cntryFileName)

    isFileValid, updateFileName = validityChecker(updateFileName, 'Update')
    if isFileValid:
        pass
    else:
        tupleReturn = (False, None)
        return tupleReturn

    with open(updateFileName, 'r', encoding='utf-8') as updateFile:
        pass



