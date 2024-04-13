from tkinter import Tk
import login_screen
import registration_screen
import home_screen
import board
import bot_board
from app_const import WINDOW_SIZE


def main():
    window = Tk()
    window.title("Login & Registration System")
    window.geometry(WINDOW_SIZE)  

    def show_login():
        login_screen.show_login_form(window, show_registration , show_home)
    
    def show_registration():
        registration_screen.show_registration_form(window, show_login)

    def show_home():
        for widget in window.winfo_children():
            widget.destroy()
        home_screen.show_home_screen(window, start_game ,start_bot_game)

    def start_game(size):
        for widget in window.winfo_children():
            widget.destroy()
        board.create_game_board(size, window)
        
    def start_bot_game(size):
        for widget in window.winfo_children():
            widget.destroy()
        bot_board.create_game_board(size, window)

    
    show_login()  
    window.mainloop()

if __name__ == "__main__":
    main()