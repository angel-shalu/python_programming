# Write a python program to print the contents of a directory using the os module
# Search online for the function which does that...

import os

# Specify the directory (you can change this to any path you like)
directory_path = '.'

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")


