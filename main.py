from tkinter import Tk
import database
import gui

# def main():
#     database.init_db()
#     window = Tk()
#     window.title("Login & Registration System")
#     gui.show_login_form(window)
#     window.mainloop()

def main():
    database.init_db()
    window = Tk()
    window.title("Login & Registration System")
    styles = gui.setup_styles()
    gui.show_login_form(window, styles)
    window.mainloop()

if __name__ == "__main__":
    main()