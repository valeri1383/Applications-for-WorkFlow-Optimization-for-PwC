import os
import subprocess
import keyboard as kb
from pynput.keyboard import Key, Controller
import time

password = input('passwprd: ')

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



open_cmd_as_thycotic_admin(password)
run_cmd_commands()





