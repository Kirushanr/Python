rivers = {'yamuna': 'india', 'nile': 'egypt', 'mahavali': 'sri lanka'}

for river, country in rivers.items():
    print(river.title() + "runs through " + country.title()+"\n")

print("Rivers: ")
for river in rivers.keys():
    print(river.title()+" ")

print("\nCountries:")
for country in rivers.values():
    print(country.title()+" ")
