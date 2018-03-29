number1 = input('Please enter the first number: ')
number2 = input('Please enter the second number: ')

try:
    number1 = int(number1)
    number2 = int(number2)
except ValueError:
    print('Please enter a number!')
else:
    print(str(number1 + number2))