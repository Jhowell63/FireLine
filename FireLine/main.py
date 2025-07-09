from tkinter import *
from logIn import LoginScreen


def launch_app():
    # Initialize window
    window = Tk()
    window.title("FireLine")
    window.geometry("1200x800")

    # Convert image to photo image
    logo_path = 'photos/FireLine.png'
    icon = PhotoImage(file=logo_path)
    window.iconphoto(True, icon)

    # Change background color
    window.configure(bg='#E6E6E6')

    # Load in logIn
    login = LoginScreen(window)
    login.pack(fill="both", expand=True)

    # Set up window
    window.mainloop()

if __name__ == "__main__":
    launch_app()