#Organizing the files in a specific folder

import os
import shutil

def organize_files(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)

    # Iterate through all files
    for file in files:
        # Get full file path
        file_path = os.path.join(folder_path, file)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
        
        # Extract file extension
        _, extension = os.path.splitext(file)
        
        # Remove the '.' from extension
        extension = extension[1:]  # Remove the dot from extension
        
        # If extension is empty, continue
        if extension == '':
            continue
        
        # Create directory if not exists
        if not os.path.exists(os.path.join(folder_path, extension)):
            os.makedirs(os.path.join(folder_path, extension))
        
        # Move file to directory
        shutil.move(file_path, os.path.join(folder_path, extension, file))

    print("Organizing files complete!")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize: ")
    organize_files(folder_path)
