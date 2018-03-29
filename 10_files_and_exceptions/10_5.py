while True:
    response = input('Why do you like programming? ')
    if response == 'quit':
        break
    with open('10_files_and_exceptions/responses.txt', 'a') as file_object:
        file_object.write(response + '\n')