import time

def time_conversion(time, utc):
    time_int = int(time)
    days_passed = time_int // 86400
    seconds_today = time_int % 86400
    hours_today = seconds_today // 3600
    seconds_passed_current_hour = seconds_today % 3600
    minutes_passed_current_hour = seconds_passed_current_hour // 60
    seconds_passed_current_minute = seconds_passed_current_hour % 60

    print(f"The time is {hours_today + utc}:{minutes_passed_current_hour}:{seconds_passed_current_minute} and {days_passed} days have passed since the Enoch time!")

time_conversion(time.time(), -3)