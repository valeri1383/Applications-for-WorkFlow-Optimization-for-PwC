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


# Changing the Brithness LvL
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

if __name__ == '__main__':
    take_brightness = input("Please enter the brightness level: ")
    command = "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + take_brightness + ")"
    hello_command = f"Write-Host {command}"
    hello_info = run(hello_command)


# Asset checking
def asset_check():
    my_system = platform.uname()

    system = f"System: {my_system.system}"
    asset = f"Asset Num: {my_system.node}"

    with open('asset_info.txt', 'w') as file:
        file.write(f'{system}\n{asset}')


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
    print(time)


# Testing internet
def testing_internet():
    args = ["ping", "www.google.com"]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    data = process.communicate()
    print(data)
    with open('internet_Response.txt', 'w') as file:
        file.write(f'{data}')


# getting the GUID username
def getting_username():
    user = os.getlogin()
    print(user)


# Opening Notepad with message
def open_notepad_with_message(self):
    current_file = self
    with open('current_file', 'w') as file:
        file.write('Hi how are you')
    os.system("notepad.exe " + 'current_file')


# displaying the operating system
def os_info():
    os.system("winver")




""" Starting the Process"""
