'''

Handling the FileNotFoundError exception

'''

filename = "alice.txt"

try:

    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
       msg = ("Sorry, the file does not exist.")
       print(msg)
