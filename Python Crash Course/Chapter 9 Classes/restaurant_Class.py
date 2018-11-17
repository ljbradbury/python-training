# Book exercise for Classes

# Create a new Class for a restaurant

class Restaurant():
    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def describe_restaurant(self):
        print("\nThe restaurant name is " + self.name.title())
        print("The restaurant type is " + self.type.title())

    def open_restaurant(self):
        print("The restaurant " + self.name.title(), "is open\n")

restaurant1 = Restaurant("domino\'s", "pizza")
restaurant2 = Restaurant("continetnal", "kebab house")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()