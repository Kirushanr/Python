class Restaurant():
    """Modeling the restaurant"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints information about the restaurant"""
        print("Welcome to " + self.name)
        print("We offer " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        """Prints the restuarant is open"""
        print("\n"+self.name + " restaurant is now open")


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = []

    def print_ice_cream_flavours(self):
        """Print the ice-cream flavours provided by restraunt"""
        print("We offer the following ice-cream flavours: \n")
        for flavour in self.flavours:
            print(flavour)

my_restraunt = IceCreamStand('Chinese Dragon', 'Chinese')
my_restraunt.flavours = ['strawberry', 'chocolate', 'orange']
my_restraunt.describe_restaurant()
my_restraunt.print_ice_cream_flavours()
