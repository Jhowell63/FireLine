from tkinter import *

class SchedulerScreen(Frame):
    def __init__(self, master):
        super().__init__(master)

        # Center the scheduler screen (optional)
        self.place(relx=0.5, rely=0.5, anchor="center")

        # Placeholder content
        Label(self, text="Great Things To Come!", font=("Segoe UI", 16)).pack(pady=50)
