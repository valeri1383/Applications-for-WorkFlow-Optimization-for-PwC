import os
import subprocess
import keyboard as kb
from pynput.keyboard import Key, Controller
import time
import tkinter as tk
from tkinter import *

#password = input('Password: ')

def open_cmd_as_thycotic_admin(password):
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(0.3)
    keyboard.type("cmd")
    time.sleep(1)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    kb.write(password)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)


def run_cmd_commands():
    keyboard = Controller()

    # Disable Protectors
    kb.write('Manage-bde -protectors -Disable C: -RebootCount 0')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    # Activate Protectors
    kb.write(' Manage-bde -Protectors -Enable C:')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # GPupdate force
    kb.write('gpupdate /force')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    os.system("taskkill /F /FI \"WINDOWTITLE eq Command Prompt\"")


def get_user_password():
    def submit_response():
        user_response = entry.get()
        open_cmd_as_thycotic_admin(user_response)
        run_cmd_commands()
        root.destroy()

    root = tk.Tk()
    root.geometry('400x200')
    root.deiconify()
    root.configure(bg='peachpuff2')
    root.title('Password Window')

    # Create a label for the question
    question_label = Label(root, bg='peachpuff2', font=("Arial", 14), text="Please enter your password here: ")
    question_label.pack(anchor="center")

    # Create an entry field for user input
    entry = tk.Entry(root,bg='azure', show='*',font=("Helvetica", 18) )
    entry.pack()

    # Create a button to submit the response
    submit_button = tk.Button(root,bg='sandy brown', font=("Helvetica", 11), text="Submit", command=submit_response)
    submit_button.pack()

    root.mainloop()

get_user_password()







