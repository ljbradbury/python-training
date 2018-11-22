'''

This is will load a json file and print
out the details to the user

'''

import json

filename = "username.json"

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back " + username +" it's nice to see you")
    