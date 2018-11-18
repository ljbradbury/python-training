'''
Writing to an empty file:

'w' = Write
'r' = Read
'a' = Append

'''
filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming")

