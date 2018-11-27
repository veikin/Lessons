def make_car(name_car, type_car, **other):
    profile = {}
    profile['name_car'] = name_car
    profile['type_car'] = type_car
    for key, value in other.items():
        profile[key] = value
    return profile
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
