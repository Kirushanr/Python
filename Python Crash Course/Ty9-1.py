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

restaurant = Restaurant('Eat with us', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
