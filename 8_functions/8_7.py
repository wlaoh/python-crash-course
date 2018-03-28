def make_album(artist, title, tracks=0):
    if tracks != 0:
        return {'artist': artist, 'title': title, 'tracks': tracks}
    return {'artist': artist, 'title': title}

print(make_album('Weezer', 'The Green Album'))
print(make_album('Avicii', 'The Nights'))
print(make_album('Weird Al', 'Running with Scissors'))
print(make_album('Armin van Buuren', 'Intense', 15))
