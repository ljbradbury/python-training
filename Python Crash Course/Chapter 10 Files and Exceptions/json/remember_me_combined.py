'''

Lodas the username if it has previously been
stored, otherwise this will prompt for the
username and store it

'''

import json

filename = "username1.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back " + username + "!")
else:
    print("Welcome back " + username + "!")
