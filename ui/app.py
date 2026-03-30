import customtkinter as ctk
from database import initialize_database

# Set the appearance of the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CookbookApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("My Cookbook")
        self.geometry("1000x700")
        self.minsize(800, 600)

        # Initialize the database when the app starts
        initialize_database()

        # Configure the layout grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

    def run(self):
        self.mainloop()