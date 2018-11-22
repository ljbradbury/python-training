'''

Using json to read stored data,
run the number_writer.py file
first to store the data in json

'''

import json

filename = "numbers.json"
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
