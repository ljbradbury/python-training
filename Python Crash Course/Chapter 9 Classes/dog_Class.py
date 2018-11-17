# A simple class that represents a dog
# This can apply to any dog

# All dogs have a name and an age
# Dog's can sit and roll over

# This class will tell Python how to make an object representing a dog, after this is written
# this will be used to make individual instances, each of which represents one specific dog

class Dog(): # The class name starts with an upper case letter
    '''A class to create a simple model of a dog'''
    def __init__(self, name, age):
        # This __init__(self): is a default method in Python and runs whenever a new instance
        # is created based on the dog class
        # Whenever a new instance of Dog class is created then the values for name and age must be passed

        '''Initialize the name and age attributes'''
        # Define the varaiables name and age
        # These have a prefix of self. are available in every method in the class
        # self.name = name, takes the value stored in the parameter name and stores it
        # in the variable called name which is then attached to the instance being created
        self.name = name
        self.age = age

    # Create the sit and roll_over Methods
    # As these methods don't need any additional information like name and age they are defined
    # with one parameter called self

    def sit(self):
        ''' Simulate a dog sitting in response to a command'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        ''' Simulate a dog rolling over in response to a command'''
        print(self.name.title() + " rolled over")


# Create an instance of a dog using the Dog class
# Store the instance of the dog creation in a variable called my_dog
# Creating an instance of a class lower case letters are used
my_dog = Dog('washington', 12)

# Print some text and also call the variable along with the attribute name
# title is used to make the first letter uppercase
print("My dog's name was " + my_dog.name.title() + ".")

# Print some text and also call the variable along with the attribute
# age converted to a string as it's a number
print("My dog was " + str(my_dog.age) + " years old")

# Calling methods
# methods can be called by using dot notation
# example my_dog.sit()
# my_dog.roll_over()

# When Python reads my_dog.sit() it looks for the sit() method in the
# class Dog and runs that code

my_dog.sit()
my_dog.roll_over()

# Creating multiple Instances from a single class

my_dog = Dog('washington', 12)
your_dog = Dog('susie', 15)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()
your_dog.roll_over()