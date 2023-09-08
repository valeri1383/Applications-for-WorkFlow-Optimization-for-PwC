import shutil
import subprocess
import time
import keyboard as kb
from pathlib import Path


def formating_the_drive():
    subprocess.run(["powershell", "Start-Process", "cmd.exe", "-verb", "RunAs"])
    time.sleep(1)

    # 1
    kb.write('diskpart')
    kb.press('enter')

    # 2
    kb.write('list disk')
    kb.press('enter')

    # 3
    kb.write('select disk 1')
    kb.press('enter')

    # 4
    kb.write('clean')
    kb.press('enter')

    # 5
    kb.write('create partition primary size=32700')
    kb.press('enter')

    # 6
    kb.write('select partition 1')
    kb.press('enter')

    # 7
    kb.write('active')
    kb.press('enter')

    # 8
    kb.write('format fs=fat32 quick')
    kb.press('enter')

    # 9
    kb.write('assign')
    kb.press('enter')

    # 10
    kb.write('exit')
    kb.press('enter')

    kb.write('exit')
    kb.press('enter')


formating_the_drive()

time.sleep(2)


source_folder = Path("C:\\Users\Administrator\Desktop\\UK-Prod-WIN11-22H2-Aug23")

destination_folder_d = Path("D:\\")
destination_folder_e = Path("E:\\")

if destination_folder_d.exists():
    destination_folder = destination_folder_d
else:
    print("Destination folder on drive D: does not exist. Using drive E: instead.")
    destination_folder = destination_folder_e

def copy_with_progress(source, destination):
    total_items = sum(1 for _ in source.glob('**/*'))  # Count total items to copy
    copied_items = 0

    for item in source.iterdir():
        destination_item = destination / item.name

        try:
            if item.is_file():
                shutil.copy2(item, destination_item)
            elif item.is_dir():
                shutil.copytree(item, destination_item)

            copied_items += 1
            progress = (copied_items / total_items) * 100
            print(f"Progress: {progress:.2f}% ({copied_items}/{total_items})")

        except Exception as e:
            print(f"Error copying {item}: {e}")

source_folder = Path("C:\\Users\\Administrator\\Desktop\\UK-Prod-WIN11-22H2-Aug23")

# Check if the destination folder on drive D: exists
destination_folder_d = Path("D:\\")
destination_folder_e = Path("E:\\")

if destination_folder_d.exists():
    destination_folder = destination_folder_d
else:
    print("Destination folder on drive D: does not exist. Using drive E: instead.")
    destination_folder = destination_folder_e

copy_with_progress(source_folder, destination_folder)
