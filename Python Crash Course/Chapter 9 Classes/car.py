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
