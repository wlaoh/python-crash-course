def make_car(manufacturer, model, **features):
    built_car = {'manufacturer': manufacturer, 'model': model}
    for key, value in features.items():
        built_car[key] = value
    return built_car

car = make_car('volkswagen', 'golf gti', trim='autobahn', color='white')

print(car)