
import os

# Specify the path of the directory
directory_path = '/New folder'  # Current directory; you can change it to any path

# List all files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory was not found.")
except PermissionError:
    print("You do not have permission to access this directory.")
