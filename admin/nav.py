import tkinter as tk

class Navigation:

    def __init__(self, parent, main_content, update_title):
        self.buttons = []
        self.parent = parent
        self.main_content = main_content
        self.update_title = update_title
        self.current_page = None

        self.sidebar_frame = tk.Frame(
            parent,
            bg="#95CCDD",
            width=270
        )
        self.sidebar_frame.pack_propagate(False)
        self.sidebar_frame.pack(side="left", fill="y")

        self.create_sidebar()

    def create_sidebar(self):
        buttons = [
            ("Dashboard", "dashboard"),
            ("Vehicles", "vehicles"),
            ("Users", "users"),
        ]
        buttons1 = [
            ("Rent & Return", "rental"),
            ("History", "history")
        ]

        space = tk.Frame(self.sidebar_frame)
        space.pack(pady=50)

        for text, page in buttons:
            button = tk.Button(
                self.sidebar_frame,
                text=text,
                bd = 0,
                bg="#95CCDD",
                fg="#373D3F",
                font=("Verdana", 10, "bold"),
                relief="flat",
                activebackground= "#95CCDD",
                activeforeground="#373D3F",
                command=lambda p=page: self.show_page(p)
            )
            button.pack(pady=7)
            self.buttons.append((button, page))

        hr = tk.Frame(self.sidebar_frame, height=2, bg="#000000", width=150)
        hr.pack(pady=30)

        for text, page in buttons1:
            button = tk.Button(
                self.sidebar_frame,
                text=text,
                bd = 0,
                bg="#95CCDD",
                fg="#373D3F",
                font=("Verdana", 10, "bold"),
                relief="flat",
                activebackground= "#95CCDD",
                activeforeground="#373D3F",
                command=lambda p=page: self.show_page(p)
            )
            button.pack(pady=7)
            self.buttons.append((button, page))

        log_frame = tk.Frame(self.sidebar_frame, bd=2, bg="#0097B2")
        log_frame.pack(pady=(150,0))
        tk.Button(
            log_frame,
            text = "Logout",
            bd = 0,
            bg = "#95CCDD",
            fg =  "#373D3F",
            font=("Verdana", 9, "bold"),
            relief = "flat",
            activebackground= "#0097B2",
            activeforeground="#373D3F",
            width=15
        ).pack()

    def show_page(self, page_name):
        self.current_page = page_name

        # Update navbar title
        self.update_title(page_name)

        # Update sidebar buttons
        for button, page in self.buttons:
            button.config(
                bg="#809BA3" if page == page_name else "#95CCDD",
                width=10 + (15 - len(page)) if page == page_name else 10,
                pady=5
            )

        # Clear previous content
        for widget in self.main_content.winfo_children():
            widget.destroy()

        # Display selected page
        if page_name == "dashboard":
            from .dashboard import Dashboard
            Dashboard(self.main_content)

        elif page_name == "vehicles":
            from .vehicles import Vehicles
            Vehicles(self.main_content)
    @staticmethod

    def navbar(parent, title_text, name):
        header = tk.Frame(parent, bg="#0097B2", height=70)
        header.pack(fill="x")

        tk.Label(
            header,
            text=title_text,
            font=("Verdana", 20, "bold"),
            bg="#0097B2",
            fg="white"
        ).pack(side="left", padx=40, pady=10)

        tk.Label(
            header,
            text=f"Welcome {name} (Admin)",
            bg="#0097B2",
            fg="white",
            font=("Verdana", 12, "bold")
        ).pack(side="right", padx=40)