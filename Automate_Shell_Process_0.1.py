import csv
import subprocess,time, os
import platform
from datetime import datetime
import math
import psutil
import sounddevice as sd
import pyaudio
import wave
from tkinter import messagebox
from tkinter import *


def test_success():
    time.sleep(1)

    user_answer = messagebox.askquestion(title='RESULT FROM THE TEST',
                                         message='Was the test successfully performed?')
    time.sleep(2)
    if user_answer == 'yes':
        return 'Pass'
    return 'FALSE'


def welcome_box():
    def close_window():
        win.destroy()

    win = Tk()
    win.geometry("500x300")

    w = Label(win, text='\nAUTOMATIC COMPUTER INSPECTION APP', font="130", fg="Navyblue")
    w.pack()

    msg = Message(win, text="\n\nPowered by VALERI VASILEV.\nAll rights Reserved!\n\nWelcome!", font=85, fg='Dodger blue',
                  width=300, justify='center', borderwidth=3)
    msg.pack()
    win.after(3000, close_window)
    win.mainloop()
    time.sleep(1)


def operation_end_notification(msg):
    def close_window():
        win.destroy()

    win = Tk()
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 6 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(350, 300, x, y))
    win.deiconify()
    win.configure(bg='cadetblue1')


    msg = Message(win, text=f"\n\n\n{msg}", font=75, fg='blue',
                  width=200, justify='center', bg='cadetblue1')
    msg.pack()
    win.after(2000, close_window)
    win.mainloop()




def current_operation_notification(msg):
    def close_window():
        win.destroy()

    win = Tk()
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 6 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(350, 300, x, y))
    win.deiconify()
    win.configure(bg='lavender blush')

    w = Label(win, text='\nCurrent Test Running: ', font="60", fg="maroon1", bg='lavender blush')
    w.pack()
    msg = Message(win, text=f"\n{msg}", font=55, fg='light slate blue',
                  width=200, justify='center', borderwidth=3, bg='lavender blush')
    msg.pack()
    win.after(3000, close_window)
    win.mainloop()



def changing_color_of_console(color):
    os.system(color)



def microphone_test():

    #print(f"*" * 4 + "  CHECKING THE Microphone FUNCTIONALITY  " + "*" * 4)
    #print()
    time.sleep(1)
    current_operation_notification('CHECKING THE MICROPHONE FUNCTIONALITY')
    # Set the audio settings
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set up the microphone stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    #print("Recording...\n")
    messagebox.showwarning("MICROPHONE RECORDING", "Microphone Recording is about to start !!! ")

    frames = []

    # Record audio from the microphone
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    messagebox.showwarning("MICROPHONE RECORDING", "Microphone Recording is finished ! ")

    # Stop the stream and close PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    os.startfile("output.wav")
    time.sleep(5)
    #print("\n--- Microphone test has been performed. ---\n")
    operation_end_notification('MICROPHONE Test\n\n has been performed!')
    time.sleep(1)
    mic_test = test_success()
    return mic_test


def keyboard_test():
    #print(f"*" * 4 + "  CHECKING THE KEYBOARD FUNCTIONALITY   " + "*" * 4)
    #print()
    current_operation_notification('CHECKING THE KEYBOARD FUNCTIONALITY')
    time.sleep(1)
    os.system("notepad.exe ")
    time.sleep(2)
    #print("\n--- Keyboard test has been performed. ---\n")
    operation_end_notification('KEYBOARD Test\n\n has been performed!')
    time.sleep(1)
    keyboard_test = test_success()
    return keyboard_test


# Checking Camera functionality
def camera_check():
    #print(f"*" * 4 + "  CHECKING THE CAMERA FUNCTIONALITY   " + "*" * 4)
    #print()
    current_operation_notification('CHECKING THE CAMERA FUNCTIONALITY')
    time.sleep(2)
    subprocess.run('start microsoft.windows.camera:', shell=True)
    time.sleep(2)
    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
    time.sleep(2)
    #print("\n--- Camera test has been performed. ---\n")
    operation_end_notification('CAMERA Test\n\n has been performed!')
    time.sleep(1)
    camera_test = test_success()
    return camera_test


