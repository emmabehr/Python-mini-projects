# Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

user_entry = input()
counter_a = 0
counter_e = 0
counter_i = 0
counter_o = 0
counter_u = 0

for char in user_entry.lower():
    if char == "a":
        counter_a = counter_a + 1
    elif char == "e":
        counter_e = counter_e + 1
    elif char == "i":
        counter_i = counter_i + 1
    elif char == "o":
        counter_o = counter_o + 1
    elif char == "u":
        counter_u = counter_u + 1

print("Summary of vowels found:")
print("a - " + str(counter_a) + " times")
print("e - " + str(counter_e) + " times")
print("i - " + str(counter_i) + " times")
print("o - " + str(counter_o) + " times")
print("u - " + str(counter_u) + " times")