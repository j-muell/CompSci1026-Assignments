# Programmer: Jason Mueller
# Date: Dec 6
# CS 1026
# Assignment 4
# File Uses:

from country import Country

class CountryCatalogue(object):
    def __init__(self, countryFile):
        self.countryCat = []


        with open(countryFile, encoding="utf-8", errors="ignore") as f:
            country_list = f.read().splitlines()

        for entry in country_list[:1]:                              # the purpose of this section is to use the header to verify the order of the data in the files
            formatted_header = entry.split('|')
            testers = ['Country', 'Continent', 'Population', 'Area']
            for theType in testers:
                for index, element in enumerate(formatted_header):
                    if theType == element:
                        if element == 'Country':
                            country_num = index
                        if element == 'Continent':
                            continent_num = index
                        if element == 'Population':
                            pop_num = index
                        if element == 'Area':
                            area_num = index
                    continue
                continue
        
        for entry in country_list[1:]:
            formatted = entry.split('|')
                        
            countryUp = Country(formatted[country_num], formatted[pop_num], formatted[area_num], formatted[continent_num])
            self.countryCat.append(countryUp)

    def setPopulationOfCountry(self, country, pop):
        for i in self.countryCat:
            if i.getName() == country:
                i.setPopulation(pop)

    def setAreaOfCountry(self, country, area):
        for i in self.countryCat:
            if i.getName() == country:
                i.setArea(area)
            
    def setContinentOfCountry(self, country, continent):
        for i in self.countryCat:
            if i.getName() == country:
                i.setContinent(continent)

    def findCountry(self, country):
        for obj in self.countryCat:
            if obj.getName() == country:
                return obj
            else:
                return None

    def addCountry(self, countryName, pop, area, cont):
        countryToAdd = Country(countryName, pop, area, cont)
        if countryToAdd in self.countryCat:
            return False
        else:
            self.countryCat.append(countryToAdd)
            return True

    def printCountryCatalogue(self):
        for entry in self.countryCat:
            print(entry)

    def saveCountryCatalogue(self, fname = 'testWriting.txt'):
        sorted_countryCat = sorted(self.countryCat, key=lambda x: x.name, reverse=False)    
        with open(fname, 'w') as out_file:
            out_file.write('Country|Continent|Population|Area')
            for i in sorted_countryCat:
                out_file.write(i.original_printing())



