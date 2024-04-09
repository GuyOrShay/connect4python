from tkinter import *
from tkinter import messagebox, font as tkfont
import database
import sqlite3
from tkinter import Tk


def setup_styles():
    """Sets up custom styles for the application."""
    return {
        "fontLarge": tkfont.Font(family="Helvetica", size=14, weight="bold"),
        "fontInput": tkfont.Font(family="Helvetica", size=12),  # New font for input fields
        "bgColor": "#2A2D34",
        "fgColor": "#C9D1D9",
        "buttonColor": "#4E5A65",
        "buttonFgColor": "#FFFFFF",
        "entryBgColor": "#3B4048",
        "entryFgColor": "#FFFFFF",
        "entryBorderWidth": 2,  # Border width for the entry widgets
    }

def create_styled_entry(parent, styles, show=""):
    """Creates and returns a styled Entry widget."""
    return Entry(parent, font=styles["fontInput"], bg=styles["entryBgColor"], fg=styles["entryFgColor"], insertbackground=styles["entryFgColor"], bd=styles["entryBorderWidth"], show=show, relief='flat', highlightthickness=1, highlightcolor=styles["buttonColor"], highlightbackground=styles["bgColor"])


def show_registration_form(window, styles, switch_to_login):
    clear_window(window, styles)
    window.geometry("300x250")
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    
    Frame(window, bg=styles["bgColor"], height=50).grid(row=0, columnspan=2, sticky="ew")
    Label(window, text="Register", font=styles["fontLarge"], bg=styles["bgColor"], fg=styles["fgColor"]).grid(row=0, columnspan=2)
    
    Label(window, text="Username:", bg=styles["bgColor"], fg=styles["fgColor"]).grid(row=1, column=0, pady=5, sticky=E)
    Label(window, text="Password:", bg=styles["bgColor"], fg=styles["fgColor"]).grid(row=2, column=0, pady=5, sticky=E)
    
    username_entry = Entry(window, bg=styles["entryBgColor"], fg=styles["entryFgColor"], insertbackground=styles["entryFgColor"])
    password_entry = Entry(window, show="*", bg=styles["entryBgColor"], fg=styles["entryFgColor"], insertbackground=styles["entryFgColor"])
    username_entry.grid(row=1, column=1, padx=10, pady=5)
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    Button(window, text="Register", width=15, command=lambda: register(username_entry.get(), password_entry.get(), window, styles, switch_to_login), bg=styles["buttonColor"], fg=styles["buttonFgColor"]).grid(row=3, columnspan=2, pady=10)

def register(username, password, window, styles, switch_to_login):
    try:
        database.register_user(username, password)
        messagebox.showinfo("Success", "You are registered successfully.")
        switch_to_login(window, styles)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")


def show_login_form(window, styles):
    clear_window(window, styles)
    window.geometry("350x300")  # Adjusted for bigger input fields

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(4, weight=1)

    form_frame = Frame(window, bg=styles["bgColor"])
    form_frame.grid(row=1, column=1, sticky='nsew', padx=30, pady=30)
    window.grid_rowconfigure(1, weight=2)

    Label(form_frame, text="Login", font=styles["fontLarge"], bg=styles["bgColor"], fg=styles["fgColor"]).pack(anchor='center', pady=10)
    Label(form_frame, text="Username:", bg=styles["bgColor"], fg=styles["fgColor"], font=styles["fontInput"]).pack(anchor='w')

    username_entry = create_styled_entry(form_frame, styles)
    username_entry.pack(fill='x', pady=10)

    Label(form_frame, text="Password:", bg=styles["bgColor"], fg=styles["fgColor"], font=styles["fontInput"]).pack(anchor='w')
    password_entry = create_styled_entry(form_frame, styles, show="*")
    password_entry.pack(fill='x', pady=10)

    Button(form_frame, text="Login", width=15, command=lambda: login(username_entry.get(), password_entry.get(), styles), bg=styles["buttonColor"], fg=styles["buttonFgColor"]).pack(pady=10)
    Button(form_frame, text="Register", width=15, command=lambda: show_registration_form(window, styles, show_login_form), bg=styles["buttonColor"], fg=styles["buttonFgColor"]).pack()

def login(username, password, styles):
    if database.login_user(username, password):
        messagebox.showinfo("Success", "You are logged in.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

def clear_window(window, styles):
    for widget in window.winfo_children():
        widget.destroy()
    window.configure(bg=styles["bgColor"])


