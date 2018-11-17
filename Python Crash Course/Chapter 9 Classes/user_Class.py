# Book exercise for Classes in Chapter 9

# This is a users class

class User():
    def __init__(self, first_name, last_name, age, dob):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.dob = dob


    def describe_user(self):
        print("\nThe users name is ", self.firstname.title(), self.lastname.title())
        print("The age of", self.firstname.title(), "is", (self.age))
        print("The date of birth of", self.firstname.title(), "is", str(self.dob))

    def greet_user(self):
        print("Welcome, ", self.firstname.title(), self.lastname.title())

user1 = User("lyndon", "bradbury", 47, "15/06/1971")
user2 = User("stephen", "jones", 48, "16/6/1971")
user3 = User("gareth", "preece", 41, "17/6/1980")
user4 = User("andre", "hopper", 99, "10/10/1066")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()
