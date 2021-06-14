# Simple script for finding the longest word in a text file.

file_name = "sample.txt"
longest_word = ""


with open(file_name) as file:
    contents = file.read()
    contents = contents.replace("\n", " ")
    words = contents.split(" ")
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

print(f"The longest word is {longest_word} at {len(longest_word)} characters") 

