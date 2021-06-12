# A simple rock paper scissors simulator.

import random

# Functions
def play_game():
    print("Choose (r)ock) | (p)aper | (s)cissors")
    user_input = input()
    user_pick = user_input[0].lower()

    ai_pick = random.choice(["r", "p", "s"])

    user_won = False

    if user_pick != ai_pick:
        if user_pick == "r":
            if ai_pick == "p":
                user_won = False
            else:
                user_won = True
        elif user_pick == "p":
            if ai_pick == "s":
                user_won = False
            else:
                user_won = True
        elif user_pick == "s":
            if ai_pick == "r":
                user_won = False
            else:
                user_won = True

    print("You picked: " + user_pick)
    print("AI picked: " + ai_pick)
    if user_pick == ai_pick:
        print ("It was a draw!")
    elif user_won:
        print("Congratulations you won!")
    else:
        print("Sorry you lost!")

# Main Program
play_game()

play_again = True
while play_again:
    print("Would you like to play again?")
    print("press y for yes")
    print("any other key for no")
    user_input = input().lower()
    if user_input == 'y':
        play_game()
    else:
        play_again = False

print("Thank you for playing!")
