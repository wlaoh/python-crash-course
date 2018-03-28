age = ''
prompt = 'How old are you? '

while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Your ticket is free')
    elif age < 12:
        print('Your ticket costs $10')
    else:
        print('Your ticket costs $15')