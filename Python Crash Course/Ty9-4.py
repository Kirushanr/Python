class Restaurant():
    """Modeling the restaurant"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints information about the restaurant"""
        print("Welcome to " + self.name)
        print("We offer " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        """Prints the restuarant is open"""
        print("\n"+self.name + " restaurant is now open")
    
    def set_number_served(self, no_served):
        """Sets the number of customers served"""
        self.number_served = no_served
    
    def increment_number_served(self, no_served):
        """Increments the number of customers served by a value"""
        self.number_served += no_served

restaurant = Restaurant('Eat with us', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("We have served "  + str(restaurant.number_served) + " customers")
restaurant.set_number_served(10)
print("We have served "  + str(restaurant.number_served) + " customers")
restaurant.increment_number_served(5)
print("We have served "  + str(restaurant.number_served) + " customers")