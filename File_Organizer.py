import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox


# Function to organize files by extension
def organize_by_extension(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The specified folder does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        file_extension = file.split('.')[-1] if '.' in file else 'no_extension'
        directory = os.path.join(folder_path, file_extension.upper())

        if not os.path.exists(directory):
            os.makedirs(directory)

        shutil.move(os.path.join(folder_path, file), os.path.join(directory, file))

    messagebox.showinfo("Success", "Files have been organized by extension.")


# Function to organize files by creation date
def organize_by_date(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The specified folder does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        # Get the last modified time of the file
        modified_time = os.path.getmtime(os.path.join(folder_path, file))
        date_folder = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d')
        directory = os.path.join(folder_path, date_folder)

        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Move the file into the corresponding directory
        shutil.move(os.path.join(folder_path, file), os.path.join(directory, file))

    messagebox.showinfo("Success", "Files have been organized by date.")


# Function to organize files by size
def organize_by_size(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The specified folder does not exist.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        file_path = os.path.join(folder_path, file)
        file_size = os.path.getsize(file_path)

        if file_size < 1 * 1024 * 1024:  # Less than 1 MB
            directory = os.path.join(folder_path, 'Small')
        elif 1 * 1024 * 1024 <= file_size < 10 * 1024 * 1024:  # Between 1 MB and 10 MB
            directory = os.path.join(folder_path, 'Medium')
        else:  # Larger than 10 MB
            directory = os.path.join(folder_path, 'Large')

        if not os.path.exists(directory):
            os.makedirs(directory)

        shutil.move(file_path, os.path.join(directory, file))

    messagebox.showinfo("Success", "Files have been organized by size.")


# Function to choose folder using file dialog
def choose_folder():
    folder_path = filedialog.askdirectory()
    return folder_path


# Function to start the organizing process based on method
def start_organizing(method):
    folder_path = choose_folder()
    if folder_path:
        if method == 'extension':
            organize_by_extension(folder_path)
        elif method == 'date':
            organize_by_date(folder_path)
        elif method == 'size':
            organize_by_size(folder_path)
        else:
            messagebox.showerror("Error", "Invalid method selected.")


# Main function to create GUI
def main():
    # Create the main window
    window = tk.Tk()
    window.title("File Organizer")
    window.geometry("400x300")
    window.config(bg="#f0f8ff")

    # Title label
    title_label = tk.Label(window, text="File Organizer", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#4682b4")
    title_label.pack(pady=10)

    # Subtitle label
    subtitle_label = tk.Label(window, text="Organize your files by extension, date, or size", font=("Helvetica", 12),
                              bg="#f0f8ff", fg="#4682b4")
    subtitle_label.pack(pady=5)

    # Buttons with styling
    button_style = {
        "font": ("Helvetica", 14),
        "bg": "#4682b4",
        "fg": "white",
        "activebackground": "#5a9bd5",
        "activeforeground": "white",
        "relief": "raised",
        "bd": 2,
        "width": 20
    }

    tk.Button(window, text="Organize by Extension", command=lambda: start_organizing('extension'), **button_style).pack(
        pady=5)
    tk.Button(window, text="Organize by Date", command=lambda: start_organizing('date'), **button_style).pack(pady=5)
    tk.Button(window, text="Organize by Size", command=lambda: start_organizing('size'), **button_style).pack(pady=5)

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()
