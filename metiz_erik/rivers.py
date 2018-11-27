rivers = {
'nile': 'egypth',
'dnepr': 'kiev',
'kama': 'russia',
}

for name, key in rivers.items():
    print("The " + name.title() + " runs though " + key.title() + ".")

for name in rivers.values():
    print(name.title())

for key in rivers.keys():
    print(key.title())
