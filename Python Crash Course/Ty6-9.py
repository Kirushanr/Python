favorite_places = {'Rus': ['Russia', 'Ukraine', 'Bali'], 'Muru': ['Sri Lanka', 'India', 'Pakistan'], 'Zoe': ['Australia', 'UK', 'US'] }

for name, places in favorite_places.items():
    print("\n"+name.title() + "'s" + " favorite places are : ")
    for p in places:
        print(p)
