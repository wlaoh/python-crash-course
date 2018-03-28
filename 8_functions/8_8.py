def make_album(artist, title, tracks=0):
    if tracks != 0:
        return {'artist': artist, 'title': title, 'tracks': tracks}
    return {'artist': artist, 'title': title}

while True:
    print('Enter "q" any time to quit')
    artist = input('Enter an artist name: ')
    if artist == 'q':
        break
    album = input('Enter an album name: ')
    if album == 'q':
        break
    print(make_album(artist, album))