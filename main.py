import logging
import threading
import os
import json
import tkinter as tk
from tkinter import filedialog
from qobuz_dl.core import QobuzDL

logging.basicConfig(level=logging.INFO)

with open("config.json", "r") as f:
    data = json.load(f)


def download(url):
    qobuz.handle_url(url)

def open_directory():
    os.startfile(directory_var.get())

def start_downloading():
    qobuz.directory = directory_var.get()
    urls = url_entries.get("1.0", tk.END).split("\n")
    threads = [threading.Thread(target=download, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_var.set(directory)


def clear_urls():
    url_entries.delete("1.0", tk.END)


def paste_urls():
    try:
        clipboard_content = root.clipboard_get()
        url_entries.insert(tk.END, clipboard_content)
    except tk.TclError:
        pass


qobuz = QobuzDL(quality=27)
default_directory = data.get(
    "default_directory", os.path.join(os.path.expanduser("~"), "Music")
)

# GUI
root = tk.Tk()
root.title("Qobuz Downloader")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

url_label = tk.Label(frame, text="Enter URLs (one per line):")
url_label.grid(row=0, column=0, sticky="w")

url_entries = tk.Text(frame, width=80, height=10)
url_entries.grid(row=1, column=0, columnspan=2)

start_button = tk.Button(frame, text="Start Downloading", command=start_downloading)
start_button.grid(row=2, column=1, sticky="e", pady=5)

directory_label = tk.Label(frame, text="Download Directory:")
directory_label.grid(row=3, column=0, sticky="w", pady=5)

directory_var = tk.StringVar()
directory_var.set(default_directory)

directory_entry = tk.Entry(frame, width=80, textvariable=directory_var)
directory_entry.grid(row=4, column=0, sticky="w")


clear_button = tk.Button(frame, text="Clear entries", command=clear_urls)
clear_button.grid(row=2, column=0, sticky="w", pady=5)

paste_button = tk.Button(frame, text="Paste from clipboard", command=paste_urls)
paste_button.grid(row=2, column=0, padx=(80, 0), sticky="w", pady=5)

browse_button = tk.Button(frame, text="Browse directory", command=browse_directory)
browse_button.grid(row=4, column=0, sticky='e', pady=5)

open_directory_button = tk.Button(frame, text="Open download directory", command=open_directory)
open_directory_button.grid(row=4, column=1, sticky='w', pady=5)

# login
qobuz.get_tokens()
qobuz.initialize_client(
    "antwuan@meantodeal.com", "antwuan@A1", qobuz.app_id, qobuz.secrets
)

root.mainloop()

# Save the default directory to the configuration file
data["default_directory"] = directory_var.get()
with open("config.json", "w") as f:
    json.dump(data, f)
