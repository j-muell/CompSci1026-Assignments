from catalogue import CountryCatalogue
from country import Country

countryTester = Country('New_York,' '10', '50000', 'United_States_Of_America')


print(CountryCatalogue('data.txt').findCountry(countryTester))