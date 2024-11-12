#TODO variabel for når jeg vil hjem
#TODO variabel for hva tiden er
#TODO noe kalkulasjon for tiden jeg vil hjem - tiden nå
#TODO print som forteller hvor lenge det er til hjem
from datetime import datetime

# Getting the time now
time_now = datetime.now()

# Getting the hour and minute
hour = time_now.hour
minute = time_now.minute

# User input for the time they want to go home
home_hour = int(input("What time do you want to go home? (hour): "))
home_minute = int(input("What time do you want to go home? (minute): "))

def calculate_home():
    # Calculate hours and minutes until home
    until_home_hour = home_hour - hour
    until_home_minute = home_minute - minute

    # Adjust if minutes are negative
    if until_home_minute < 0:
        until_home_minute += 60
        until_home_hour -= 1

    # Print the result
    return print(f"It is sadly {until_home_hour}:{until_home_minute:02} until home :-(")

print()
calculate_home()
