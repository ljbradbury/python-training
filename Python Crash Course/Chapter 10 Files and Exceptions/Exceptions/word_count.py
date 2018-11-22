'''

A function to count the number of words in a file

'''

def count_words(failename):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            file_contents = f_obj.read()

    except FileNotFoundError:
        message = "Sorry the file '" + filename + "' does not exist"
        print(message)

    else:
        # Count the number of words in a file
        words = file_contents.split()
        number_words = len(words)
        print("The file '" + filename + "' has '" + str(number_words) + "' words in it.")

''' 
Create a list to store the filenames in so that the function will go through them all
and print out the output
'''
filenames = ["alice1.txt", "alice1.txt", "alice1.txt", "nosuchfile.txt"]
# We have create a list called filenames and added three files in it

# We have a for loop to loop through each item (filename) in the list filenames
# and count the words

for filename in filenames:
    count_words(filename)
