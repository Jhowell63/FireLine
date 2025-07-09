import tkinter as tk
from PIL import Image, ImageTk
from scheduler import SchedulerScreen


class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Bind Enter key
        master.bind('<Return>', self.enter_key_pressed)

        # Add Logo
        logo_path = 'photos/FireLine.png'
        logo_img = Image.open(logo_path)
        # Resize proportionally (optional: max width/height)
        max_width = 800
        max_height = 240

        w, h = logo_img.size
        scale = min(max_width / w, max_height / h)
        new_size = (int(w * scale), int(h * scale))

        logo_img = logo_img.resize(new_size, Image.Resampling.LANCZOS)
        self.fireLine_logo = ImageTk.PhotoImage(logo_img)

        tk.Label(self, image=self.fireLine_logo).pack(pady=10)



        # Username label and input
        tk.Label(self, text="Username").pack(pady=10)
        self.username = tk.Entry(self, width=30)
        self.username.pack()

        # Password label and input
        tk.Label(self, text="Password").pack(pady=10)
        self.password = tk.Entry(self, show="*", width=30)
        self.password.pack()

        # Login button
        tk.Button(self, text="Login", command=self.login_user).pack(pady=20)

        tk.Label(self, text="Username = admin \n Password = password", font=("Segoe UI", 16)).pack(pady=20)
    

    def login_user(self):
        username = self.username.get()
        password = self.password.get()

        if username == "admin" and password == "password":
            # Destroy the login screen and show the scheduler screen
            self.destroy()
            scheduler = SchedulerScreen(self.master)
            scheduler.pack(fill="both", expand=True)
        else:
            print("Login failed. Please try again.")
            self.username.delete(0, tk.END)
            self.password.delete(0, tk.END)

    def enter_key_pressed(self, event):
        # Trigger the login function when Enter is pressed
        self.login_user()

