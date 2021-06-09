# Checks if the string entered by the user is a palindrome. 
# That is that it reads the same forwards as backwards like “racecar” 

#  racecar 

user_entry = input() #racecar
word_length = len(user_entry) #7
index = word_length - 1 #6
is_palindrome = True

while index >= 0 and is_palindrome == True:
    last_char = user_entry[index] #r  
    first_char = user_entry[word_length - 1 - index] #r

    if last_char != first_char:
        is_palindrome = False

    index = index - 1 #5

if is_palindrome == False:
    print("This is not a palindrome")
else:
    print("This is a palindrome")