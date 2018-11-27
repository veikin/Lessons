pizzas = ['the detroiter', 'margherita', 'napolitano']
friend_pizzas = pizzas[:]

pizzas.append('papperoni')
friend_pizzas.append('chelentano')

for pizza in pizzas:
    print("My favorite pizzas are:" + pizza.title() + "!\n")

for friend in friend_pizzas:
    print("My friend's favorite pizzas are:" + friend.title() + "!")
