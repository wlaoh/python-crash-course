cat = 'too sweety'
print("Is cat == 'too sweety'?  I predict True")
print(cat == 'toosweety')
print("Is cat == 'belle'?  I predict False")
print(cat == 'belle')
print("Is cat not 'spot'?  I predict True")
print(cat != 'spot')
print('Is cat == "Too Sweety"?  I predict False')
print(cat == 'Too Sweety')
print('Is cat titled == "Too Sweety"?  I predict True')
print(cat.title() == 'Too Sweety')

print('Is 3 greater than or equal to 3?  I predict True')
print(3 >= 3)

print('Is 4 less than or equal to 3?  I predict False')
print(4 <= 3)

print('Is 4 greater than 3 and less than 5?  I predict True')
print( 4 > 3 and 4 < 5)

pizzas = ['pepperoni', 'cheese', 'deluxe']
print('Does Costco have anchovy pizzas?  I predict False')
print('anchovy' in pizzas)

print('Does Costco not have cheese pizza?  I predict False')
print('cheese' not in pizzas)