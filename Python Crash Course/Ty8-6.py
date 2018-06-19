def city_country(city, country):
    """ Return a formated string """
    string = city + ", " + country
    return string.title()


formatted_string = city_country('sydney', 'australia')
print(formatted_string)
formatted_string = city_country('delhi', 'India')
print(formatted_string)
formatted_string = city_country('colombo', 'sri lanka')
print(formatted_string)
