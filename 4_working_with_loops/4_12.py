pizzas = ['pepperoni', 'deluxe', 'mushrooms and pepperoni', 'meat lovers', 'cheese']
friend_pizzas = pizzas[:]
pizzas.append('four cheese')
friend_pizzas.append('heart of artichoke')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)
print('My friend\'s favorite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)