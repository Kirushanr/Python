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


class Admin(User):
    """Modeling Admin"""

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.privileges = []

    def show_privileges(self):
        """Prints the privileges of admin"""
        print("\nPrivileges: ")
        for privilege in self.privileges:
            print(privilege)


my_admin = Admin('Harry', 'Potter')
my_admin.greet_user()
my_admin.privileges = ["can add post", "can delete post", "can ban user"]
my_admin.show_privileges()
