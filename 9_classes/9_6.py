class Restaurant():

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0
    
    def describe_restaurant(self):
        print('The name of the restaurant is: ' + self.restaurant_name.title())
        print('This place serves: ' + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open!')
    
    def set_numbers_served(self, numbers):
        self.numbers_served = numbers
    
    def increment_number_served(self, number):
        self.numbers_served += number

class IceCreamStand(Restaurant):
    def __init__(self, name, *flavors):
        super().__init__(name, 'ice cream')
        self.flavors = flavors
    
    def display_flavors(self):
        print('The flavors today are: ' + str(self.flavors))

scoops_westside = IceCreamStand('Scoops Westside', 'brown brown bread', 'chocolate lavendar', 'chocolate vanilla cola')

scoops_westside.display_flavors()