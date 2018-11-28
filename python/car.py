"""Class for presentation car"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
        
    def get_discriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometr(self):
        print("This car has " + str(self.odometr_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometr(self, miles):
        self.odometr_reading += miles

