''' As with is being used there is no need to call close on the
file as this is automatically closed
'''

with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())

''' Using a loop '''

filename = "C:\\Users\\Lyndon Bradbury\\PycharmProjects\\Projects\\Python Crash Course\\Chapter 10 Files and Exceptions\\pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

''' Listing the lines '''

filename = "C:\\Users\\Lyndon Bradbury\\PycharmProjects\\Projects\\Python Crash Course\\Chapter 10 Files and Exceptions\\pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
