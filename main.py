from datetime import datetime

# Getting the time now
time_now = datetime.now()

# Getting the hour and minute
hour = time_now.hour
minute = time_now.minute
seconds = time_now.second

# User input for the time they want to go home
home_hour = int(input("What time do you want to go home? (hour): "))
home_minute = int(input("What time do you want to go home? (minute): "))
home_seconds = int(input("What time do you want to go home? (seconds): "))

def calculate_home():
    # Calculate hours and minutes until home
    until_home_hour = home_hour - hour
    until_home_minute = home_minute - minute
    until_home_seconds = home_seconds - seconds

    # Adjust if minutes are negative
    if until_home_minute < 0:
        until_home_minute += 60
        until_home_hour -= 1

    if until_home_seconds < 0:
        until_home_seconds += 60
        until_home_minute -= 1

    return print(f"It is sadly {until_home_hour} {'hours' if until_home_hour > 1 else 'hour'}, "
                 f"{until_home_minute} {'minutes' if until_home_minute > 1 else 'minute'} "
                 f"{f'and {until_home_seconds} seconds' if until_home_seconds > 1 else f'and {until_home_seconds} second'}"
                 f" until home :-(")


print()
calculate_home()
