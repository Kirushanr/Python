class User():
    """ Modeling user """

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def describe_user(self):
        """Prints the summary of a user"""
        print("\nFirst name: " + self.firstname.title())
        print("Last name: " + self.lastname.title())

    def greet_user(self):
        """Prints personalized greeting to the user"""
        print("Welcome " + self.firstname.title() + " " + self.lastname.title())


user = User('harry', 'potter')
user.describe_user()
user.greet_user()

new_user = User('ron', 'weasley')
new_user.describe_user()
new_user.greet_user()
