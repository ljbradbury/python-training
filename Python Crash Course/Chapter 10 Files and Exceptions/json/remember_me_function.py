'''

Moving the existing code for remember_me.py
into a number of functions

'''

import json


def get_stored_username():
    ''' Get stored username if available '''

    filename = "username123.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():

    ''' Prompt for a new username '''

    username = input("What is your username? ")

    filename = "username123.json"

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username


def greet_user():
    ''' Greet the user by username '''
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()

# Call greet_user which will call get_stored_username
greet_user()