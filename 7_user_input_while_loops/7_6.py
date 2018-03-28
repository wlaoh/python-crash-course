age = ''
prompt = 'How old are you? '
active = True

while active == True:
    age = input(prompt)
    if age == 'quit':
        active = False
        break
    age = int(age)
    if age < 3:
        print('Your ticket is free')
    elif age < 12:
        print('Your ticket costs $10')
    else:
        print('Your ticket costs $15')