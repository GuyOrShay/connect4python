from tkinter import Frame, Button, Label
from app_styles import setup_styles
from app_const import WINDOW_SIZE

def show_home_screen(window):
    styles = setup_styles()
    clear_window(window)

    window.geometry(WINDOW_SIZE)  # Adjust the size as per your requirement
    # Ensure the window can expand and the widgets within it can too
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Central frame to hold the buttons
    frame = Frame(window, bg=styles["bgColor"])
    frame.grid(row=0, column=0, sticky="nsew")

    # Make the frame adjust to the window size
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Buttons
    Button(frame, text="Play vs Bot", font=styles["fontLarge"], bg=styles["buttonColor"], fg=styles["buttonFgColor"], command=play_vs_bot).grid(row=1, column=0, sticky="ew", padx=50)
    Button(frame, text="Play 2 Players on this Computer", font=styles["fontLarge"], bg=styles["buttonColor"], fg=styles["buttonFgColor"], command=play_local_multiplayer).grid(row=2, column=0, sticky="ew", padx=50, pady=10)
    Button(frame, text="Play 2 Players over IP", font=styles["fontLarge"], bg=styles["buttonColor"], fg=styles["buttonFgColor"], command=play_over_ip).grid(row=3, column=0, sticky="ew", padx=50)

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.configure(bg=setup_styles()["bgColor"])

# Placeholder functions for button commands
def play_vs_bot():
    print("Playing vs Bot...")  # Replace with actual function

def play_local_multiplayer():
    print("Playing Local Multiplayer...")  # Replace with actual function

def play_over_ip():
    print("Playing over IP...")  # Replace with actual function
