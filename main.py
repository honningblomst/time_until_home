from datetime import datetime
import time

# Getting the time now
time_now = datetime.now()

# User input for the time they want to go home
home_hour, home_minute, home_second = map(int, input("Enter the time you want to go home (hour minute second): ").split())
if home_hour >= 24:
    print("Please enter a valid value for hour")
    exit()
elif home_minute >= 60:
    print("Please enter a valid value for minute")
    exit()
elif home_second >= 60:
    print("Please enter a valid value for second")
    exit()


# Calculate the target time
home_time = time_now.replace(hour=home_hour, minute=home_minute, second=home_second, microsecond=0)

def countdown():
    while True:
        # Calculate the remaining time
        time_now = datetime.now()
        time_left = home_time - time_now

        # Break the loop if time is up
        if time_left.total_seconds() <= 0:
            print("\nHeimat :-)")
            break

        # Extract hours, minutes, and seconds
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Print the remaining time
        print(f"\rTid til hjem :-( : {hours:02}h:{minutes:02}m:{seconds:02}s", end="")

        # Wait for 1 second
        time.sleep(1)

print()
countdown()
