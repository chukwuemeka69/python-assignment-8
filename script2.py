#! /usr/bin/python3

import os

# Get the list of all files and directories in the current working directory
items = os.listdir()

# Separate them into files and directories
files = [item for item in items if os.path.isfile(item)]
directories = [item for item in items if os.path.isdir(item)]

# Print the names of files
print("Files:")
for file in files:
    print(file)

# Print the names of directories
print("\nDirectories:")
for directory in directories:
    print(directory)

