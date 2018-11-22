'''

Saving and reading user generated data, this
asks a user to input their name and then this
stores that in a json file called username.json

'''

import json

username = input("What is your name? ")

filename = "username.json"

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back " + username + "!")
