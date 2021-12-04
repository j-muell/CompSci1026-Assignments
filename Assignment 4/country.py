# Programmer: Jason Mueller
# Date: Dec 6
# CS 1026
# Assignment 4
# File Uses:

class Country(object):
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.population = pop
        self.area = area
        self.continent = continent
        self.nameOG = name
        self.continentOG = continent

    def listToString(self, s):
        newStr = " "
        return (newStr.join(s)) 

  
    # --GETTERS--

    def getName(self):
        self.name = self.name.split('_')
        self.name = self.listToString(self.name)
        return self.name
    
    def getPopulation(self):
        return self.population
    
    def getArea(self):
        return self.area

    def getContinent(self):
        self.continent = self.continent.split('_')
        self.continent = self.listToString(self.continent)
        return self.continent


    # --SETTERS--

    def setPopulation(self, pop):
        self.population = pop

    def setArea(self, area):
        self.area = area
    
    def setContinent(self, continent):
        self.continent = continent

    def original_printing(self):
        return '\n' + self.nameOG + '|' + self.continentOG + '|' + self.population + '|' + self.area

    # --STRING REPRESENTATION--


    def __repr__(self):
        return self.getName() + ' (pop: ' + self.getPopulation() + ', size: ' + self.getArea() + ') in ' + self.getContinent()
