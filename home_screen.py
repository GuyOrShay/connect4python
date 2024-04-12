from tkinter import Frame, Button, simpledialog, messagebox, Toplevel
from app_styles import setup_styles
from app_const import WINDOW_SIZE
import board

def show_home_screen(window ,start_game_callback):
    styles = setup_styles()
    clear_window(window)

    window.geometry(WINDOW_SIZE)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    frame = Frame(window, bg=styles["bgColor"])
    frame.grid(row=0, column=0, sticky="nsew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    Button(frame, text="Play vs Bot", font=styles["fontLarge"], bg=styles["buttonColor"], fg=styles["buttonFgColor"], command=play_vs_bot).grid(row=1, column=0, sticky="ew", padx=50)
    Button(frame, text="Play 2 Players on this Computer", font=styles["fontLarge"], bg=styles["buttonColor"], fg=styles["buttonFgColor"], command=lambda: play_local_multiplayer(window, start_game_callback)).grid(row=2, column=0, sticky="ew", padx=50, pady=10)
    Button(frame, text="Play 2 Players over IP", font=styles["fontLarge"], bg=styles["buttonColor"], fg=styles["buttonFgColor"], command=play_over_ip).grid(row=3, column=0, sticky="ew", padx=50)


def setup_game(window):
    size = simpledialog.askinteger("Board Size", "Enter the board size (4-10):", minvalue=4, maxvalue=10)
    if not size:
        messagebox.showerror("Error", "Board size is required to start the game.")
        return

    board.create_game_board(size, window)

def start_game(size, window):
    print(f"Starting game with board size: {size}")

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.configure(bg=setup_styles()["bgColor"])

def play_vs_bot():
    print("Playing vs Bot...")  # Replace with actual function

def play_local_multiplayer(window,start_game_callback):
    size = simpledialog.askinteger("Board Size", "Enter the board size (4-10):", minvalue=4, maxvalue=10)
    if size:
        start_game_callback(size)
        
def play_over_ip():
    print("Playing over IP...")  # Replace with actual function
