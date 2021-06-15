#Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) 
# and validates it to make sure that it is a valid number (look into how credit cards use a checksum).
print("Please input credit card number to check")
card_number = input()
if len(card_number) != 16:
    print(f"The number you have entered {card_number} is not 16 digits")
    exit()

sum_one = 0
sum_two = 0
index = len(card_number) - 1
while index >= 0:
    number = int(card_number[index])
    if index % 2 == 0:
        doubled = number * 2
        if doubled >= 10:
            product = 1 
            right = doubled % 10
            left = int(doubled / 10)
            sum_one = sum_one + right + left
        else:
            sum_one = sum_one + doubled
    else:
        sum_two = sum_two + number
    index = index - 1

total_sum = sum_one + sum_two
if total_sum % 10 == 0:
    print("Credit Card number is valid")
else:
    print("Credit Card number is not valid")


