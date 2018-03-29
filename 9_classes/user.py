class User():
    def __init__(self, first_name, last_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print('First name: ' + self.first_name.title())
        print('Last name: ' + self.last_name.title())
        print('Email: ' + self.email)
        print('Location: ' + self.location.title())

    def greet_user(self):
        print('Hi! ' + self.first_name.title() + ', how are you?')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0