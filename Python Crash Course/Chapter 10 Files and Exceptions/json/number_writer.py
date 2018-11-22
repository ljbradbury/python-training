'''

Using json to store data
this has to be ran before
the number_reader.py tries
to read the stored data

'''

import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filename = "numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
