import csv
import datetime
import os
import platform
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from datetime import *
import time



# creating source
source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\\")


# creating target folder
destination_folder = os.path.join(os.environ["USERPROFILE"], "Documents\Backup Files from Desktop\\")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)





def moving_files_by_extensions_or_folders_names():
    def submit_response():
        user_response = entry.get()
        files = os.listdir(source_folder)
        file_extension = user_response

        # Filter files by extension
        filtered_files = [file for file in files if file.endswith(file_extension)]

        # Move filtered files to the destination directory
        for file in filtered_files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)

        messagebox.showwarning('Your Request has been done', 'All Done.')
        root.destroy()

    root = tk.Tk()
    root.geometry('500x150')
    root.deiconify()
    root.configure(bg='light cyan')
    root.title('Please select File Extension or Folder name')

    # Create a label for the question
    question_label = tk.Label(root, bg='light cyan', text="What type of files (extensions) or Folders would you like to Move/Copy: ")
    question_label.pack(anchor="center")

    # Create an entry field for user input
    entry = tk.Entry(root)
    entry.pack()

    # Create a button to submit the response
    submit_button = tk.Button(root, text="Submit", command=submit_response)
    submit_button.pack()

    root.mainloop()


def copy_files_by_extension_and_folders_by_name():
    def submit_response():
        user_response = entry.get()

        # Get a list of all files in the source directory
        files = os.listdir(source_folder)
        file_extension = user_response

        # Filter files by extension
        filtered_files = [file for file in files if file.endswith(file_extension)]

        # Copy filtered files and folders to the destination directory
        for file in filtered_files:
            file_path = os.path.join(os.environ["USERPROFILE"], f"Desktop\\{file}")
            if os.path.isdir(file_path):
                source = source_folder + file
                destination = destination_folder + file
                shutil.copytree(source, destination)
            else:
                source_path = os.path.join(source_folder, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.copy(source_path, destination_path)

        messagebox.showwarning('Your Request has been done', 'All Done.')
        root.destroy()

    root = tk.Tk()
    root.geometry('500x150')
    root.deiconify()
    root.configure(bg='light cyan')
    root.title('Please select File Extension or Folder name')

    # Create a label for the question
    question_label = tk.Label(root, bg='light cyan', text="What type of files (extensions) or Folders would you like to Move/Copy: ")
    question_label.pack(anchor="center")

    # Create an entry field for user input
    entry = tk.Entry(root)
    entry.pack()

    # Create a button to submit the response
    submit_button = tk.Button(root, text="Submit", command=submit_response)
    submit_button.pack()

    root.mainloop()


def move_all_files_and_folders():
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move files and folders
        shutil.move(source, destination)

    messagebox.showwarning('ALL FILES AND FOLDERS HAS BEEN MOVED', 'ALL FILES AND FOLDERS HAS BEEN MOVED.')


def copy_all_files_and_folders():
    for file_name in os.listdir(source_folder):
        # construct full file path
        file_path = os.path.join(os.environ["USERPROFILE"], f"Desktop\\{file_name}")
        if os.path.isdir(file_path):
            source = source_folder + file_name
            destination = destination_folder + file_name
            shutil.copytree(source, destination)
        else:
            source = source_folder + file_name
            destination = destination_folder + file_name
            # copy only files
            shutil.copy(source, destination)

    # end message here
    messagebox.showwarning('ALL FILES AND FOLDERS HAS BEEN COPIED', 'ALL FILES AND FOLDERS HAS BEEN COPIED.')



def listing_files_from_desktop():
    window = tk.Tk()
    window.geometry("300x700")
    window.configure(bg='misty rose',border=5)
    window.title('Files on the Desktop')

    # Create a list of element texts
    source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\\")
    element_texts = os.listdir(source_folder)


    def create_elements_with_delay():
        for i, text in enumerate(element_texts):
            element = tk.Label(window,fg='navy', bg='misty rose', text=text)
            element.pack()
            window.update()
            time.sleep(0.2)

        window.destroy()

    create_elements_with_delay()
    window.mainloop()


def custom_message_box(text):
    def close_window():
        win.destroy()

    win = Tk()
    win.geometry("500x300")

    w = Label(win, text='\nMOVING FILES and FOLDERS', font="130", fg="Navyblue")
    w.pack()

    msg = Message(win, text=f"\n\nPowered by VALERI VASILEV.\n\n\n{text}", font=85, fg='Dodger blue',
                  width=300, justify='center', borderwidth=3)
    msg.pack()
    win.after(1500, close_window)
    win.mainloop()
    time.sleep(0.5)




# Main Menu
def option_selected(option):


    # Move Files by extension or Folders by name
    if option[-1] == '1':
        moving_files_by_extensions_or_folders_names()

    # Move all Files and Folders
    elif option[-1] == '2':
        move_all_files_and_folders()

    #  Copy files by extension and Folders by name
    elif option[-1] == '3':
        copy_files_by_extension_and_folders_by_name()

    # Copy all Files and Folders
    elif option[-1] == '4':
        copy_all_files_and_folders()

    # Exit
    elif option[-1] == '5':
        window.destroy()






"""        Main Functionality      """

# Welcome message
custom_message_box('***     Welcome     ***')

# Listing all elements from the Desktop
listing_files_from_desktop()
time.sleep(1)


# Create the main menu window
window = tk.Tk()
window.geometry("500x400")
window.configure(bg='misty rose')
window.title('Moving Files and Objects with Graphic Interface')

# Define the options with descriptions
options = [
    {"name": "Option 1", "description": "1. Move Files by extension or Folders by name"},
    {"name": "Option 2", "description": "2. Move all Files and Folders"},
    {"name": "Option 3", "description": "3. Copy files by extension and Folders by name"},
    {"name": "Option 4", "description": "4. Copy all Files and Folders"},
    {"name": "Option 5", "description": "5. Exit"}
]

# Create and position the buttons with descriptions
for option in options:
    label = tk.Label(window,bg='misty rose',fg='blue', text=option["description"], font=85)
    label.pack()
    window.update()
    time.sleep(0.4)
    button = tk.Button(window,bg='khaki', padx=50, pady=10, text=option["name"], command=lambda option=option: option_selected(option["name"]))
    button.pack()
    window.update()
    time.sleep(0.4)



# Start the main event loop
window.mainloop()

custom_message_box('***     Goodbye!     ***')
time.sleep(1)


""" Writting to CSV file"""
def getting_username():
    user = os.getlogin()
    return user

def get_current_time():
    time = datetime.now().strftime('%Y-%m-%d')
    return time

def asset_check():
    my_system = platform.uname()
    system = my_system.system
    asset = my_system.node
    return asset


def writting_to_CSV_file():
    with open(r"\\pwcglb.com\gb\PCmover_Data\A. Tech Support Tools\Valeri\Moving_Coping_Files_and_Folders\Users_Moved_Data.csv",'a', newline='') as csvfile:
        fieldnames = ['Date', 'User', 'Asset N']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        time_data_moved = get_current_time()
        user = getting_username()
        asset = asset_check()

        info = {f'Date': time_data_moved,
                f'User': user,
                f'Asset N': asset}

        writer.writerow(info)


writting_to_CSV_file()