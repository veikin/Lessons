class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Name: " + self.restaurant_name.title())
        print("Size: " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The " + self.restaurant_name.title() + " is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, add_number):
        self.number_served += add_number

    def print_number_served(self):
        print("Count men: " + str(self.number_served) + " in restaurant.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors 

    def describe_ice_cream(self):
        print("Flavors: " + str(self.flavors))

ice_cream_stand = IceCreamStand('some', 'else', ['and', 'more'])
ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_ice_cream()
