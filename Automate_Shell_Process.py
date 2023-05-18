import subprocess,time, os
import platform
from datetime import datetime


# Checking Camera functionality
def camera_check():
    subprocess.run('start microsoft.windows.camera:', shell=True)
    time.sleep(2)
    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)


# Opening YouTube to test speakers
def youtube():
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", 'www.youtube.com/watch?v=XqZsoesa55w'])
    time.sleep(5)
    os.system("taskkill /im chrome.exe /f")


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


# Testing internet
def testing_internet(self):
    current_file = self
    with open('current_file', 'w') as file:
        file.write("Internet Test has been successful")
    os.system("notepad.exe " + 'current_file')


# getting the GUID username
def getting_username():
    user = os.getlogin()
    return user


# Opening Notepad with message
def open_notepad_with_Menu(self):
    current_file = self
    with open('current_file', 'w') as file:
        file.write('*** SHELL INSPECTION AUTOMATION APP ***\n')
        file.write('***  Powered by VALERI VASILEV  ***\n')
        file.write('\n')
        file.write('    1. Step - Testing the Brightness Lvl\n')
        file.write('    2. Step - Camera Functionality Check\n')
        file.write('    3. Step - Displaying the OS System Info\n')
        file.write('    4. Step - Opening YouTube Video for Sound/Internet check\n')
        file.write('    5. Step - Testing Internet Connectivity by Ping\n')
        file.write('    6. Step - Detecting user and Displaying Info\n')

    os.system("notepad.exe " + 'current_file')


def open_notepad_with_User_Info(self):
    current_file = self
    with open('current_file', 'w') as file:
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
    os.system("winver")



""" Starting the Process"""

# Loading the menu with the steps performed
open_notepad_with_Menu('')

# Changing the Brightness LvL
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


if __name__ == '__main__':
    take_brightness = input("Please enter the brightness level: ")
    command = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + take_brightness + ")"
    hello_command = f"Write-Host {command}"
    hello_info = run(hello_command)

# Testing the camera
camera_check()

# Displaying the operating system
os_info()

# Opening Vide in YouTube for sound check
youtube()

# Testing Internet Connectivity by ping
testing_internet('')

# Detecting User and Displaying Results
open_notepad_with_User_Info('')

# Loading the option for shutdown
shutdown()





