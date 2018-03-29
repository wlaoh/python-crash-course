with open('10_files_and_exceptions/sherlock_holmes.txt') as file_object:
    the_count = 0
    for line in file_object:
        the_count += line.lower().count('the')

print(the_count)