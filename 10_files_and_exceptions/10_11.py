import json

fav_num = input('What\'s your favorite number? ')

with open ('10_files_and_exceptions/fav_num.txt', 'w') as file_object:
    json.dump(fav_num, file_object)