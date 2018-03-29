try:
    with open('10_files_and_exceptions/cats.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    pass

try:
    with open('10_files_and_exceptions/dogs.txt') as file_object:
        print(file_object.read())
except FileNotFoundError:
    pass