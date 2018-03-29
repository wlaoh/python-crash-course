while True:
    number1 = input('Please enter the first number or "q" to quit: ')
    if number1 == 'q':
        break
    number2 = input('Please enter the second number or "q" to quit: ')
    if number1 == 'q':
        break
    try:
        number1 = int(number1)
        number2 = int(number2)
    except ValueError:
        print('Please enter a number!')
    else:
        print(str(number1 + number2))