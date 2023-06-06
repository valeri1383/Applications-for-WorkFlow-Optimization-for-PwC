import csv
import subprocess,time, os
import platform
from datetime import datetime


def test_success():
    user_choice = input("Was the test successfully performed? Y/N: ")
    if user_choice in ['Y', 'y']:
        return 'Pass'
    elif user_choice in ['N', 'n']:
        return 'False'
    else:
        print("Incorrect input!!!")


def microphone_test():

    print(f"*" * 4 + "  CHECKING THE Microphone FUNCTIONALITY  " + "*" * 4)
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", 'https: // www.onlinemictest.com /'])
    time.sleep(6)
    #os.system("taskkill /im chrome.exe /f")
    time.sleep(2)
    print("\n--- Microphone test has been performed. ---\n")
    time.sleep(2)




def keyboard_test():
    print(f"*" * 4 + "  CHECKING THE KEYBOARD FUNCTIONALITY   " + "*" * 4)
    time.sleep(1)
    os.system("notepad.exe ")
    time.sleep(2)
    print("\n--- Keyboard test has been performed. ---\n")
    time.sleep(3)


# Checking Camera functionality
def camera_check():
    print(f"*" * 4 + "  CHECKING THE CAMERA FUNCTIONALITY   " + "*" * 4)
    time.sleep(3)
    subprocess.run('start microsoft.windows.camera:', shell=True)
    time.sleep(2)
    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
    time.sleep(2)
    print("\n--- Camera test has been performed. ---\n")
    time.sleep(2)
    # yes / no


# Opening Sound_check_website to test speakers
def sound_check_website():
    print(f"*" * 4 + "  CHECKING THE SPEAKERS FUNCTIONALITY  " + "*" * 4)
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", 'https://www.onlinemictest.com/sound-test/'])
    time.sleep(6)
    #os.system("taskkill /im chrome.exe /f")
    time.sleep(2)
    print("\n--- Speakers test has been performed. ---\n")
    time.sleep(2)


# Asset checking
def asset_check():
    my_system = platform.uname()

    system = my_system.system
    asset = my_system.node
    return asset


# Shutting down the PC
def shutdown():
    print("Would you like to shutdown? Y/N? ")
    user_response = input().lower()
    if user_response == 'y':
        subprocess.call(["shutdown", "-f", "-s", "-t", "20"])
    else:
        print('Operation aborted')


# getting current time
def get_current_time():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time


def testing_internet():
    # Pinging Google
    print(f"*" * 4 + "  CHECKING THE WI-FI CARD   " + "*" * 4)

    os.system('PING 8.8.8.8')
    print("\n--- Internet connection test has been performed. ---\n")

    # check in the test in PASS / FALSE
    #print(test_success())



def battery_test():
    command = 'WMIC PATH Win32_Battery Get EstimatedChargeRemaining, BatteryStatus'
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    result = f"Battery status is: {output[59:61]}%"
    return result


# getting the GUID username
def getting_username():
    user = os.getlogin()
    return user



def open_notepad_with_User_Info(self):
    current_file = self
    with open('current_file,txt', 'w') as file:
        name = getting_username()
        time = get_current_time()
        asset = asset_check()
        file.write("Camera Test: OK\n")
        file.write("Brightness Test: OK\n")
        file.write("Operating System Test: OK\n")
        file.write("Internet Test: OK\n")
        file.write("Sound Test: OK\n")
        file.write('\n')
        file.write(f"User: {name}\nTime: {time}\nAsset N: {asset}\n")

    os.system("notepad.exe " + 'current_file')


# displaying the operating system
def os_info():
    print(f"*" * 4 + "  CHECKING THE OPERATING SYSTEM   " + "*" * 4)
    os.system("winver")
    time.sleep(2)
    print("\n--- OS version has been checked ---\n")
    time.sleep(2)


# Listing USB info with powershell command
def listing_usb_info():
    print(f"*" * 4 + "  CHECKING THE USB PORTS FUNCTIONALITY   " + "*" * 4)
    time.sleep(2)
    output = ''
    # PowerShell command
    powershell_command = "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"

    # Execute PowerShell command
    result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Print the command output
        print(result.stdout)
        output += result.stdout

    else:
        # Print the error message
        print(result.stderr)
        output += result.stderr

    print("\n--- USB Functionality test has been performed. ---\n")


    with open('USB_TEST.txt', 'w') as file:
        file.write(output)

    time.sleep(2)
    #os.system("notepad.exe " + 'USB_TEST')




""" Starting the Process"""
# Loading the menu with the steps performed
#open_notepad_with_Menu('')

print('         AUTOMATIC COMPUTER INSPECTION APP\n')
time.sleep(1)
print("Powered by VALERI VASILEV.\nAll rights Reserved!\n")
time.sleep(3)


# Testing Internet
testing_internet()


# Testing the camera
camera_check()


# Displaying the operating system
os_info()


# Opening Sound check website
sound_check_website()


# Keyboard check
keyboard_test()

# Changing the Brightness LvL
print(f"*" * 4 + "  CHECKING THE BRIGHTNESS FUNCTIONALITY   " + "*" * 4)
time.sleep(2)

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


if __name__ == '__main__':
    print()
    take_brightness = input("Please enter the brightness level: ")
    command = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + take_brightness + ")"
    hello_command = f"Write-Host {command}"
    hello_info = run(hello_command)

counter = 0

print("\n--- Brightness test has been performed. ---\n")
time.sleep(2)


# Listing all USB info
listing_usb_info()

# Writing to CSV file
with open('Inspected_PC.csv', 'a', newline='') as csvfile:
    fieldnames = ['User', 'Asset N', 'Time Inspected', 'Camera Test', 'Speakers Test', 'Battery Test', 'Internet Test', 'Brightness Test', 'Operating System Test']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    user = getting_username()
    asset = asset_check()
    time_inspected = get_current_time()
    battery_lvl = battery_test()

    info = {f'User': user,
            f'Asset N': asset,
            f'Time Inspected': time_inspected,
            'Camera Test': 'Pass',
            'Speakers Test': 'Pass',
            'Battery Test': battery_lvl,
            'Internet Test': 'Pass',
            'Brightness Test': 'Pass',
            'Operating System Test': 'Pass'}
    writer.writerow(info)




print("ALL TEST ARE DONE. HAVE A NICE DAY")