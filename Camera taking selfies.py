import pyautogui as pg #For taking screenshot
import time # For necessary delay
import subprocess, random

# Launch Windows OS Camera
subprocess.run('start microsoft.windows.camera:', shell=True)

time.sleep(2) # Required !
img=pg.screenshot() # Take screenshot using PyAutoGUI's function
time.sleep(2) # Required !
num = random.randint(1,100)
img.save(rf"\\pwcglb.com\gb\PCmover_Data\A. Tech Support Tools\Valeri\Selfie{num}.PNG") # Save image screenshot at desired location on your computer

#Close the camera
subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)