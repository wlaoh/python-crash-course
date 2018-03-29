from user import User

class Admin(User):
    def __init__(self, first_name, last_name, email, location, *privileges):
        super().__init__(first_name, last_name, email, location)
        self.privileges = Privileges(privileges)

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print('The list of privileges are: ' + str(self.privileges))