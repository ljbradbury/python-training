'''

Handling the FileNotFoundError exception and
failing silently

'''

filename = "alice.txt"

try:

    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    message = "Sorry the file '" + filename + "' does not exist"
    print(message)

'''
Analyzing text, counting the words in a file
'''

filename = "alice1.txt"

try:

    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
       msg = ("Sorry, the file '" + filename + "' does not exist.")
       print(msg)
else:
    # Count the number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file '" + filename + "' has '" + str(num_words) + "' words in it")
