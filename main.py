import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk

# file extensions
imageExt = ['.jpg', '.png', '.gif']
docExt = ['.pdf', '.docx', '.txt']
appExt = ['.url', '.lnk']

# Create a Tkinter window
window = tk.Tk()
window.title("Directory Organizer")

# Define the functions for handling files and the "Browse" and "Sort" buttons
def handleFiles(folder_name, filename):
    desired_directory = os.path.join(folder_entry.get(), folder_name)

    if not os.path.exists(desired_directory): # Check if the new directory already exists
        os.mkdir(desired_directory) # Create the new directory if it doesn't exist
        print('Created:', desired_directory)

    #Define the source path of the file
    source_path = os.path.join(folder_entry.get(), filename)
    # Define the destination path of the file
    destination_path = os.path.join(folder_entry.get(), folder_name, filename)
    # Move the file to the new directory
    shutil.move(source_path, destination_path)
    print('Moved:', filename, 'into', folder_name)

def browse_folder(): # function to handle selecting the browse button
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def sort_files(): # function to handle selecting the sort button
    directory = folder_entry.get()

    # Iterate over every file in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)): # Check if the file is a file (not a directory)
            extension = os.path.splitext(filename)[1]
            if images.get() and (extension in imageExt): #handles if the images checkbox is checked and the current file is an image
                handleFiles('Images', filename)

            if docs.get() and (extension in docExt): #handles if the docs checkbox is checked and the current file is an doc
                handleFiles('Docs', filename)

            if applications.get() and  (extension in appExt): #handles if the app checkbox is checked and the current file is an app
                handleFiles('Applications', filename)

    tk.messagebox.showinfo("Directory Organizer", "Files sorted successfully!\nYou can find your files sorted into their designated folders!")

# Create the GUI widgets
style = ttk.Style()

style.configure('TLabel', font=('Helvetica', 11))
style.configure('TButton', font=('Helvetica', 11))
style.configure('TEntry', font=('Helvetica', 11))

folder_label = ttk.Label(window, text="Select folder to sort:")
folder_entry = ttk.Entry(window)
browse_button = ttk.Button(window, text="Browse", command=browse_folder)
sort_button = ttk.Button(window, text="Sort", command=sort_files)

docs = tk.BooleanVar()
docsButton = tk.Checkbutton(window, text="Documents (.docx, .pdf, .txt)", variable=docs)
images = tk.BooleanVar()
imagesButton = tk.Checkbutton(window, text="Images (.jpg, .png, .gif)", variable=images)
applications = tk.BooleanVar()
appButton = tk.Checkbutton(window, text="Applications", variable=applications)

# Position the widgets on the window
folder_label.grid(row=0, column=0, padx=10, pady=10)
folder_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button.grid(row=0, column=2, padx=10, pady=10)
sort_button.grid(row=2, column=1, padx=10, pady=10)
docsButton.grid(row=1, column=0, padx=10, pady=10)
imagesButton.grid(row=1, column=1, padx=10, pady=10)
appButton.grid(row=1, column=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
