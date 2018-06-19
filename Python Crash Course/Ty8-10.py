def show_magicians(magician_list):
    """Prints the name of each magician"""
    for magician in magician_list:
        print(magician)


def make_great(magician_list):
    """Modifies the existing list and """
    for value in range(0, len(magician_list)):
        magician_list[value] =  magician_list[value] + " The Great"


magicians = ['Ron', 'Harry', 'Hermoine', 'Luna']
show_magicians(magicians)
print("\n")
make_great(magicians)
show_magicians(magicians)
