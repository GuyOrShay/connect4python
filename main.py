from tkinter import Tk
import login_screen
import registration_screen

def main():
    window = Tk()
    window.title("Login & Registration System")
    window.geometry("350x250")  # Adjust as needed

    def show_login():
        login_screen.show_login_form(window, show_registration)
    
    def show_registration():
        registration_screen.show_registration_form(window, show_login)

    show_login()  # Show the login form initially
    window.mainloop()

if __name__ == "__main__":
    main()