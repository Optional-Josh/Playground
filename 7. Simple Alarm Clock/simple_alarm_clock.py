import time
from datetime import datetime


def alarm_clock():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60):
            raise ValueError
    except ValueError:
        print("Invalid time format. Please enter time as HH:MM in 24-hour format.")
        return

    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Wake up! It's time!")
            break

        time.sleep(1)

alarm_clock()