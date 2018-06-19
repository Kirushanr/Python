class Restaurant():
    """Modeling the restaurant"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints information about the restaurant"""
        print("\nWelcome to " + self.name)
        print("We offer " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        """Prints the restuarant is open"""
        print("\n"+self.name + " restaurant is now open")

restaurant = Restaurant('Kothu', 'Sri Lankan')
restaurant.describe_restaurant()

restaurant = Restaurant('Chinese Dragon', 'Chinese')
restaurant.describe_restaurant()

restaurant = Restaurant('Chettinad', 'Indian')
restaurant.describe_restaurant()


