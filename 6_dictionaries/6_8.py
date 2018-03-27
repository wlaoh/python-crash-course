too_sweety = {
    'owners_name': 'Winston',
    'age': 12
}

belle = {
    'owners_name': 'Ashley',
    'age': 6
}

buffy = {
    'owners_name': 'Gary',
    'age': 2
}

pets = [too_sweety, belle, buffy]

for pet in pets:
    print(pet['owners_name'])
    print(pet['age'])