vacation = {}

dream = True

while dream:
    name = input("what is your name? ")
    city = input("Where are u dream vacation? ")

    vacation[name] = city

    answ = input("You want enter another entry? (y/n) ")
    if answ == 'n':
        break

for name, city in vacation.items():
    print(name.title() + " you choice is " + city.title())
