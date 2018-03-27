numbers = [v for v in range(1, 10)]
ordinal_suffix = ''

for number in numbers:
    if number == 1:
        ordinal_suffix = 'st'
    elif number == 2:
        ordinal_suffix = 'nd'
    elif number == 3:
        ordinal_suffix = 'rd'
    else:
        ordinal_suffix = 'th'
    print(str(number) + ordinal_suffix)