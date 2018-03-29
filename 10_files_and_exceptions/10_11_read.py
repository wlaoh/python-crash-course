import json

with open('10_files_and_exceptions/fav_num.txt') as file_object:
    fav_num = json.load(file_object)

print('I know your favorite number!  It\'s ' + fav_num)