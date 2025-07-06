"""
File: roadcraft_save_backup.py
Author: Leilacchi
Date: 04-07-2025 (d/m/Y)
Version: 1.0
Description: Makes a backup of the user directory of the game RoadCraft, including config and save files.
"""

from zipfile import ZipFile, ZIP_DEFLATED
import os, time, shutil

# initialising variables
zip_name = 'roadcraft-' + time.strftime("%Y%m%d-%H%M%S") + '.zip'
save_path = os.getenv('LOCALAPPDATA') + r'\Saber\RoadCraftGame\storage\steam\user'
save_destination = os.getenv('USERPROFILE') + r'\RoadCraft Save Backups'

# folder check
if not os.path.exists(save_destination):
    os.makedirs(save_destination)
    print('Folder "RoadCraft Save Backups" successfully created in ' + os.getenv('USERPROFILE'))

# make zip file
try:
    with ZipFile(zip_name, "w", ZIP_DEFLATED) as zip_output:
        for root_folder, sub_folders, files in os.walk(save_path):
            for file in files:
                full_path = os.path.join(root_folder, file)
                zip_output.write(full_path, arcname = os.path.relpath(full_path, save_path))

    # report results
    print('File ' + zip_name + ' was successfully created.')
except:
    print('Failed to create ' + zip_name)

zip_output.close()

# move zip file to desired location
shutil.move(zip_name, save_destination)
print('Moved ' + zip_name + ' to ' + save_destination)