# Opening Sound_check_website to test speakers
def sound_check_website():
    #print(f"*" * 4 + "  CHECKING THE SPEAKERS FUNCTIONALITY  " + "*" * 4)
    current_operation_notification('CHECKING THE SPEAKERS FUNCTIONALITY')
    sd.default.device = None
    sd.default.samplerate = samplerate = 48000

    duration = 1.5
    volume = 0.3
    frequency = 440

    # fade time in seconds:
    fade_in = 0.01
    fade_out = 0.3

    buffer = memoryview(bytearray(int(duration * samplerate) * 4)).cast('f')

    for i in range(len(buffer)):
        buffer[i] = volume * math.cos(2 * math.pi * frequency * i / samplerate)

    fade_in_samples = int(fade_in * samplerate)
    for i in range(fade_in_samples):
        buffer[i] *= i / fade_in_samples

    fade_out_samples = int(fade_out * samplerate)
    for i in range(fade_out_samples):
        buffer[-(i + 1)] *= i / fade_out_samples

    for mapping in ([1], [2], [1, 2]):
        sd.play(buffer, blocking=True, mapping=mapping)
        sd.sleep(500)

    time.sleep(1)
    #print("\n--- Speakers test has been performed. ---\n")
    operation_end_notification('SPEAKERS Test\n\n has been performed!')
    time.sleep(1)
    speakers = test_success()
    return speakers

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
    #print(f"*" * 4 + "  CHECKING THE WI-FI CARD   " + "*" * 4)
    current_operation_notification('CHECKING THE WI-FI CARD')
    time.sleep(2)
    os.system('PING 8.8.8.8')
    #print("\n--- Internet connection test has been performed. ---\n")
    time.sleep(1)
    operation_end_notification('WI-FI CARD Test\n\n has been performed!')

    # check in the test in PASS / FALSE
    internet_connection = test_success()
    return internet_connection



def battery_test():
    battery = psutil.sensors_battery()

    if battery is None:
        print("Battery information not available.")
    else:
        plugged = battery.power_plugged
        percent = battery.percent
        result = f"Plugged in: {'Yes' if plugged else 'No'} | Remaining: {percent}%"
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
    #print(f"*" * 4 + "  CHECKING THE OPERATING SYSTEM   " + "*" * 4)
    current_operation_notification('CHECKING THE OPERATING SYSTEM')
    os.system("winver")
    time.sleep(2)
    #print("\n--- OS version has been checked ---\n")
    operation_end_notification('OS Version\n\n has been checked!')
    time.sleep(2)
    os_test = test_success()
    return os_test


# Listing USB info with powershell command
def listing_usb_info():
    #print(f"*" * 4 + "  CHECKING THE USB PORTS FUNCTIONALITY   " + "*" * 4)
    current_operation_notification('CHECKING THE USB PORTS FUNCTIONALITY')
    time.sleep(1)
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

    #print("\n--- USB Functionality test has been performed. ---\n")
    operation_end_notification('USB Functionality test\n\n has been performed!')


    with open('USB_TEST.txt', 'w') as file:
        file.write(output)

    time.sleep(2)
    usb_test = test_success()
    return usb_test
    #os.system("notepad.exe " + 'USB_TEST')




""" Starting the Process"""
# Loading the menu with the steps performed

welcome_box()

changing_color_of_console("color E1")
"""print()
print('         AUTOMATIC COMPUTER INSPECTION APP\n')
time.sleep(1)
print("Powered by VALERI VASILEV.\nAll rights Reserved!\n")
time.sleep(3)"""


# Testing Internet
internet_test = testing_internet()


# Testing the camera
camera_test = camera_check()


# Displaying the operating system
os_test = os_info()


# Opening Sound check website
speakers_test = sound_check_website()

# Microphone test
mic_test = microphone_test()

# Keyboard check
keyboard_test = keyboard_test()



# Changing the Brightness LvL
#print(f"*" * 4 + "  CHECKING THE BRIGHTNESS FUNCTIONALITY   " + "*" * 4)
current_operation_notification('CHECKING THE BRIGHTNESS FUNCTIONALITY')
time.sleep(1)

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

#print("\n--- Brightness test has been performed. ---\n")
operation_end_notification('BRIGHTNESS Test\n\n has been performed!')
time.sleep(1)

brightness_test = test_success()


# Listing all USB info
usb_test = listing_usb_info()

# Writing to CSV file
with open('Inspected_PC.csv', 'a', newline='') as csvfile:
    fieldnames = ['User', 'Asset N', 'Time Inspected', 'Network Card test', 'Camera Test',
                  'Operating System Test', 'Speakers Test', 'Microphone Test', 'Battery Test',
                  'Keyboard Test', 'Brightness Test', 'USB Ports test']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    user = getting_username()
    asset = asset_check()
    time_inspected = get_current_time()
    battery_lvl = battery_test()

    info = {f'User': user,
            f'Asset N': asset,
            f'Time Inspected': time_inspected,
            'Network Card test': internet_test,
            'Camera Test': camera_test,
            'Operating System Test': os_test,
            'Speakers Test': speakers_test,
            'Microphone Test': mic_test,
            'Battery Test': battery_lvl,
            'Keyboard Test': keyboard_test,
            'Brightness Test': brightness_test,
            'USB Ports test': usb_test
            }
    writer.writerow(info)

print()
#print('*' * 4 +"    ALL TEST ARE DONE. HAVE A NICE DAY  " + '*' * 4)
current_operation_notification('ALL TEST ARE DONE. HAVE A NICE DAY')

time.sleep(2)