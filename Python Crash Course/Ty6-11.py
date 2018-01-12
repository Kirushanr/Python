cities = {'Colombo ': {'Country': 'Sri Lanka', 'Population': '21.2 million',
                       'fact': 'Sri Lanka is formerly known as Ceylon'},
          'Chennai':  {'Country': 'India', 'Population': '1.324 billion',
                       'fact': 'Chennai is formerly known as Madras'}}

for city, information in cities.items():
    print("\nCity : "+ city)
    for key, value  in information.items():
        print(key + ": "+ value)
