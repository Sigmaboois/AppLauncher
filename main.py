import tkinter as tk
from tkinter import filedialog
import json
import os

CONFIG_PATH = "config.json"

def load_apps():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return []

def save_apps(apps):
    with open(CONFIG_PATH, "w") as f:
        json.dump(apps, f)

def add_app():
    filepath = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if filepath and filepath not in apps:
        apps.append(filepath)
        listbox.insert(tk.END, filepath)
        save_apps(apps)

apps = load_apps()

root = tk.Tk()
root.title("App Launcher")

listbox = tk.Listbox(root, width=60)
listbox.pack(padx=10, pady=10)

for app in apps:
    listbox.insert(tk.END, app)

tk.Button(root, text="Add App", command=add_app).pack(pady=10)

root.mainloop()
