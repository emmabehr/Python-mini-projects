# take input from the user regarding the length of the countdown in seconds. 
# After that, a countdown will begin on the screen of the format ‘minutes: seconds’.

import time

def clear_output():
    print("\r", end='\r', flush=True)

def countdown(timer):
    seconds = int(timer)
    while seconds > 0:
        div = divmod(seconds, 60)
        clear_output()
        print(f"{div[0]} minutes {div[1]} seconds remaining. ", flush=True, end="")
        seconds = seconds - 1
        time.sleep(1)
    
    clear_output()
    print(f"The Countdown has now completed")

print("Please enter countdown in seconds")
user_input = input()
countdown(user_input)