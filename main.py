from tkinter import Tk
import login_screen
import registration_screen
import home_screen
from app_const import WINDOW_SIZE


def main():
    window = Tk()
    window.title("Login & Registration System")
    window.geometry(WINDOW_SIZE)  

    def show_login():
        login_screen.show_login_form(window, show_registration , show_registration)
    
    def show_registration():
        registration_screen.show_registration_form(window, show_login)

    def show_registration():
        home_screen.show_home_screen(window)
    
    
    show_login()  
    window.mainloop()

if __name__ == "__main__":
    main()