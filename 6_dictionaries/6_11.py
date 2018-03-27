cities = {
    'los angeles': {
        'country': 'usa',
        'population': '3.9 million',
        'fact': 'center of nation\'s film and television industry',
    },
    'san francisco': {
        'country': 'usa',
        'population': '864 thousand',
        'fact': 'center of nation\'s technology industry',
    },
    'casablanca': {
        'country': 'morocco',
        'population': '3.1 million',
        'fact': 'one of africa\'s largest financial centers',
    },
}

for name, info in cities.items():
    print(name.title() + ': ' + str(info))