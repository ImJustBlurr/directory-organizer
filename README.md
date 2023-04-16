# Directory Organizer

This program allows you to sort files in a given directory into subfolders based on file type. The user can select a folder to sort and choose which file types to organize.

## Requirements

- [Python 3.x](https://www.python.org/downloads/)
- tkinter (included standard in python)
- shutil (included standard in python)

## Usage

1. Run the program into the command window (usually by typing `python main.py`). Make sure you are operating within the programs directory.
2. Click the "Browse" button to select a folder to sort
3. Check the checkboxes for the file types you want to sort
4. Click the "Sort" button to sort the files
5. The files will be sorted into subfolders in the original directory

## Functions

The following functions are defined in the script:

- **`handleFiles(folder_name, filename)`**: This function handles the sorting of a file into a subdirectory. It takes two arguments: folder_name is the name of the subdirectory to create or move the file to, and filename is the name of the file to move. The function first checks if the subdirectory already exists, and creates it if it doesn't. It then moves the file from its current location to the new subdirectory.
- **`browse_folder()`**: This function handles the selection of a folder to sort. It opens a file dialog window for the user to select a folder, and inserts the selected folder path into the folder_entry widget.
- **`sort_files()`**: This function handles the sorting of files in the selected folder. It iterates over every file in the selected folder and checks its file extension against the selected file types. If a file matches a selected file type, it is sorted into the appropriate subdirectory using the handleFiles function.

## File Types

Currently, these are the supported file types that can be sorted:

- **Images**: png, jpg, gif
- **Documents**: docx, pdf, txt
- **Applications**: url, lnk

You can, of course, go in and alter the code to handle the specific file types you would like to sort.

## License

This project is licensed under the [MIT License](https://mit-license.org/).
