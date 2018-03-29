class Restaurant():

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('The name of the restaurant is: ' + self.restaurant_name)
        print('This place serves: ' + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open!')


my_restaurant = Restaurant('Little Caesars', 'Pizza')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()