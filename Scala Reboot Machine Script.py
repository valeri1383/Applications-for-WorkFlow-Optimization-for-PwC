import os
import datetime
import time
import sys
import subprocess

import now


def create_task(task_name, executable_path):
    # Command to create a task in Task Scheduler using schtasks
    command = f"schtasks /create /tn \"{task_name}\" /tr \"{executable_path}\" /sc onlogon /rl highest /f"

    # Run the command using subprocess
    subprocess.run(command, shell=True)


# Example usage:
task_name = "StartMyProgram"
executable_path = r"C:\Users\vvasilev005\Desktop\test.exe"

create_task(task_name, executable_path)
def reboot():
    print("Rebooting the PC...")
    os.system("shutdown /r /t 1")  # Command to reboot the PC

def schedule_reboot(hour):
    print(f"Reboot scheduled every Monday at {hour}")
    while True:
        now = datetime.datetime.now()
        if now.weekday() == 3 and now.strftime("%H:%M") == hour:  # currently is Thursday for testing
            reboot()
        time.sleep(60)  # Check every minute


def reverse_counter(reboot_time, reboot_weekday):
    try:
        target_hour, target_minute = map(int, reboot_time.split(":"))
    except ValueError:
        print("Invalid time format. Please use HH:MM (24-hour format).")
        return

    # Validate target_hour and target_minute
    if not (0 <= target_hour < 24 and 0 <= target_minute < 60):
        print("Invalid time. Please enter a valid time in HH:MM format.")
        return

    # Validate the reboot_weekday
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if reboot_weekday.capitalize() not in weekdays:
        print("Invalid weekday. Please enter a valid day of the week (e.g., Monday, Tuesday, etc.).")
        return

    # Get the current date
    current_date = datetime.date.today()

    # Find the next occurrence of the specified weekday
    target_date = current_date + datetime.timedelta((weekdays.index(reboot_weekday.capitalize()) - current_date.weekday() + 7) % 7)

    # Create the target datetime
    target_datetime = datetime.datetime.combine(target_date, datetime.time(target_hour, target_minute))

    current_time = datetime.datetime.now()

    if current_time >= target_datetime:
        print(f"The next {reboot_weekday.capitalize()} at {reboot_time} has already passed.")
        return

    print(f"Counting down to the {reboot_weekday.capitalize()} at {reboot_time}\n")

    while datetime.datetime.now() < target_datetime:
        remaining_time = target_datetime - datetime.datetime.now()
        sys.stdout.write(f"\rRemaining time: {remaining_time}")
        sys.stdout.flush()
        time.sleep(1)  # Update every second

    print("\nCountdown finished. Reached the target time.")



if __name__ == "__main__":
    reboot_time = "13:00"
    reboot_weekday = "Friday"
    reverse_counter(reboot_time, reboot_weekday)

    # Schedule the reboot every Monday
    schedule_reboot(reboot_time)








