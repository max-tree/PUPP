'''
General Functions
Maxwell Tree
Creation date: Sep 30, 2026

This file is for generic functions that will be used throughout PUPP
'''

import tkinter as tk
from tkinter import filedialog, messagebox


def get_files(type="TXT"):
    # Hide the root Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Ask user to select multiple files
    files = filedialog.askopenfiles(
        title="Select " + type + " files",
        filetypes=[(type + " files", "*." + type)])

    return files