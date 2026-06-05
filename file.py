import os
import shutil
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "=== FILE ORGANIZER ===")

# Folder path
path = input(Fore.YELLOW + "Enter folder path to organize: ")

# File type categories
file_types = {

    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Documents": ['.pdf', '.docx', '.txt', '.pptx'],
    "Videos": ['.mp4', '.mkv', '.avi']
}

# Organize files
for filename in os.listdir(path):

    file_path = os.path.join(path, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    extension = os.path.splitext(filename)[1].lower()

    moved = False

    # Check category
    for folder_name, extensions in file_types.items():

        if extension in extensions:

            folder_path = os.path.join(path, folder_name)

            # Create folder if not exists
            os.makedirs(folder_path, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(folder_path, filename))

            print(Fore.GREEN + f"Moved: {filename} → {folder_name}")

            moved = True
            break

    # Others folder
    if not moved:

        other_folder = os.path.join(path, "Others")

        os.makedirs(other_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(other_folder, filename))

        print(Fore.MAGENTA + f"Moved: {filename} → Others")

print(Fore.CYAN + "\nFiles Organized Successfully!")