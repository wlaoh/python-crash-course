class User():
    def __init__(self, first_name, last_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
    
    def describe_user(self):
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        print('Email: ' + self.email)
        print('Location: ' + self.location)

    def greet_user(self):
        print('Hi! ' + self.first_name + ', how are you?')

winston = User('winston', 'laoh', 'winston.laoh@gmail.com', 'Los Angeles')

winston.describe_user()
winston.greet_user()