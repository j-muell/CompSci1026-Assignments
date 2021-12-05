"""
Alexander Belan-Hudson
Student Number:   [251206726]
Course Code:      [1026A]
Section Number:   [001]
Project:          Assignment 4 - Country Classes
File:             catalogue.py
Script houses the methods which would allow one to construct and manipulate entries of the country catalogue
"""


# ****************************************************   Script   *****************************************************

import country as nation


class CountryCatalogue:
    def __init__(self, countryFile):
        """
        Constructor method initially constructs the data structure of catalogue, based on the info of countryFile
        :param countryFile:     name of the file containing the country data
        """

        self.file_name = self.nameChecker(countryFile)      # rechecking the file name for .txt
        self.countryCat = []       # creating an empty list, representing the country catalogue
        count = 0       # initializing the line counter

        file1 = open(self.file_name, "r", encoding="utf-8")
        # traversing through the lines located in countryFile
        for line in file1.readlines():
            # ignoring the first irrelevant header
            if count > 0:

                self.text = line.split("|")     # splitting the line based on the vertical line division
                self.text[3] = self.text[3][:-1]        # eliminating the newline feed

                tempObj = nation.Country(self.text[0], self.text[2], self.text[3], self.text[1])
                self.countryCat.append(tempObj)     # creating an new instance of country and appending to countryCat

            count += 1  # incrementing the line counter
        file1.close()

    def setPopulationOfCountry(self, country, pop):
        """
        Method sets the population of the associated country
        :param country:
        :param pop:
        :return:
        """
        for obj in self.countryCat:
            if obj.getName() == country:
                obj.setPopulation(pop)

    def setAreaOfCountry(self, country, area):
        """
        Method sets the area of the associated country
        :param country:
        :param area:
        :return:
        """
        for obj in self.countryCat:
            if obj.getName() == country:
                obj.setArea(area)

    def setContinentOfCountry(self, country, continent):
        """
        Method sets the continent of the associated country
        :param country:
        :param continent:
        :return:
        """
        for obj in self.countryCat:
            if obj.getName() == country:
                obj.setContinent(continent)

    def findCountry(self, country):
        """
        Method identifies whether new country already exists in the catalogue
        :param country:
        :return: boolean object of none or the country object that was found
        """
        for obj in self.countryCat:
            if obj.getName() == country:
                return obj
        return None

    def addCountry(self, countryName, pop, area, cont):
        """
        Method adds a new country to the data structure countryCat
        :param countryName: Name of the country
        :param pop:         Population of the Country
        :param area:        Area of the Country
        :param cont:        Continent of the Country
        :return: boolean value representing the success (or failure) of adding the country to catalogue
        """

        # identifying whether country entry already exists, using an external method
        obj = self.findCountry(countryName)
        if obj is not None:     # if an object with the same country name is found, return false
            return False

        tempObj = nation.Country(countryName, pop, area, cont)
        self.countryCat.append(tempObj)     # creating a new country object and appending it to the catalogue

        return True

    def printCountryCatalogue(self):
        """
        Method prints the entirety of the catalogue countryCat
        :return:
        """
        for obj in self.countryCat:
            print(obj)

    def saveCountryCatalogue(self, fname):
        """
        Method saves the data structure of countryCat to an output file
        :param fname: name of the output file
        :return:
        """
        self.orderCat()     # calling upon method to organize countryCat
        self.file_name = self.nameChecker(fname)  # checking the name of output file

        # writing to output file the contents of countryCat
        file2 = open(self.file_name, "w")
        file2.write("Country|Continent|Population|Area\n")  # writing initial header line

        # traversing through countryCat and writing each line
        for obj in self.countryCat:
            file2.write(self.getFullLine(obj))

        file2.close()

    def orderCat(self):
        """
        Method employs selection sort to order the country objects in Alphabetical Order
        :return:
        """
        # traversing through list countryCat
        for i in range(len(self.countryCat) - 1):
            baseIndex = i

            # traversing through countryCat after the baseIndex value
            for j in range(i + 1, len(self.countryCat)):
                # instance wherein one index is alphabetically lower than the next
                if self.countryCat[baseIndex].getName() > self.countryCat[j].getName():
                    baseIndex = j  # redefining baseIndex

            # reordering objects in list based on the precedence of alphabetical order
            tempObj = self.countryCat[i]
            self.countryCat[i] = self.countryCat[baseIndex]
            self.countryCat[baseIndex] = tempObj

    @staticmethod
    def getFullLine(obj):
        """
        Static method returns a concatenated string using
        :param obj:     individual object housed within countryCat list
        :return: a string containing the concatenated line of the country's associated information
        """
        line = ""
        line += obj.getName() + "|" + obj.getContinent() + "|" + obj.getPopulation() + "|" + obj.getArea() + "\n"
        return line

    @staticmethod
    def nameChecker(name):
        """
        Static method double-checks the name of files for .txt on end of file name, in case of class-direct usage
        :param name:
        :return: a potentially updated name
        """
        if ".txt" in name:
            return name
        else:
            name = name + ".txt"
            return name

# *********************************************************************************************************************
