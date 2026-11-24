import tkinter as tk
from .nav import Navigation
from tkinter import messagebox as mbox

class MainContent:

    def __init__(self, username):
        self.window = tk.Tk()
        self.window.title("Vehicle Rental Management System")
        self.window.geometry("1300x700")
        self.window.configure(bg="white")

        # Navbar
        self.navbar_frame = tk.Frame(
            self.window,
            bg="#0097B2",
            height=70
        )
        self.navbar_frame.pack(fill="x")
        self.navbar_frame.pack_propagate(False)

        self.title_label = tk.Label(
            self.navbar_frame,
            text="Vehicle Rental Management System",
            bg="#0097B2",
            fg="white",
            font=("Verdana", 20, "bold")
        )
        self.title_label.pack(side="left", padx=40)

        tk.Label(
            self.navbar_frame,
            text=f"Welcome {username} (Admin)",
            bg="#0097B2",
            fg="white",
            font=("Verdana", 12, "bold")
        ).pack(side="right", padx=40)

        # Application body
        self.body = tk.Frame(self.window, bg="white")
        self.body.pack(fill="both", expand=True)

        # Main content area
        self.main_content = tk.Frame(self.body, bg="white")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Navigation
        self.navigation = Navigation(
            self.body,
            self.main_content,
            self.update_title
        )

        self.navigation.show_page("dashboard")

    # Update navbar title
    def update_title(self, page_name):
        title = (
            "Vehicle Rental Management System"
            if page_name == "dashboard"
            else ("Manage Vehicles" if page_name == "vehicles" else (
                "Manage Users" if page_name == "users" else (
                    "Rent and Return Vehicle" if page_name == "rent and return" else "Rent History"
                )
            ))
        )

        self.title_label.config(text=title)

    def run(self):
        self.window.mainloop()