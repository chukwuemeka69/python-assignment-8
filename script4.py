#! /usr/bin/python3

# Get filenames from the user
source_file = input("Enter the name of the source file (e.g., input.txt): ")
destination_file = input("Enter the name of the destination file (e.g., output.txt): ")

# Read from source file and write to destination file
try:
    with open(source_file, 'r') as infile:
        content = infile.read()

        with open(destination_file, 'w') as outfile:
            outfile.write(content)

    print(f"Content has been copied from '{source_file}' to '{destination_file}'.")
except FileNotFoundError:
    print(f"Error: '{source_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

