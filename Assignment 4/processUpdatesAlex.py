"""
Alexander Belan-Hudson
Student Number:   [251206726]
Course Code:      [1026A]
Section Number:   [001]
Project:          Assignment 4 - Country Classes
File:             processUpdates.py
Script houses the functions that can manipulate files
"""

# ****************************************************   Script   *****************************************************

import catalogue as log


def nameChecker(name):
    """
    Function simply checks the name of of the file to see if .txt is on the end or not
    :param name:
    :return: a potentially modified name
    """
    if ".txt" in name:
        return name
    else:
        name = name + ".txt"
        return name


def fileChecker(fileName, fileType):
    """
    Function tests a file for its existence, if not prompts user for new file name or whether to leave program
    :param fileName:    name of the file
    :param fileType:    type of file (update vs. initial data)
    :return: list contains the validity of the file and the file's name
    """

    loopFlag = True  # initializing boolean values
    fileValidity = True

    # loop repeats until flag condition is not met
    while loopFlag:
        # try-catch block tests
        try:
            # re-checking the name for .txt on end
            fileName = nameChecker(fileName)
            fileObj = open(fileName, "r", encoding="utf-8")
            fileObj.close()     # test opening and closing the file
            loopFlag = False            # setting the loop sentinel to False
        except IOError:
            # instance when file doesn't exist, prompt user
            message = fileType + " file name does not exist. Do you want to quit? (“Y” (yes) or “N” (no)): "
            query = input(message)

            if query == "N":
                message = "Enter the new " + fileType + " file name: "
                newFileName = input(message)
                fileName = nameChecker(newFileName)
            else:
                unsuccessfulUpdate()    # calling upon external function for an unsuccessful update
                fileValidity = False
                loopFlag = False        # setting boolean values to false

    # returning associated list
    return [fileValidity, fileName]


def unsuccessfulUpdate():
    """
    Function simply writes to a file when an unsuccessful update occurs
    :return:
    """
    f3 = open("output.txt", "w")
    f3.write("Update Unsuccessful\n")
    f3.close()


