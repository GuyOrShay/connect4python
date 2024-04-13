from tkinter import Frame, Button, simpledialog, messagebox, Toplevel
from app_styles import setup_styles
from app_const import WINDOW_SIZE
import board


def show_home_screen(
    window, start_game_callback, start_bot_game_callback, start_online_game_callback
):
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

    Button(
        frame,
        text="Play vs Bot",
        font=styles["fontLarge"],
        bg=styles["buttonColor"],
        fg=styles["buttonFgColor"],
        command=lambda: play_vs_bot(start_bot_game_callback),
    ).grid(row=1, column=0, sticky="ew", padx=50)
    Button(
        frame,
        text="Play 2 Players on this Computer",
        font=styles["fontLarge"],
        bg=styles["buttonColor"],
        fg=styles["buttonFgColor"],
        command=lambda: play_local_multiplayer(start_game_callback),
    ).grid(row=2, column=0, sticky="ew", padx=50, pady=10)
    Button(
        frame,
        text="Play 2 Players over IP",
        font=styles["fontLarge"],
        bg=styles["buttonColor"],
        fg=styles["buttonFgColor"],
        command=lambda: play_over_ip(start_online_game_callback),
    ).grid(row=3, column=0, sticky="ew", padx=50)


def setup_game(window):
    size = simpledialog.askinteger(
        "Board Size", "Enter the board size (4-10):", minvalue=4, maxvalue=10
    )
    if not size:
        messagebox.showerror("Error", "Board size is required to start the game.")
        return

    board.create_game_board(size, window)


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()
    window.configure(bg=setup_styles()["bgColor"])


def play_vs_bot(start_bot_game_callback):
    size = simpledialog.askinteger(
        "Board Size", "Enter the board size (4-10):", minvalue=4, maxvalue=10
    )
    if size:
        start_bot_game_callback(size)


def play_local_multiplayer(start_game_callback):
    size = simpledialog.askinteger(
        "Board Size", "Enter the board size (4-10):", minvalue=4, maxvalue=10
    )
    if size:
        start_game_callback(size)


def play_over_ip(start_online_game_callback):
    isHost = messagebox.askyesno(
        "Connect Four over IP", "Do you want to host the game?"
    )
    if isHost:
        size = simpledialog.askinteger(
            "Board Size", "Enter the board size (4-10):", minvalue=4, maxvalue=10
        )
        if size:
            start_online_game_callback(isHost, size, 0, 0)
    else:
        client_address = simpledialog.askstring(
            "Connect Four over IP",
            "Enter the host address in the format ip:port",
            initialvalue="127.0.0.1:4000",
        )
        ip, port = client_address.split(":")
        port = int(port)
        if client_address:
            start_online_game_callback(False, 0, ip, port)
