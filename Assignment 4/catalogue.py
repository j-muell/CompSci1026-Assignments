from country import Country

class CountryCatalogue(object):
    def __init__(self):
        self.countryCat = []
        
    def dataCreator(self, countryFile):

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

        return self.countryCat


print(CountryCatalogue().dataCreator('data.txt'))