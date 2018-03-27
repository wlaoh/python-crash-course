favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'winston': 'go',
    'eric': 'javascript',
    'ben': 'javascript',
    'martin': 'javascript',
}

should_take_list = ['martin', 'jen', 'ashley', 'sameer', 'david']

for name in should_take_list:
    if name in favorite_languages.keys():
        print('Thanks for responding')
    else:
        print('Please take the poll')