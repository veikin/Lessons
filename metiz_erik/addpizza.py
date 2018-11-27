pizza = "\nEnter pizza supplement: "
pizza += "\n(Enter 'quit' when you are finished)"

while True:
    order = input(pizza)

    if order == 'quit':
        break
    else:
        print(order.title() + " add to order.")
