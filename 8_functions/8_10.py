def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians, magicians_the_great):
    while magicians:
        magician = magicians.pop()
        magicians_the_great.append(magician + ' the Great')

magicians = ['Winston', 'Ashley', 'Leon']
magicians_the_great = []
show_magicians(magicians)
make_great(magicians, magicians_the_great)
show_magicians(magicians_the_great)
show_magicians(magicians)