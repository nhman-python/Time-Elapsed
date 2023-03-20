import datetime
import pytz
import time
import os


# Prompt the user to enter the target date and time
while True:
    target_str = input("Enter the target date and time in the format 'YYYY-MM-DD HH:MM:SS': ")
    try:
        target_date = datetime.datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
        break
    except ValueError as e:
        print(f"Please enter a date and time in the format 'YYYY-MM-DD HH:MM:SS'. \nERROR: {e}")

# Convert the input string to a datetime object in the local timezone
target_date = pytz.timezone('UTC').localize(target_date)

# Calculate the time difference between now and the target date
while True:
    delta = datetime.datetime.now(pytz.utc) - target_date

    # Extract the difference in years, months, days, hours, minutes, and seconds
    total_seconds = delta.total_seconds()
    years, seconds = divmod(int(total_seconds), 31536000)
    months, seconds = divmod(seconds, 2629800)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # Print the remaining time
    print(f"Time left until {target_date}: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")

    # If the target date has been reached, break out of the loop
    if delta.total_seconds() <= 0:
        break

    # Wait for 1 second before checking the time again
    time.sleep(1)
    os.system('clear')