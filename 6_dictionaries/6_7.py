winston = {
    'first_name': 'Winston',
    'last_name': 'Laoh',
    'age': '28',
    'city': 'Los Angeles',
}

ben = {
    'first_name': 'Ben',
    'last_name': 'Tran',
    'age': '24',
    'city': 'Los Angeles',
}

eric = {
    'first_name': 'Eric',
    'last_name': 'Hirshfield',
    'age': '26',
    'city': 'Los Angeles',
}

people = [winston, ben, eric]

for person in people:
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])
