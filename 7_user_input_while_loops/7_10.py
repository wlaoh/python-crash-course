active = True
places = []

while active:
    place = input('If you could visit one place in the world, where would you go? ')
    places.append(place)
    repeat = input('Would you like to add more places? ')
    if repeat != 'no':
        continue
    active = False

print('Places you would like to go: ')
print(str(places))