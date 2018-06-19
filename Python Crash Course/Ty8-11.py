def show_magicians(magician_list):
    """Prints the name of each magician"""
    for magician in magician_list:
        print(magician)


def make_great(magician_list):
    """returns a list of the Great magicians """
    great_magician = []
    while magician_list:
        value = magician_list.pop() + " The Great"
        great_magician.append(value)
    return great_magician


magicians = ['Ron', 'Harry', 'Hermoine', 'Luna']
show_magicians(magicians)
print("\n")
great_magician_list = make_great(magicians)
show_magicians(great_magician_list)