with open('10_files_and_exceptions/learning_python.txt') as file_object:
    for line in file_object:
        print(line.replace('Python', 'Javascript').rstrip())