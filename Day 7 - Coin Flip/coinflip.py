# Write some code that simulates flipping a single coin however many times the user decides. 
# The code should record the outcomes and count the number of tails and heads.

import random

print("How many times to flip the coin?")
count = input()
counter = int(count)
count_heads = 0
count_tails = 0 
while counter > 0:
    flip = random.choice(["h","t"])
    if flip == "h":
        count_heads = count_heads + 1
    elif flip == "t":
        count_tails = count_tails + 1
    counter = counter - 1 

print("The coin was flipped {0} times".format(count))
print("The coin landed on heads {0} times".format(count_heads))
print("The coin landed on tails {0} times".format(count_tails))