import requests
import logging
import threading
import os
import json
import tkinter as tk
from tkinter import filedialog
from qobuz_dl.core import QobuzDL

# Set up logging
logging.basicConfig(level=logging.INFO)

# Fetch configuration data
data = requests.get("https://owenwijaya22.github.io/qobuz_config/config.json").json()
email = data["email"]
password = data["password"]

# Initialize QobuzDL
qobuz = QobuzDL(quality=27)
qobuz.get_tokens()
qobuz.initialize_client(
    email, password, qobuz.app_id, qobuz.secrets
)

# Define directory operations
def open_directory():
    os.startfile(directory_var.get())

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_var.set(directory)
        with open("dir.json", "w") as f:
            json.dump({"default_directory": directory}, f)

# Define download operations
def download(url):
    qobuz.handle_url(url)

def start_downloading():
    qobuz.directory = directory_var.get()
    urls = url_entries.get("1.0", tk.END).split("\n")
    threads = [threading.Thread(target=download, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

# Define URL entry operations
def clear_urls():
    url_entries.delete("1.0", tk.END)

def paste_urls():
    try:
        clipboard_content = root.clipboard_get()
        url_entries.insert(tk.END, clipboard_content + "\n")
    except tk.TclError:
        pass

# Load the default directory from the configuration file
if os.path.isfile("dir.json"):
    with open("dir.json", "r") as f:
        default_directory = json.load(f)["default_directory"]
else:
    default_directory = os.path.join(os.path.expanduser("~"), "Music")
    with open("dir.json", "w") as f:
        json.dump({"default_directory": default_directory}, f)

# Set up GUI
root = tk.Tk()
root.title("Qobuz Downloader")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# URL entry setup
url_label = tk.Label(frame, text="Enter URLs (one per line):")
url_label.grid(row=0, column=0, sticky="w")

url_entries = tk.Text(frame, width=80, height=10, undo=True)
url_entries.grid(row=1, column=0, columnspan=2)

# Button setup
start_button = tk.Button(frame, text="Start Downloading", command=start_downloading)
start_button.grid(row=2, column=1, sticky="e", pady=5)

clear_button = tk.Button(frame, text="Clear entries", command=clear_urls)
clear_button.grid(row=2, column=0, sticky="w", pady=5)

paste_button = tk.Button(frame, text="Paste from clipboard", command=paste_urls)
paste_button.grid(row=2, column=0, padx=(80, 0), sticky="w", pady=5)

browse_button = tk.Button(frame, text="Browse directory", command=browse_directory)
browse_button.grid(row=4, column=0, sticky='e', pady=5)

open_directory_button = tk.Button(frame, text="Open download directory", command=open_directory)
open_directory_button.grid(row=4, column=1, sticky='w', pady=5)

# Download directory setup
directory_label = tk.Label(frame, text="Download Directory:")
directory_label.grid(row=3, column=0, sticky="w", pady=5)

directory_var = tk.StringVar()
directory_var.set(default_directory)

directory_entry = tk.Entry(frame, width=80, textvariable=directory_var)
directory_entry.grid(row=4, column=0, sticky="w")

root.mainloop()
