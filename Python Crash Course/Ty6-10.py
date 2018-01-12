favorite_numbers = {'Zoe': [10, 2, 9], 'Kevin': [6, 7, 11], 'Mo': [5, 6, 8]}

#iterate through the dictionary
for name, numbers in favorite_numbers.items():
    print("\n"+name.title() + " favorite numbers are: ")
    for number in numbers:
        print(number)
