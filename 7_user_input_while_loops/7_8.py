sandwich_orders = ['pastrami', 'reuben', 'blt', 'ham and cheese']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich + ' sandwich')
    finished_sandwiches.append(sandwich)

print('All these sandwiches were made: ')
print(str(finished_sandwiches))