# gui/components.py
import tkinter as tk


def create_label(parent, text, row, column, pady=10, padx=10):
    label = tk.Label(parent, text=text)
    label.grid(row=row, column=column, pady=pady, padx=padx)
    return label


def create_entry(parent, row, column, show=None, pady=10, padx=10):
    entry = tk.Entry(parent, show=show)
    entry.grid(row=row, column=column, pady=pady, padx=padx)
    return entry


def create_button(parent, text, command, row, column, pady=10, padx=10):
    button = tk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, pady=pady, padx=padx)
    return button
