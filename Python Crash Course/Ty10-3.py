"""
Writes the names of the guests to the Guest Book
"""
file_name = "guest.txt"
name_of_the_guest = input("Please enter your name:")

with open(file_name, "a") as file_object :
    file_object.write(name_of_the_guest+"\n");