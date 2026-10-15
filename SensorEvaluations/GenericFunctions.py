'''
General Functions
Maxwell Tree
Creation date: Sep 30, 2026

This file is for generic functions that will be used throughout PUPP
'''

import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt


def get_files(type="TXT"):
    # Hide the root Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Ask user to select multiple files
    files = filedialog.askopenfiles(
        title="Select " + type + " files",
        filetypes=[(type + " files", "*." + type)])

    return files


def create_xy_scatter_plot(x, y, xLabel, yLabel, figTitle):
    plt.figure(figTitle)
    plt.title(figTitle)
    plt.scatter(x, y, c='k', marker='o')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    return


def create_xy_plot(x, y, xLabel, yLabel, figTitle):
    plt.figure(figTitle)
    plt.title(figTitle)
    plt.plot(x, y, color='k')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    return
