import os
import tkinter as tk
import win32com.client
import time
from tkinter import messagebox
from tkinter import *
import subprocess
from gtts import gTTS



def devices_checked():
    window = tk.Tk()
    window.geometry("300x700")
    window.configure(bg='snow',border=5)
    window.title('Scanning all devices')

    normal_devices =  check_all_devices_status()[0]


    def create_elements_with_delay():
        for i, text in enumerate(normal_devices):
            element = tk.Label(window,fg='black', bg='snow', text=text)
            element.pack()
            window.update()
            time.sleep(0.025)

        window.destroy()

    create_elements_with_delay()
    window.mainloop()


def writting_to_text_file():
    with open('device_status.txt', 'w') as file:
        problem_devices = check_all_devices_status()[1]
        if len(problem_devices) > 0:
            file.write('Devices NOT running properly:\n')
            file.write('\n')
            for device in problem_devices:
                file.write(f'{device}\n')

            file.write('\n')
        else:
            file.write('All Devices are functioning properly\n')


def custom_message_box(text):
    def close_window():
        win.destroy()

    win = Tk()
    win.geometry("700x500")

    w = Label(win, text='\nDevices NOT running properly:', font="130", fg="red")
    w.pack()

    msg = Message(win, text=f"\n\n\n\n\n{text}", font=70, fg='black',
                  width=500, justify='center', borderwidth=20)
    msg.pack()
    #win.after(1500, close_window)
    win.mainloop()
    time.sleep(1)


def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='en')  # 'en' specifies English language
    tts.save(output_file)


def close_windows_media_player():
    # Use the taskkill command to forcefully terminate Windows Media Player process
    subprocess.run(["taskkill", "/f", "/im", "wmplayer.exe"], shell=True)


def get_device_status(device):
    if device.Status == 'OK':
        return "Running Normally"
    else:
        return "Not Running Normally"


def check_all_devices_status():
    wmi = win32com.client.GetObject("winmgmts:")
    devices = wmi.ExecQuery("SELECT * FROM Win32_PnPEntity")
    #default_devices =

    normal_devices = []
    problem_devices = []

    for device in devices:
        device_name = device.Caption
        device_status = get_device_status(device)

        if device_status == "Running Normally" or \
                device_name == 'PANGP Virtual Ethernet Adapter Secure' or \
                device_name == 'Intel® Smart Sound Technology for USB Audio' or \
                device_name == 'PANGP Virtual Ethernet Adapter':
            normal_devices.append(device_name)
        else:
            problem_devices.append(device_name)


    print("Devices Running Normally:")
    for device in normal_devices:
        print(device)

    print("\nDevices Not Running Normally:")
    for device in problem_devices:
        print(device)

    return normal_devices, problem_devices


def main():
    print("Checking All Devices Status:\n")
    check_all_devices_status()


writting_to_text_file()

devices_checked()


# trowing the message box
problem_devices = check_all_devices_status()[1]
updated_devices = [x for x in problem_devices]
if len(updated_devices) > 0:
    input_text_2 = "You have driver which is not functioning properly."
    output_filename = "output.mp3"
    text_to_speech(input_text_2, output_filename)
    os.system(f"start {output_filename}")
    time.sleep(4)
    close_windows_media_player()
    messagebox.showwarning('Warning', 'There are devices who are Not running properly')

formatted_output = '\n'.join(updated_devices)

if len(updated_devices) > 0:
    custom_message_box(formatted_output)
else:
    input_text = "All your drivers are functioning normally."
    output_filename = "output.mp3"

    text_to_speech(input_text, output_filename)

    os.system(f"start {output_filename}")
    time.sleep(4)
    close_windows_media_player()
    messagebox.showinfo('Devices / Drivers function normally', 'All Devices / Drivers are functioning normally')

#os.startfile('device_status.txt')

main()