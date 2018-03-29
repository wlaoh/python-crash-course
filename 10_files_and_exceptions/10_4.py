while True:
    name = input('What\'s your name? ')
    if name == 'quit':
        break
    print('Hi! ' + name + ', nice to meet you!')
    with open('10_files_and_exceptions/guest_book.txt', 'a') as file_object:
        file_object.write(name + '\n')