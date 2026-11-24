from tkinter import *
from tkinter import messagebox as mbox
from pages.authentication import Auth_Page

class Authentication():
    def __init__ (self):
        self._id = None
        self._name = None
        self._role = None
        self._window = None

    @staticmethod
    def change_color(e, color):
        e.widget.config(background=color)

    def login(self):
        window = Tk()
        auth = Auth_Page()
        window.title("Login")
        window.geometry("700x400")
        window.configure(bg="#FFFFFF")
        window.resizable(False, False)


        self._window = window


        icon = PhotoImage(file="img/icon/vrs.png")
        window.iconphoto(True, icon)

        header = Frame(window, bg = "#0097B2", height = 50)
        header.pack(fill = "x")

        header_label = Label(header, text = "Vehicle Rental Management System", font = ("Arial", 20, "bold"), justify = "center", bg = "#0097B2", fg = "#FFFFFF")
        header_label.pack(pady = 10)

        label = Label(window, text = "Please log in to continue", font = ("Comic sans MS", 15, ""), justify = "center", fg = "#737373", bg = "#FFFFFF")
        label.pack(pady = (25, 15))


# ___________________________________________________________________________________________


        username = Label(window, text = "Username:", fg = "black", font = ("Berlin Sans FB Demi", 10, "bold"), bg = "#FFFFFF")
        username.pack(anchor = "w", padx = (100, 0))

        user_input = Frame(window, height = 35, width = 500, highlightbackground = "black", highlightthickness = 1, bg = "#FFFFFF")
        user_input.pack()
        user_input.pack_propagate(False)

        user_entry = Entry(user_input, bg="#FFFFFF", fg="black", bd=0, relief="flat", font=("Arial", 11))
        user_entry.pack(fill="both", expand=True, padx=8, pady=5)


# ___________________________________________________________________________________________


        pass_label = Label(window, text = "Password:", fg = "black", font = ("Berlin Sans FB Demi", 10, "bold"), bg = "#FFFFFF")
        pass_label.pack(anchor = "w", padx = (100, 0), pady = (10, 0))

        pass_input = Frame(window, height = 35, width = 500, highlightbackground = "black", highlightthickness = 1, bg = "#FFFFFF")
        pass_input.pack()
        pass_input.pack_propagate(False)

        pass_entry = Entry(pass_input, bg = "#FFFFFF", fg = "black", bd = 0, relief = "flat", font = ("Arial", 11), show = "*")
        pass_entry.pack(fill = "both", expand = True, padx = 8, pady = 5)
        
        def handle_login():
            username_val = user_entry.get().strip()
            password_val = pass_entry.get().strip()

            # 1. Required Field Validation
            if not username_val and not password_val:
                mbox.showerror("Error", "Username and Password are required!")
                user_entry.focus()
                return
            if not username_val:
                mbox.showerror("Error", "Username is required!")
                user_entry.focus()
                return
            if not password_val:
                mbox.showerror("Error", "Password is required!")
                pass_entry.focus()
                return

            # 2. Database Verification Check
            success, name, role, msg = auth.verify_login(username_val, password_val)
            self._role = role
            self._name = name

            if success:
                mbox.showinfo("Success", msg)
                window.destroy()  # Close the login window

            else:
                mbox.showerror("Login Failed", msg)
                pass_entry.delete(0, END)  # Clear password field on failure

# ___________________________________________________________________________________________

        button_frame = Frame(window, height = 35, width = 50, bg = "#FFFFFF")
        button_frame.pack(pady = (50, 0))
        button_frame.pack_propagate()

        login = Button(
            button_frame,
            text = "Login",
            bg = "#0097B2",
            fg = "#FFFFFF",
            padx = 25,
            font = ("Verdana", 10, "bold"),
            activebackground="#007A90",
            activeforeground="white",
            relief = "flat",
            command = handle_login
        )
        login.pack(side = "left", padx = 10)

        cancel = Button(
            button_frame,
            text = "Cancel",
            bg = "gray",
            fg = "#FFFFFF",
            activebackground="gray",
            activeforeground="white",
            padx = 20,
            font = ("Verdana", 10, "bold"),
            relief = "flat",
            command = window.destroy
        )
        cancel.pack(side = "right", padx = 10)

        login.bind("<Enter>", lambda e: Authentication.change_color(e, "#007A90"))  # Hover color
        login.bind("<Leave>", lambda e: Authentication.change_color(e, "#0097B2"))  # Normal color

        cancel.bind("<Enter>", lambda e: Authentication.change_color(e, "#555555"))  # Darker gray hover
        cancel.bind("<Leave>", lambda e: Authentication.change_color(e, "gray"))


        window.mainloop()

if __name__ == "__main__":
    auth = Authentication()
    auth.login()

    if auth._name:
        from admin.content import MainContent
        app = MainContent(auth._name)
        app.run()