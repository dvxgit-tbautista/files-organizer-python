# files-organizer-python
A simple Python script for automating file organization based on file extensions.

## Prerequisites

- Python 3.11
- `dotenv` package (install using `pip install python-dotenv`)

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/files-organizer-python.git`
2. Navigate to the project directory: `cd files-organizer-python`
3. Install the required packages: `pip install -r requirements.txt`
4. Create a `.env` file in the project directory and specify the destination directories for each file extension:
5. Run the script: `python index.py`

## How It Works

1. The script reads the source directory containing the files.
2. It creates a list of all files in the source directory.
3. A dictionary maps file extensions to destination directories.
4. For each file, it checks if the extension exists in the destination directories.
5. If a matching destination directory is found, it creates the directory if it doesn't exist.
6. The file is then moved to the respective destination directory.

Please note that you can customize the source directory and destination directories by modifying the variables in the script.

Feel free to adapt the script to fit your specific file organization needs!



