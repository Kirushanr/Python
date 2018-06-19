class User():
    """ Modeling user """

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.login_attempts = 0

    def describe_user(self):
        """Prints the summary of a user"""
        print("\nFirst name: " + self.firstname.title())
        print("Last name: " + self.lastname.title())

    def greet_user(self):
        """Prints personalized greeting to the user"""
        print("Welcome " + self.firstname.title() + " " + self.lastname.title())

    def increment_login_attempts(self):
        """Increments the login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts"""
        self.login_attempts = 0

user = User('harry', 'potter')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
print("No of login attempts made " + str(user.login_attempts))
user.reset_login_attempts()
print("No of login attempts made " + str(user.login_attempts))
