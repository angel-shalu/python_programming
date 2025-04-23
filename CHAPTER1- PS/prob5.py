# Lable the program written in problem 4 with cpmments
import os

# Select tyhe directory whose content you want to list
directory_path = '/'

# Use the os module to list the directort content
contents = os.listdir(directory_path)

for item in contents:
    print(item)