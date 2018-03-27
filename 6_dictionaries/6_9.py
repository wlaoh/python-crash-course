favorite_places = {
    'winston': ['los angeles', 'seattle', 'portland'],
    'ashley': ['los angeles', 'hawaii', 'michigan'],
    'ben': ['los angeles', 'valley', 'san francisco'],
}

for name, places in favorite_places.items():
    print(name.title() + ': ' + str(places))