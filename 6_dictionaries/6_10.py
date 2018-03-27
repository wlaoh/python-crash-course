favorite_numbers = {
    'winston': [1, 2, 3],
    'ashley': [2, 3, 4],
    'ben': [3, 4, 5],
    'eric': [4, 5, 6],
    'sameer': [5, 6, 7],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + ': ' + str(numbers))