# Smallest number of notes/coins to make a specific amount of money in change

from decimal import *

user_input = input("How much do you have? £" )
amount = round(Decimal(user_input), 2)

rolling_amount = amount * 100

print(rolling_amount // 5000, "fifty pound note(s)")
rolling_amount = rolling_amount % 5000

print(rolling_amount // 2000, "twenty pound notes(s)")
rolling_amount = rolling_amount % 2000

print(rolling_amount // 1000, "ten pound notes(s)")
rolling_amount = rolling_amount % 1000

print(rolling_amount // 500, "five pound notes(s)")
rolling_amount = rolling_amount % 500

print(rolling_amount // 200, "two pound piece(s)")
rolling_amount = rolling_amount % 200

print(rolling_amount // 100, "one pound piece(s)")
rolling_amount = rolling_amount % 100

print(rolling_amount // 50, "fifty pence piece(s)")
rolling_amount = rolling_amount % 50

print(rolling_amount // 20, "twenty pence piece(s)")
rolling_amount = rolling_amount % 20

print(rolling_amount // 10, "ten pence piece(s)")
rolling_amount = rolling_amount % 10

print(rolling_amount // 5, "five pence piece(s)")
rolling_amount = rolling_amount % 5

print(rolling_amount // 2, "two pence piece(s)")
rolling_amount = rolling_amount % 2

print(rolling_amount // 1, "one pence piece(s)")
rolling_amount = rolling_amount % 1