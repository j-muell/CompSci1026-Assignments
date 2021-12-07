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
        print("The file entered does not exist. It is of type " + fileType + ".")
        choice = input("Do you wish to quit? (Y for yes, N for no): ")

        if choice.lower() == 'n':
            fileName = input("Please enter the new file name for file type " + fileType + ":")
            fileName = fileNameCheck(fileName) # take in the new file name and run it through this function again
            validityChecker(fileName, fileType)
        else:
            updateFailed() # if they want to exit, throw back the updateFailed and make isValid false for the return.
            isValid = False

    return [isValid, fileName]


def updateFailed():
    with open("output.txt", 'w') as file:
        file.write("Update Unsucessful.\n")

def fileAnalysis(updateFile):

    continents = ['Africa', 'Antartica', 'Arctic', 'Asia', 'Europe', 'North_America', 'South_America']
    validInfo = []
    badInfo = []

    updateFile = updateFile.readlines()

    for line in updateFile:
        
        isLineValid = True
        populationCounter = 0
        areaCounter = 0
        continentCounter = 0

        formatted_line = line.replace('\n', "")
        formatted_line = formatted_line.replace(" ", "")
        lineTextList = formatted_line.split(";")

        # if the len of the linelist is greater than 4, there was more than 3 semicolons, therefore it is not valid.
        if len(lineTextList) > 4:
            isLineValid = False

        # next, see if the country name, which is always in the front, is there, and if it only has normal characters and underscores
        for character in lineTextList[0]:
            if character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWKYZ_":
                pass
            else:
                isLineValid = False
                break
        
        # test if country name is capitals

        countryName = lineTextList[0].split("_")

        for character in countryName:
            # try except used to make sure there isn't an error thrown when accessing the first element. If there is then it isn't valid anyway.

            try:
                if character[0] in "ABCDEFGHIJKLMNOPQRSTUVWKYZ": # makes sure first character is capital
                    pass
                else:
                    isLineValid = False
                    break
            except IndexError:
                isLineValid = False
                break

        for index, section in enumerate(lineTextList[1:]): # run through the element of the list but not including the country

            letter = section[0:2] # takes only the letter
            content = section[2:] # takes everything after the letter

            if letter == "P=":
                populationCounter += 1
            elif letter == "A=":
                areaCounter += 1
            elif letter == "C=":
                continentCounter += 1

            if not (letter == "P=" or letter == "A=" or letter == "C="):
                isLineValid = False
                break
            
            elif populationCounter > 1 or areaCounter > 1 or continentCounter > 1:
                isLineValid = False
                break
            
            elif letter == 'C=' and content not in continents:
                isLineValid = False
                break

            elif letter == 'P=' or letter == 'A=':

                for character in content:
                    if character not in '1234567890,':
                        isLineValid = False
                        break

                for overallGroupIndex, numberGroup in enumerate(content.split(',')): # taking the number grouping that exists for the P= and A= types
                    if len(numberGroup) > 3:
                        isLineValid = False
                        break
                    elif overallGroupIndex > 0 and len(numberGroup) < 3:
                        isLineValid = False
                        break
                    
                    
                    # if overallGroupIndex > 0 and len(numberGroup) < 3: # basically, each group after the first number has to have exactly 3 numbers.
                    #     # if the group is over index of 0, which is the first number, and the length of the number group is less than 3, we know it is not valid
                    #     isLineValid = False
                    #     break
                    # if len(numberGroup) > 3: # if we have any group above 3, it is not valid.
                    #     isLineValid = False
                    #     break

        if isLineValid:
            validInfo.append(lineTextList) # basically if it runs through all tests above it is still valid and goes into the valid info list
        else:
            badInfo.append(line)


    # after finishing running through everything
    return [validInfo, badInfo]



def processUpdates(cntryFileName, updateFileName, badUpdateFile):

    cntryFileName = fileNameCheck(cntryFileName)
    updateFileName = fileNameCheck(updateFileName)

    isFileValid, cntryFileName = validityChecker(cntryFileName, "Country")
    if isFileValid: 
        pass
    else:
        tupleReturn = (False, None)
        return tupleReturn

    catObject = CountryCatalogue(cntryFileName)

    isFileValid, updateFileName = validityChecker(updateFileName, 'Update')
    if isFileValid:
        pass
    else:
        tupleReturn = (False, None)
        return tupleReturn

    with open(updateFileName, 'r', encoding='utf-8') as updateFile:
        validInfo, badInfo = fileAnalysis(updateFile)
    
    with open(badUpdateFile, 'w') as badUpdates:
        for piece in badInfo: # for the element of badInfo list, write them indivudally to the badUpdates file 
            badUpdates.write(piece)


    for lineValid in validInfo:
        addCountry = 0
        country = lineValid[0] # linevalid will always have a first element that is the country name
        continent = ""
        population = ""
        area = ""

        

        for section in lineValid[1:]:
            letter = section[0:2] # takes only the letter to update
            content = section[2:] # takes everything after the letter

            if catObject.findCountry(country):
                if letter == 'P=':
                    catObject.setPopulationOfCountry(country, content)
                elif letter == 'A=':
                    catObject.setAreaOfCountry(country, content)
                elif letter == 'C=':
                    catObject.setContinentOfCountry(country, content)

            else: # if country doesn't exist in the country catalogue

                addCountry = 1
                if letter == 'P=':
                    population = content
                if letter == 'A=':
                    area = content
                if letter == 'C=':
                    continent = content

        if addCountry == 1:
            catObject.addCountry(country, population, area, continent)
    
    catObject.saveCountryCatalogue("output.txt")


    tupleReturn = (True, catObject)
    return tupleReturn
