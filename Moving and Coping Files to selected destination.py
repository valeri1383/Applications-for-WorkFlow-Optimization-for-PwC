import csv
import time
from datetime import datetime
import os
import shutil
import platform

# creating source
source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\\")


# creating target folder
destination_folder = os.path.join(os.environ["USERPROFILE"], "Documents\Backup Files from Desktop\\")
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


def move_files_by_extension_and_folders_by_name():
    # Get a list of all files in the source directory
    files = os.listdir(source_folder)
    file_extension = input("What type of Files (extensions) or Folders would you like to move: ")

    # Filter files by extension
    filtered_files = [file for file in files if file.endswith(file_extension)]

    # Move filtered files to the destination directory
    for file in filtered_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
    time.sleep(1.5)
    print('\nAll done.')


# move all files and folders
def move_all_files_and_folders():
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move files and folders
        shutil.move(source, destination)
    time.sleep(1.5)
    print('\nAll done.')


def list_all_files():
    files = os.listdir(source_folder)
    print(" All Available files: ")
    for x in files:
        time.sleep(0.3)
        print(f"    - {x}")
    print()
    time.sleep(2)


def copy_all_files_from_desktop():
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
    time.sleep(1.5)
    print('\nAll done.')



def copy_file_by_extention_and_folders_by_name():
    # Get a list of all files in the source directory
    files = os.listdir(source_folder)
    file_extension = input("What type of files (extensions) or Folders would you like to copy: ")

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
    time.sleep(1.5)
    print('\nAll done!')


# getting the GUID username
def getting_username():
    user = os.getlogin()
    return user

# getting current time
def get_current_time():
    time = datetime.now().strftime('%Y-%m-%d')
    return time

# Asset checking
def asset_check():
    my_system = platform.uname()

    system = my_system.system
    asset = my_system.node
    return asset



with open('Users Moved Data.csv', 'a', newline='') as csvfile:
    fieldnames = ['Date', 'User', 'Asset N']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    user = getting_username()
    asset = asset_check()
    time_data_moved = get_current_time()

    info = {f'Date': time_data_moved,
            f'User': user,
            f'Asset N': asset}
    writer.writerow(info)




def menu():
    os.system('color B0')
    user_choice = 1
    while True:

        if user_choice == 5:
            break

        print()
        print('*' * 4 +' MOVING and COPING App ' + '*' * 4 + '\n')
        time.sleep(2)
        print("Powered by Valeri Vasilev\n")
        time.sleep(2)
        options = ["    1. Move Files by extension or Folders by name\n"  # done
                   "    2. Move all Files and Folders\n"  # to be tested extra
                   "    3. Copy files by extension and Folders by name\n"  # done
                   "    4. Copy all Files and Folders\n"      # done
                   "    5. Exit\n"]

        for x in options:
            print(x)


        time.sleep(2)
        user_choice = int(input("-- What would you like to do? "))
        print()

        if user_choice in [1, 2, 3, 4]:
            list_all_files()

        if user_choice == 1:
            move_files_by_extension_and_folders_by_name()
        elif user_choice == 2:
            move_all_files_and_folders()
        elif user_choice == 3:
            copy_file_by_extention_and_folders_by_name()
        elif user_choice == 4:
            copy_all_files_from_desktop()
        elif user_choice == 5:
            print("Exiting... Have a nice day!")
            break
        else:
            print("Wrong choice option selected!!! Please try again.\n")

        user_select = input("\nWould you like to continue? Y/N: ").lower()
        if user_select == 'n':
            print("\nExiting... Have a nice day!")
            break


menu()