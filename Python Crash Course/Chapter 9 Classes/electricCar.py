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

# Calling increment_odometer to add the value to the odometer
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

'''

# Inheritance 

Create a new class that is based on another class
in this example this is a new class called ElectricCar
that is based on the class Car
'''
class ElectricCar(Car):
    ''' Represents aspects of a car specific to an electric car'''
    def __init__(self, make, model, year):
        ''' Initialize the attributes of the parent class'''
        '''
        
        The super() function is used to tell python 
        to call the __init__() method from ElectricCar's
        parent class and store it in 'myTesla'
        
        '''
        super().__init__(make, model, year)

        # Create an attribute specific to an electric car
        self.battery_size = 70

    def descriptive_battery(self):
        ''' Print statement for the battery size'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

myTesla = ElectricCar("Tesla", "model S", "2016")
print("\n" + myTesla.descriptive_name())
myTesla.descriptive_battery()