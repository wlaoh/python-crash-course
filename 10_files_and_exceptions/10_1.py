with open('10_files_and_exceptions/learning_python.txt') as file_object:
    print(file_object.read())

with open('10_files_and_exceptions/learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

with open('10_files_and_exceptions/learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())