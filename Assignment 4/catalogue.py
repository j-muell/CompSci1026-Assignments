from country import Country

class CountryCatalogue(object):
    def __init__(self, countryFile):
        self.countryCat = []
        

        with open(countryFile, encoding="utf-8", errors="ignore") as f:
            country_list = f.read().splitlines()

        for entry in country_list[:1]:
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
        pass

    def setAreaOfCountry(self, country, area):
        pass

    def setContinentOfCountry(self, country, continent):
        pass

    def findCountry(self, country):
        for obj in self.countryCat:
            if obj.getName() == country:
                return obj
            else:
                return None
    
    def getName(self):
        return self.name

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
        


