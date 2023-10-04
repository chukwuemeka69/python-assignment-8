#! /usr/bin/python3
import os
import shutil

def copy_files_with_extension(src_dir, dest_dir, extension):
    """
    Copy files with the specified extension from src_dir to dest_dir.
    
    Parameters:
    - src_dir: The source directory from which to copy files.
    - dest_dir: The destination directory where the files should be copied.
    - extension: The file extension to look for.
    """
    
    # Check if the source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist!")
        return
    
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Iterate through each file in the source directory
    for filename in os.listdir(src_dir):
        # If the file has the desired extension
        if filename.endswith(extension):
            # Construct full file paths for source and destination
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            
            # Copy the file from the source to destination
            shutil.copy(src_path, dest_path)
            print(f"Copied {filename} to {dest_dir}")


if __name__ == '__main__':
    # Prompt the user for input values
    src_directory = input("Enter the source directory path: ")
    dest_directory = input("Enter the destination directory path: ")
    file_extension = input("Enter the file extension (e.g., .txt): ")

    # Call the function with the provided input values
    copy_files_with_extension(src_directory, dest_directory, file_extension)

