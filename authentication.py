from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as mbox
from pages.authentication import Auth_Page

# App Palletes
PALETTE = {
    "bg_app": ("#eaf3f6", "#0f172a"),
    "sidebar": ("#dceef3", "#13222b"),
    "card": ("#ffffff", "#1e293b"),
    "border": ("#d5e2e7", "#334155"),
    "text_dark": ("#1e293b", "#f1f5f9"),
    "text_muted": ("#64748b", "#94a3b8"),
    "teal_dark": ("#0b6e78", "#0e7490"),
    "teal_hover": ("#095860", "#155e75"),
}


class Authentication(ctk.CTk):
    def __init__ (self):
        super().__init__()
        self._id = None
        self.auth = Auth_Page()
        self.error = None
        self.window = None
        ctk.set_appearance_mode("light")

    @staticmethod
    def change_color(e, color):
        e.widget.config(background=color)

    def login(self) -> str:
        window = ctk.CTk()
        style = ttk.Style()
        window.title("Login")
        window.geometry("700x400")
        window.configure(fg_color=PALETTE["bg_app"])
        window.resizable(False, False)

        self.window = window

        header = ctk.CTkFrame(
            window,
            fg_color=PALETTE["teal_dark"],
            corner_radius=0,
            height=50,
        )
        header.pack(side="top", fill="x")
        header.pack_propagate(False)
        
        ctk.CTkLabel(
            header,
            text="Vehicle Rental Management System",
            font=("Segoe UI", 20, "bold"),
            text_color="#ffffff",
            justify = "center"
        ).pack(padx=24, pady=12)
        
        Label(window,
            text = "Please log in to continue",
            font = ("Comic sans MS", 15, ""),
            justify = "center",
            fg = "#737373",
            bg = "#eaf3f6"
        ).pack(pady = (40, 25 if self.error == False else 0))

        self.error = Label(window,
            text="Incorrect username or password",
            font=("Segoe UI", 10, ""),
            justify="center",
            fg="#eaf3f6",
            bg="#eaf3f6"
        )
        self.error.pack(pady=(5, 20))

        Label(window,
            text="Username:",
            fg="black",
            font=("Segoe UI", 11, "bold"),
            bg="#eaf3f6"
        ).pack(anchor="w", padx=(100, 0))

        self.user_entry = ctk.CTkEntry(window, width=530)
        self.user_entry.pack(padx=24, pady=(5, 8))


        Label(window,
            text="Password:",
            fg="black",
            font=("Segoe UI", 11, "bold"),
            bg="#eaf3f6"
        ).pack(anchor="w", padx=(100, 0))

        self.pass_entry = ctk.CTkEntry(window, width=530, show="•")
        self.pass_entry.pack(padx=24, pady=(5, 8))

        btn_row = Frame(window)
        btn_row.pack(fill="x", padx=24, pady=24)
        self.login_btn = ctk.CTkButton(
            window,
            text="Sign in",
            font=("Segoe UI", 11, "bold"),
            fg_color=PALETTE["teal_dark"],
            hover_color=PALETTE["teal_hover"],
            text_color="#ffffff",
            corner_radius=5,
            height=27,
            width=100,
            command=self.sign_in,
        )
        self.login_btn.pack()


        window.mainloop()

    def sign_in(self):
        username_val = self.user_entry.get().strip()
        password_val = self.pass_entry.get().strip()

        # 1. Required Field Validation
        if not username_val and not password_val:
            mbox.showerror("Error", "Username and Password are required!")
            self.user_entry.focus()
            return
        if not username_val:
            mbox.showerror("Error", "Username is required!")
            self.user_entry.focus()
            return
        if not password_val:
            mbox.showerror("Error", "Password is required!")
            self.pass_entry.focus()
            return

        # self.login_btn.configure(state="disabled", text="Signing in...")
        #check user in database
        id = self.auth.verify_login(username_val, password_val)
        self._id = id

        if id != 0:
            self.window.destroy()
            from admin.content import MainContent
            app = MainContent(self._id)
            app.run()
        else:
            self.error.configure(fg="#FF0000")
            self.login_btn.configure(state="normal", text="Sign in")
            self.user_entry.delete(0, "end")
            self.pass_entry.delete(0, "end")
            self.pass_entry.focus_set()


if __name__ == "__main__":
    auth = Authentication()
    auth.login()