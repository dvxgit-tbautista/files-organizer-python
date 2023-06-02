import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Specify the source directory containing the files
source_dir = os.getenv('SOURCE_DIR')

# Create a list of all files in the source directory
files = os.listdir(source_dir)

# print(files)

# Create a dictionary to map file extensions to destination directories
destination_dirs = {
    '.xlsx': os.getenv('XLSX_DIR'),
    '.jpg': os.getenv('JPG_DIR'),
    '.docx': os.getenv('DOCX_DIR'),
    '.txt': os.getenv('TXT_DIR'),
    '.mp3': os.getenv('MP3_DIR'),
    '.json': os.getenv('JSON_DIR'),
}

# print(destination_dirs)

# Iterate over each file
for file in files:
    # Split the file name and its extension
    # using os.path.splitext()
    # The function returns a tuple with two elements:
    #   - The file name without the extension (ignored and assigned to _)
    #   - The file extension assigned to ext
    _, ext = os.path.splitext(file)
    # print("filename: " + _)
    # print("file extension: " + ext)

    # Check if the extension exists in the destination directories
    if ext in destination_dirs:
        # Create the destination directory if it doesn't exist
        os.makedirs(destination_dirs[ext], exist_ok=True)

        # Move the file to the destination directory
        try:
            shutil.move(os.path.join(source_dir, file),
                        os.path.join(destination_dirs[ext], file))
            print(f"Moved '{file}' to '{destination_dirs[ext]}' successfully.")
        except Exception as e:
            print(f"Failed to move '{file}': {str(e)}")
