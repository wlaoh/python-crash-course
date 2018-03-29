import json

try:
    with open('10_files_and_exceptions/fav_num.txt') as file_object:
        fav_num = json.load(file_object)
except FileNotFoundError:
    fav_num = input('What\'s your favorite number? ')
    with open ('10_files_and_exceptions/fav_num.txt', 'w') as file_object:
        json.dump(fav_num, file_object)
else:
    print('I know your favorite number!  It\'s ' + fav_num)