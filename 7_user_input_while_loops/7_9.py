sandwich_orders = ['pastrami', 'reuben', 'pastrami', 'blt', 'pastrami', 'ham and cheese']
finished_sandwiches = []

print('We\'re all out of pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        continue
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('All these sandwiches were made: ')
print(str(finished_sandwiches))