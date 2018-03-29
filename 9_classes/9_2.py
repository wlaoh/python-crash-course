class Restaurant():

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('The name of the restaurant is: ' + self.restaurant_name)
        print('This place serves: ' + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open!')


my_restaurant1 = Restaurant('Little Caesars', 'Pizza')
my_restaurant2 = Restaurant('Olive Garden', 'Italian')
my_restaurant3 = Restaurant('In n Out', 'Burgers')

my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()