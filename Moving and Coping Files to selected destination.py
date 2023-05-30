import os
import shutil

# creating source and target folders
source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\Source_folder\\")
destination_folder = os.path.join(os.environ["USERPROFILE"], "Documents\Target_folder\\")


def move_files_by_extention():
    # Get a list of all files in the source directory
    files = os.listdir(source_folder)
    file_extension = input("What type of files (extensions) would you like to move: ")

    # Filter files by extension
    filtered_files = [file for file in files if file.endswith(file_extension)]

    # Move filtered files to the destination directory
    for file in filtered_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
    print('All done.')


# move all files and folders
def move_all_files_and_folders():
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move only files
        shutil.move(source, destination)
    print('All done.')


def list_all_files():
    files = os.listdir(source_folder)
    print("All Available files:")
    for x in files:
        print(f"    - {x}")
    print()


def copy_all_files_from_desktop():
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # copy only files
        shutil.copy(source, destination)
    print('All done.')



def copy_files_by_extention():
    # Get a list of all files in the source directory
    files = os.listdir(source_folder)
    file_extension = input("What type of files (extensions) would you like to copy: ")

    # Filter files by extension
    filtered_files = [file for file in files if file.endswith(file_extension)]

    # Copy filtered files to the destination directory
    for file in filtered_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.copy(source_path, destination_path)
    print('All done.')



def menu():
    print("MOVING and COPING App")
    print("Powered by Valeri Vasilev\n")
    options = ["    1. Move files by extension\n"
               "    2. Move all filed and folders\n"
               "    3. Copy files by extension\n"
               "    4. Copy all files\n"]
    for x in options:
        print(x)

    user_choice = int(input("What would you like to do? "))

    list_all_files()

    if user_choice == 1:
        move_files_by_extention()
    elif user_choice == 2:
        move_all_files_and_folders()
    elif user_choice == 3:
        copy_files_by_extention()
    elif user_choice == 4:
        copy_all_files_from_desktop()


menu()