age = "\nEtnter your age plese: "
mes = ''
active = True
while active:
    mes = int(input(age))
    
    if mes <= 3:
        print("Is free")
    elif mes <= 12:
        print("$10")
    elif mes > 12:
        print("$15")
    else:
        break
