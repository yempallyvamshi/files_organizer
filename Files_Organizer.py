import os
import shutil


def organize_files(directory):
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Get the file extension
        file_extension = os.path.splitext(file)[1][1:]  # Remove the dot from the extension

        # Skip if the file has no extension
        if not file_extension:
            continue

        # Create a folder for the extension if it doesn't exist
        folder_path = os.path.join(directory, file_extension)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Move the file to the corresponding folder
        shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))

    print("Files organized successfully!")


if __name__ == "__main__":
    # Specify the directory you want to organize
    directory_to_organize = r"C:\Users\Vamshi Yempally\Downloads"

    # Call the function to organize files
    organize_files(directory_to_organize)