def updateFileAnalyzer(file):
    """
    Functions breaks down each line of the update file to identify which lines are valid
    :param file: name of the update file
    :return: list that contains two sub-lists of valid data and invalid data
    """

    # following list contains only the valid continents
    continentList = ("Africa", "Antarctica", "Arctic", "Asia", "Europe", "North_America", "South_America")
    goodFileInfo = []
    badFileInfo = []  # empty lists housing the valid and invalid update data respectively

    # for loop reads in each line of update file and determines the validity of its fields
    for line in file.readlines():

        lineValidity = True
        continentCount = 0
        popCount = 0  # redefining variables for each line every time the loop iterates
        areaCount = 0
        strand = line.replace("\n", "")
        strand = strand.replace(" ", "")
        lineText = strand.split(";")

        # identifying whether the field count for each does not exceed four (alt. no more than 3 semicolons)
        if len(lineText) > 4:
            lineValidity = False

        # identifying whether the country name only contains latin characters and underscores
        for char in lineText[0]:
            if char not in "abcdefghijklmnopqrstuvwxwyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
                lineValidity = False
                break

        # identifying whether each name inside country (even those separated by commas) start with capital letters
        sepCountryName = lineText[0].split("_")

        for name in sepCountryName:
            # try-catch block examines the index of country name for the instance that it doesnt exist
            try:
                if name[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    lineValidity = False
                    break
            except IndexError:
                lineValidity = False
                break

        # loop traverses the entire text of each line
        for index, component in enumerate(lineText):
            if index > 0:  # dealing with only the update fields

                compType = component[0:2]  # substring represents the type for the update
                compInfo = component[2:]  # substring represents all characters after initial type

                # depending on type of update, increments an associated counter
                if compType == "P=":
                    popCount += 1
                elif compType == "A=":
                    areaCount += 1
                elif compType == "C=":
                    continentCount += 1

                if not (compType == "P=" or compType == "A=" or compType == "C="):
                    # identifying whether each update field begins with valid characters
                    lineValidity = False
                    break

                elif popCount > 1 or areaCount > 1 or continentCount > 1:
                    # identifying whether the update fields don't repeat
                    lineValidity = False
                    break

                elif compType == "C=" and compInfo not in continentList:
                    # identifying whether the continent update is valid, based on predefined list
                    lineValidity = False
                    break

                elif compType == "P=" or compType == "A=":
                    # instance of update type being population or area

                    for char in compInfo:  # loop traverses through characters of each field
                        if char not in "1234567890,":  # instance that the character is not valid
                            lineValidity = False
                            break

                    # for loop identifies whether any field number is accurately composed in groups of three (e.g. *,***,***)
                    for group, numGrouping in enumerate(compInfo.split(",")):
                        if len(numGrouping) > 3:  # making sure no grouping exceeds three characters
                            lineValidity = False
                            break
                        elif group > 0 and len(
                                numGrouping) < 3:  # any grouping after the first must be three characters exactly
                            lineValidity = False
                            break

        # depending on whether the update is valid or not, the line will be added to an associated list
        if lineValidity:
            goodFileInfo.append(lineText)  # appending the edited line if its valid
        else:
            badFileInfo.append(line)  # appending the unedited line if it's invalid

    # returning a list that contains two sub-lists of valid data and invalid data respectively
    return [goodFileInfo, badFileInfo]


def processUpdates(cntryFileName, updateFileName, badUpdateFile="badupdates.txt"):
    """
    Function takes all the files and performs the appropriate analysis/modifications to housed information
    :param cntryFileName:   name for file Country
    :param updateFileName:  name for file Updates
    :param badUpdateFile:   name for file containing invalid Updates
    :return: tuple containing the success of the program and potential catalogue object
    """

    # checking the name of the files to see if .txt is on the end
    cntryFileName = nameChecker(cntryFileName)
    updateFileName = nameChecker(updateFileName)

    # identifying whether the country file exits. If not, returns a specific tuple
    fileValidity, cntryFileName = fileChecker(cntryFileName, "Country")
    if not fileValidity:
        tupleOut = (False, None)
        return tupleOut  # returning a tuple containing a boolean, and an empty index

    logObj = log.CountryCatalogue(cntryFileName)  # creating a catalogue object using the valid country file

    # identifying whether the update file exits. If not, returns a specific tuple
    fileValidity, updateFileName = fileChecker(updateFileName, "Update")
    if not fileValidity:
        tupleOut = (False, None)
        return tupleOut  # returning a tuple containing a boolean, and an empty index

    f1 = open(updateFileName, "r", encoding="utf-8")
    # calling upon a function to analyze the update file for valid and invalid updates
    goodFileInfo, badFileInfo = updateFileAnalyzer(f1)
    f1.close()

    f2 = open(badUpdateFile, "w")
    for segment in badFileInfo:  # loop writes to a file covering all of the invalid updates
        f2.write(segment)
    f2.close()

    # based on the list containing the valid updates,
    for seg in goodFileInfo:
        nation_name = seg[0]  # storing the nation name in a separate variable for understandability
        cont = ""
        pop = ""  # initializing field updates for every valid line as empty strings
        area = ""
        addFlag = False  # initializing the flag for adding the fields (of each line) as a new country, to False

        # looping through contents of the valid line (file segment) list
        for updateField in seg:
            addFlag = False
            updType = updateField[0:2]  # substring represents the type for the update
            updInfo = updateField[2:]

            # instance when line update is valid, and country already exists in the catalogue
            if logObj.findCountry(nation_name):
                if updType == "P=":
                    logObj.setPopulationOfCountry(nation_name, updInfo)
                elif updType == "A=":
                    logObj.setAreaOfCountry(nation_name, updInfo)
                elif updType == "C=":
                    logObj.setContinentOfCountry(nation_name, updInfo)
            else:
                # instance when line update is valid, but the country doesn't exist in the catalogue

                addFlag = True  # setting the flag for adding new country, to False
                if updType == "P=":
                    pop = updInfo
                elif updType == "A=":  # based on the field's update-type, assigning the field info to a related variable
                    area = updInfo
                elif updType == "C=":
                    cont = updInfo

        # instance that flag is true for adding a new country to the catalogue
        if addFlag:
            logObj.addCountry(nation_name, pop, area, cont)  # invoking a method of the object to add country

    logObj.saveCountryCatalogue("output.txt")  # invoking a method of the object to save the entire catalogue to a text file

    tupleOut = (True, logObj)  # setting a tuple that contains a boolean, and the instantiated catalogue object
    return tupleOut

# *********************************************************************************************************************
