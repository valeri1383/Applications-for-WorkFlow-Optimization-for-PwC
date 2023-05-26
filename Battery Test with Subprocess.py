import subprocess, os


command = 'WMIC PATH Win32_Battery Get EstimatedChargeRemaining, BatteryStatus'
output = subprocess.check_output(command, shell=True).decode('utf-8')
result = f"Battery status on: {output[59:61]}%"

def open_notepad_with_Menu(self):
    current_file = self
    with open('current_file', 'w') as file:
        file.write(result)
    os.system("notepad.exe " + 'current_file')
open_notepad_with_Menu('')