# Car Class

class Car():
    ''' A simple class to represent a car '''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def descriptive_name(self):
        ''' Return a neatly formatted descriptive name '''
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        ''' Print a statement showing the cars mileage '''
        print("\nThis car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        ''' Set the odometer_reading to a given value '''
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        ''' Increments the odometer reading by a given amount'''
        self.odometer_reading += miles

# This calls my_new_car and passes three attributes
my_new_car = Car("audi", "quattro", 2013)
print(my_new_car.descriptive_name())

# Using a method to update the value
#my_new_car.update_odometer(99)
#my_new_car.read_odometer()

# The first reading calls the initial variable which is 0
#my_new_car.read_odometer()

# Here I'm calling my_new_car. and statically setting the value of the variable to 23
#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()

# Calling increment_odometer to add the value to the odometer
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
