def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names, great_names):
    while names:
        name = names.pop()
        great_names.append("Great " + name + "!")



names = ['devid', 'clerik', 'popov']
show_magicians(names)

great_names = []
make_great(names[:], great_names)
show_magicians(great_names)

show_magicians(names)
