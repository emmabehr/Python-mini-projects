# Enter a string and the program will reverse it and print it out.

user_entry = input()
reverse_string = ""
for character in user_entry:
    reverse_string = character + reverse_string
print (reverse_string) 
