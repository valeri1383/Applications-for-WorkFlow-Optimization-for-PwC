import os
import shutil


source_folder = os.path.join(os.environ["USERPROFILE"], "Desktop\Test_folder\\")

destination_folder = os.path.join(os.environ["USERPROFILE"], "Documents\Test_folder\\")

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files

    shutil.move(source, destination)
    print('Moved:', file_name)