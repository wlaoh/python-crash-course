topping = ''
prompt = 'What topping would you like on your pizza? '

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print('Adding ' + topping + ' to your pizza')