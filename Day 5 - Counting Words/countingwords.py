# Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

with open('sample.txt') as file:
    content = file.read()
    words = content.split(" ")
    print(len(words))