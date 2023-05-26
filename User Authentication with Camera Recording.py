from tkinter import *
from functools import partial
import pyautogui as pg  # For taking screenshot
import time  # For necessary delay
import subprocess, random
from tkinter import messagebox
import os

# new user register
new_user = input('Register new user: ')

def printDetails(usernameEntry):
    usernameText = usernameEntry.get()
    print("user entered :", usernameText)

    if usernameText != new_user:
        # Launch Windows OS Camera
        subprocess.run('start microsoft.windows.camera:', shell=True)

        time.sleep(2)  # Required !
        img = pg.screenshot()  # Take screenshot using PyAutoGUI's function
        time.sleep(2)  # Required !
        num = random.randint(1, 100)

        # personal cloud folder
        #img.save( rf"\\pwcglb.com\gb\PCmover_Data\A. Tech Support Tools\Valeri\Selfie{num}.PNG")
        # desktop folder for every user
        img.save(rf"C:\Users\vvasilev005\Desktop\Selfie{num}.PNG")
        os.path.join(os.environ["USERPROFILE"], "Desktop")

        # Close the camera
        subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)

        # Displaying warning message
        top = Tk()
        top.geometry("20x20")
        messagebox.showinfo("WARNING", "Your have attempt unauthorized action!!! Your identity has been captured!")
        top.mainloop()
        return
    else:
        print('Welcome')
        return


#window
tkWindow = Tk()
tkWindow.geometry('650x200')
tkWindow.title('User Authentication')

#label
usernameLabel = Label(tkWindow, text="Enter your name here ---->  ")
#entry for user input
usernameEntry = Entry(tkWindow)

#define callable function with printDetails function and usernameEntry argument
printDetailsCallable = partial(printDetails, usernameEntry)

#submit button
submitButton = Button(tkWindow, text="Submit", command=printDetailsCallable)

#place label, entry, and button in grid
usernameLabel.grid(row=0, column=0)
usernameEntry.grid(row=0, column=1)
submitButton .grid(row=1, column=1)

#main loop
tkWindow.mainloop()


